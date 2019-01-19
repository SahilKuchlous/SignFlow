import os

file = ""
current=""
destination=""

for i in range (3,11):
	print(i)
#	current="/home/vikram/Documents/SignFlow/datasets/user_"+i
	current="datasets/user_"+str(i)
	destination="datasets/test_user_"+str(i)
	for c in range (65,90):
		file=str(ch(c))+str(4)
		os.rename(current+"/"file, "path/to/new/destination/for/"+file)
		file=str(ch(c))+str(9)
		os.rename(current+"/"file, "path/to/new/destination/for/"+file)


