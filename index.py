import pytube
import subprocess
import re
import argparse
from pathlib import Path

def set_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', help="Set path where to save downloading sound. Default = '~/Download/'", action='store_true')
	args = parser.parse_args()
	return args


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
	args = set_arguments()
	urls = get_opened_urls()
	if urls:
		for url in urls:
			home_path = str(Path.home())
			path = args.path if args.path  else '{}/Downloads/'.format(home_path)
			download_sound(url, path)
	else:
		print('No Youtube tabs currently opened in firefox. Can`t download anything')