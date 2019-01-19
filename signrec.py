import cv2
import pandas as pd
from skimage.feature import hog
from skimage import io
import glob
def crop(img, x1, x2, y1, y2, scale):
	crp=img[y1:y2,x1:x2]
	crp=resize(crp,((scale, scale))) 
	return crp
user_list = map(str, [3, 4, 5, 6, 7, 9, 10])
X = []
Y = []
for user in user_list:
	user_images = glob.glob("datasets\\user_"+user+"\\*.jpg")
	boxes = pd.read_csv("datasets\\user_"+user+"\\user_"+user+"_loc.csv")
	img_dict = {}
	for img in user_images:
		print(img[9:])
		img_dict[img[9:]] = io.imread(img)
	for row in boxes.iterrows():
		cropped_image = crop(img_dict[row[1]['image']],
			row[1]['top_left_x'],
			row[1]['top_left_y'],
			row[1]['bottom_right_x'],
			row[1]['bottom_right_y'],
			128
			)
		print(cropped_image)