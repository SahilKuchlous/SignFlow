from imutils.video import FPS
import cv2
import csv

fps = FPS().start()

def draw(x1, x2, y1, y2, label):
	cv2.rectangle(img, (x1, y1), (x2, y2),(0,255,0), 2)
	y = y1 - 15 if y1 - 15 > 15 else y1 + 15
	cv2.putText(img, label, (x1, y),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

with open('datasets/user_3/user_3_loc.csv') as csvfile:
    readCSV = list(csv.reader(csvfile, delimiter=','))
    for row in readCSV[1:]:
    	img = cv2.imread("datasets/"+(row[0].replace('\\', '/')))
    	print(row[1],row[3],row[2],row[4])
    	draw(int(row[1]),int(row[3]),int(row[2]),int(row[4]),"test")
    	cv2.imshow("img",img)
    	cv2.waitKey()
    	fps.update()

