from imutils.video import VideoStream
from imutils.video import FPS
import time
import imutils
import cv2

vs = VideoStream(src=0).start()
time.sleep(1.0)
fps = FPS().start()

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()