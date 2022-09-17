import os
folder='/home/kaliw/GITHUB/PYTHON3/PYTUBE'
for file in os.listdir(folder):
	print(file)
	source=folder+'/'
	source=source+file

	temp =source.split(' -')

	re = temp[0]+'.mp3'
	print(source)
	print(re)
	os.rename(source,re)