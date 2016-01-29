#!/usr/bin/python3
import argparse
import yaml

#set_defaults
def set_defaults():
	config = 'config.yml'
	return
set_defaults()

parser = argparse.ArgumentParser(description='TODO insert description')

parser.add_argument('--config', '-c')
parser.add_argument('--verbose',
	action='store_true',
	help='verbose flag' )

args = parser.parse_args()

#load the configuration file first so that the configuration can be overridden by flags
if args.config:
	config = args.config
#load_config
with open(config, 'r') as ymlfile:
	cfg = yaml.load(ymlfile)



if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")



#save_config