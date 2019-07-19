import cv2
image = cv2.imread('circles.png')
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(grayImage,127,255)
contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print ("Length of contours = ",len(contours))
for count in contours:
	approx = cv2.approxPolyDP(count,0.01 * cv2.arcLength(count,True),True)
	print ("\n",len(approx))
	x = approx.ravel()[0]
	y = approx.ravel()[1]
	if len(approx) == 3:
		cv2.putText(image,"Triangle",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
		print ("Triangle")
	elif len(approx) == 4:
		cv2.putText(image,"Square",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
		print ("Square")
	elif len(approx) > 10:
		cv2.putText(image,"Circle",(x,y+30),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,127),1)
		print ("Circle")
	cv2.drawContours(image,[count],-1,(0,255,0),3)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()