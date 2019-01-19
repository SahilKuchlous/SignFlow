from imutils.video import VideoStream
from imutils.video import FPS
import time
import imutils
import cv2

vs = VideoStream(src=0).start()
time.sleep(1.0)
fps = FPS().start()

def draw(x1, x2, y1, y2, label):
	# draw the prediction on the frame
	cv2.rectangle(frame, (x1, y1), (x2, y2),(0,255,0), 2)
	y = y1 - 15 if y1 - 15 > 15 else y1 + 15
	cv2.putText(frame, label, (x1, y),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	draw(15,152,53,199,"Test")

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

	fps.update()

fps.stop()
print("Elapsed time: {:.2f}".format(fps.elapsed()))
print("Approx. FPS: {:.2f}".format(fps.fps()))
cv2.destroyAllWindows()