from pytube import Playlist
p = Playlist('https://www.youtube.com/watch?v=Y3UDx5JFqiw&list=PLUKRqQ8cSB-DCDuEl5vYogIMH9ph-7OP7&ab_channel=BenLionelScott')


for video in p.videos:
	print(video.streams.filter(only_audio=True).get_audio_only())
	audio= video.streams.filter(only_audio=True).get_audio_only()
	audio.download()
	