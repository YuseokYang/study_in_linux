#!/usr/bin/env python3
'''
Autjor: Yuseok Yang <ysyang1009@naver.com>
Purpose: change text to uppercase
'''

import os
import re
import random
import string
import subprocess

prg = './howler.py'


#---------------------------------------
def random_string():
	'''generate a random string'''
	k = random.randint(5,10)
	random_str = random.choices(string.ascii_letters + string.digits, k=k)
	return ''.join(random_str)


#---------------------------------------
def out_flag():
	'''Either -o or --outfile'''
	return '-o' if random.randint(0,1) else '--outfile'


#---------------------------------------
def run_command(cmd):
	'''Run a shell command safelt and return (returncode, returnstdout)'''
	result = subprocess.run(cmd, capture_output=True, text=True)
	return result.returncode, result.stdout.strip()


#---------------------------------------
def test_exists():
	'''exist'''
	assert os.path.isfile(prg)


#---------------------------------------
def test_usage():
	'''usage'''
	for flag in ['-h', '--help']:
		rv, out = run_command([prg, flag])
		assert rv == 0, '-h usage not exist'
		assert re.match('usage', out, re.IGNORECASE)


#----------------------------------------
def test_text_stdout():
	'''Test STDIN/STDOUT'''
	rv, out = run_command([prg, 'foo bar baz'])
	assert rv == 0
	assert out == 'FOO BAR BAZ'


#----------------------------------------
def test_text_outfile():
	'''Test STDIN/outfile'''

	out_file = random_string()
	if os.path.isfile(out_file):
		os.remove(out_file)

	try:
		rv, out = run_command([prg, out_flag(), out_file, 'foo bar baz'])
		assert rv == 0
		assert out == ''
		assert os.path.isfile(out_file)

		with open(out_file, 'r') as out_file_reader:
			text = out_file_reader.read().strip()
		assert text == 'FOO BAR BAZ'
	finally:
		if os.path.isfile(out_file):
			os.remove(out_file)


#-------------------------------------------
def test_file():
	'''Test file in/out'''

	for expected_file in os.listdir('test-outs'):
		try:
			out_file = random_string()
			if os.path.isfile(out_file):
				os.remove(out_file)

			basename = os.path.basename(expected_file)
			in_file = os.path.join('../inputs', basename)

			rv, out = run_command([prg, out_flag, out_file, in_file])
			assert rv == 0
			assert out == ''

			with open(out_file) as out_file_reader:
				produced = out_file_reader.read().strip()

			with open(os.path.join('test-outs', expected_file)) as filereader:
				expected = filereader.read().strip()

			assert expected == produced
		finally:
			if os.path.isfile(out_file):
				os.remove(out_file)
