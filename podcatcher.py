#!/usr/bin/python3
import argparse
import yaml #python3-yaml

def save_config():
	
	return

#set_defaults
configfile = 'config.yml'

parser = argparse.ArgumentParser(description='TODO insert description')

parser.add_argument('--config', '-c')
parser.add_argument('--verbose',
	action='store_true',
	help='verbose flag' )

args = parser.parse_args()

#load the configuration file first so that the configuration can be overridden by flags
if args.config:
	configfile = args.config
#load_config
try:
	with open(configfile, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
except FileNotFoundError as err:
	save_config()
	#with open(configfile, 'r') as ymlfile:
	#	cfg = yaml.load(ymlfile)

if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")



#save_config