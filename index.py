import pytube
import subprocess
import re
import requests

def get_opened_urls():
	command = ['bt', 'list']
	all_tabs = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
	all_tabs = all_tabs.decode('utf-8')
	match_url = re.findall(r'htt.*youtube\.com/watch.*', all_tabs)
	if match_url:
		return match_url
	else:
		return None
	

def download_sound(url, path):	
	youtube_video = pytube.YouTube(url)
	try:
		sound = youtube_video.streams.filter(only_audio=True).first()
		print('Starting downloading sound from {}'.format(youtube_video.title))
		sound.download(path)
		print("Sound downloaded!")
	except:
		print("Cant download sound!")


if __name__ == '__main__':
	urls = get_opened_urls()
	if urls:
		for url in urls:
			download_sound(url, './')
	else:
		print('No Youtube tabs currently opened in firefox. Can`t download anything')