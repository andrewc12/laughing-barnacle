#!/usr/bin/python3
import argparse
import yaml #python3-yaml

#set_defaults
cfg = {}
configfile = 'config.yml'

def save_config():
	with open(configfile, 'w') as ymlfile:
		yaml.dump(cfg, ymlfile)
	return

def load_config():
	global cfg
	with open(configfile, 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return



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
	load_config()
except FileNotFoundError as err:
	save_config()
	load_config()
	#with open(configfile, 'r') as ymlfile:
	#	cfg = yaml.load(ymlfile)

if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")



#save_config