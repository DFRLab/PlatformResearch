# -*- coding: utf-8 -*-

'''
Fuctions

	- get_time
	- check_dir
	- bitchute_collector
	- apps_object
'''

# import modules
import pandas as pd
import time
import os

# import submodules
from pathlib import Path
from datetime import datetime
from modules import bitchute as bc

# get time
def get_time():
	'''
	'''
	return str(int(datetime.utcnow().timestamp()))

# create directory if it does not exists
def check_dir(path):
	'''
	'''
	if not os.path.exists(path):
		Path(path).mkdir(parents=True, exist_ok=True)

# convert to int -> view_count
def convert_view_count_to_int(value):
	'''
	'''
	try:
		value = int(value)
	except ValueError:
		value = 0

	return value


# bitchute collector
def bitchute_collector():
	'''
	This function will retrive data from the
	platform BitChute
	'''

	# BitChute instance
	b = bc.Crawler(headless=False)

	results_base = './data/bitchute-results/'
	check_dir(results_base)

	# get data path
	data_path = os.path.abspath('./data/bitchute-results/')

	print ('')
	ini = time.ctime()
	print ('')
	print (f'Init program --> {ini}')
	print ('')

	print (f'All data will be save in this folder: {data_path}')
	print ('')
	print ('')

	'''
	Getting data
	
	'''

	print ('Getting popular videos...')
	popular_path = os.path.join(results_base, 'popular-videos')
	check_dir(popular_path)
	
	# popular videos
	rv, tags = b.get_recommended_videos(type='popular')
	rv['view_count'] = rv['view_count'].apply(
		convert_view_count_to_int
	)

	# saving data and tags in csv and xlsx formats
	popular_path_file = os.path.join(
		popular_path,
		'popular_videos.{}'
	)

	popular_tags_path_file = os.path.join(
		popular_path,
		'popular_tags.{}'
	)

	rv.to_csv(
		popular_path_file.format('csv'),
		encoding='utf-8',
		sep=',',
		index=False
	)

	rv.to_excel(
		popular_path_file.format('xlsx'),
		index=False
	)

	tags.to_csv(
		popular_tags_path_file.format('csv'),
		encoding='utf-8',
		sep=',',
		index=False
	)

	tags.to_excel(
		popular_tags_path_file.format('xlsx'),
		index=False
	)

	# finish
	print ('done!')
	print ('')

	
	# trending videos
	print ('Getting trending videos...')
	trending_videos_path = os.path.join(
		results_base,
		'trending-videos'
	)
	check_dir(trending_videos_path)
	rv, tags = b.get_recommended_videos(type='trending')
	rv['view_count'] = rv['view_count'].apply(
		convert_view_count_to_int
	)

	# saving data and tags in csv and xlsx formats
	trending_path_file = os.path.join(
		trending_videos_path,
		'trending_videos.{}'
	)

	trending_tags_path_file = os.path.join(
		trending_videos_path,
		'trending_tags.{}'
	)

	rv.to_csv(
		trending_path_file.format('csv'),
		encoding='utf-8',
		sep=',',
		index=False
	)

	rv.to_excel(
		trending_path_file.format('xlsx'),
		index=False
	)

	tags.to_csv(
		trending_tags_path_file.format('csv'),
		encoding='utf-8',
		sep=',',
		index=False
	)

	tags.to_excel(
		trending_tags_path_file.format('xlsx'),
		index=False
	)

	# finish
	print ('done!')
	print ('')


	# recommended channels
	print ('Getting recommended channels...')
	recommended_channels_path = os.path.join(
		results_base,
		'recommended-channels'
	)
	check_dir(recommended_channels_path)
	rc = b.get_recommended_channels(extended=False)

	# saving recommended channels in csv and xlsx formats
	channels_path_file = os.path.join(
		recommended_channels_path,
		'recommended_channels.{}'
	)

	rc.to_csv(
		channels_path_file.format('csv'),
		encoding='utf-8',
		sep=',',
		index=False
	)

	rc.to_excel(
		channels_path_file.format('xlsx'),
		index=False
	)

	# finish
	print ('done!')
	print ('')

	return


# apps object
def apps_object(app):
	'''
	This function will return a function based on the selected app
	'''
	functions = {
		'bitchute': bitchute_collector
	}

	return functions[app]
