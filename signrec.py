import cv2
import pandas as pd
from skimage.feature import hog
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
import glob
from sklearn.svm import SVC
import pickle
def crop(img, x1, x2, y1, y2, scale):
	crp=img[y1:y2,x1:x2]
	crp=resize(crp, ((scale, scale))) 
	return crp
def process(img):
	bwimg = rgb2gray(img)
	return hog(bwimg)

user_list = map(str, [3, 4, 5, 6, 7, 9, 10])
X = []
Y = []
for user in user_list:
	user_images = glob.glob("datasets/user_"+user+"/*.jpg")
	boxes = pd.read_csv("datasets/user_"+user+"/user_"+user+"_loc.csv")
	img_dict = {}
	for img in user_images:
		img_dict[img[9:]] = io.imread(img)
	for row in boxes.iterrows():
		cropped_image = crop(img_dict[row[1]['image']],
			row[1]['top_left_x'],
			row[1]['bottom_right_x'],
			row[1]['top_left_y'],
			row[1]['bottom_right_y'],
			128
			)
		hogvec = process(cropped_image)
		X.append(hogvec.tolist())
		Y.append(row[1]['image'.split('\\')[1][0]])
label_encoder = LabelEncoder().fit(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'])
Y = self.label_encoder.fit_transform(Y)
svcmodel = SVC(kernel='linear', C=0.9, probability=True)
sign_detector = scvmodel.fit(X, Y)