import os
folder='/home/kaliw/GITHUB/PYTHON3/PYTUBE'
for file in os.listdir(folder):
	print(file)
	source=folder+file
	re = folder+file+'.mp3'
	os.rename(source,re)