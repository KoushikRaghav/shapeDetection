import cv2
import glob

def detectGeometricShapes(image,x,y,approx):
	if len(approx) == 3:
		cv2.putText(image,"Triangle",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
		print("Triangle")
	elif len(approx) == 4:
		(xAxis,yAxis,width,height) = cv2.boundingRect(approx)
		if((float(width)/height) <= 1.5):
			cv2.putText(image,"Square",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
			print("Square")
		else:
			cv2.putText(image,"Rectangle",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
			print("Rectangle")
	elif len(approx) > 10:
		cv2.putText(image,"Circle",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
		print("Circle")

def getContours(canny):
	contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	return contours,hierarchy

def getCannyEdges(grayImage):
	canny = cv2.Canny(grayImage,127,255)
	return canny

def getPathofImages():
	path = '/home/linuxuser/Python-3.5.6/shapes'
	return path

def main():
	print ("\n<--- GEOMETRIC SHAPE DETECTION --->\n")
	path = getPathofImages()
	files = [f for f in glob.glob(path + "**/*.png",recursive=True)]
	for f in files:
		print(f)
		image = cv2.imread(f)
		grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		canny = getCannyEdges(grayImage)
		contours,hierarchy = getContours(canny)
		print ("Length of contours = ",len(contours))
		for count in contours:
			approx = cv2.approxPolyDP(count,0.01*cv2.arcLength(count,True),True)
			print ("\n",len(approx))
			x = approx.ravel()[0]
			y = approx.ravel()[1]
			detectGeometricShapes(image,x,y,approx)
			cv2.drawContours(image,[count],-1,(0,255,0),3)
		cv2.imshow('image',image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

if __name__ == '__main__':						
	main()