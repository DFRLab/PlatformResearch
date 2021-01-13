# -*- coding: utf-8 -*-

# import modules
import argparse

# import local modules
from utils import *

# parser
parser = argparse.ArgumentParser()

# adding arguments
parser.add_argument(
	'-a',
	'--app',
	required=True,
	type=str,
	choices=[
		'bitchute'
	],
	help='This parameter adds the platform. The program will \
	extract information based on this parameter.'
)

# get arguments
args = vars(parser.parse_args())

# get app
app = args['app']

# objects
scraper = apps_object(app)
scraper()
