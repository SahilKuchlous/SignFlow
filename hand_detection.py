import cv2
import sys

#cascPath = sys.argv[1]
closed_palm = cv2.CascadeClassifier("Haarcascades/closed_frontal_palm.xml")
palm = cv2.CascadeClassifier("Haarcascades/palm.xml")

video_capture = cv2.VideoCapture(0)

while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	closed_palms = closed_palm.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(31, 31),
		flags=cv2.CASCADE_SCALE_IMAGE
	)

	palms = palm.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=6,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)

	for (x, y, w, h) in closed_palms :
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		y = y - 15 if y - 15 > 15 else y + 15
		cv2.putText(frame, "A", (x, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

	for (x, y, w, h) in palms :
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
		y = y - 15 if y - 15 > 15 else y + 15
		cv2.putText(frame, "B", (x, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 2)

	cv2.imshow('Video', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
