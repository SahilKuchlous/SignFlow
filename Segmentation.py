#Signflow
#Importing dependencies
import cv2
import numpy
import glob
import pandas as pd


def crop(img, x1, x2, y1, y2, scale):
    crp=img[y1:y2,x1:x2]
    crp=resize(crp,((scale, scale))) 
    return crp

for 

def get_data(user_list, img_dict, datasets/):
  X = []
  Y = []

  for user in user_list:
    user_images = glob.glob(data_directory+user+'/*.jpg')

    boundingbox_df = pd.read_csv(data_directory + user + '/' + user + '_loc.csv')

'''    for rows in boundingbox_df.iterrows():
      cropped_img = crop( img_dict[rows[1]['image']], 
                         rows[1]['top_left_x'], 
                         rows[1]['bottom_right_x'], 
                         rows[1]['top_left_y'], 
                         rows[1]['bottom_right_y'], 
                         128
                        )
       hogvector = convertToGrayToHOG(cropped_img)

       X.append(hogvector.tolist())
       Y.append(rows[1]['image'].split('/')[1][0])

    return X, Y
'''