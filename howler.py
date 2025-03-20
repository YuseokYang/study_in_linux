#!/usr/bin/env python3
'''change uppercase and print'''

import argparse
import os


#-----------------------------------
def get_args():
	parser = argparse.ArgumentParser(description='change uppercase and print', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('text', metavar='str', help='input text')

	parser.add_argument('-o', '--outfile', metavar='file_name', help='output > output_file')
	return parser.parse_args()


#-----------------------------------
def main():
	args = get_args()
	text = args.text

	if os.path.isfile(text):
		with open(text, 'r') as input_file:
			string = input_file.read()
			string = string.upper()
	else:
		string = text.upper()

	if args.outfile:
		outfile = args.outfile
		with open(outfile, 'w') as output_file:
			output_file.write(string)
	else:
		print(string)


#------------------------------------
if __name__ == '__main__':
	main()
	
