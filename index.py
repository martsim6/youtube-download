import pytube

def download_sound(url, path):	
	youtube_video = pytube.YouTube(url)
	sound = youtube_video.streams.filter(only_audio=True).first()
	print('Starting downloading sound from {}'.format(youtube_video.title))
	sound.download(path)
	print("Sound downloaded!")

if __name__ == '__main__':
	url = 'https://www.youtube_video.com/watch?v=7OIvHJ0RvJk'
	download_sound(url, './')


