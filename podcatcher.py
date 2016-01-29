#!/usr/bin/python3
import argparse

#set_defaults

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


if args.verbose:
	print("~ Verbose!")
else:
	print("~ Not so verbose")



#save_config