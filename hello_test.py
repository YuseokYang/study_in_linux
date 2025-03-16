#!/usr/bin/env python3
'''
Tests for hello.py
'''

import os
import sys
import subprocess
import pytest

prg = './hello.py'


#---------------------------------------------
def test_exists():
	'''1. Check file exists'''
	assert os.path.isfile(prg), f"{prg} is not exist"


#---------------------------------------------
def test_runnable():
	'''2. Runs using python3'''
	result = subprocess.run([sys.executable, prg], capture_output=True, text=True)
	assert result.returncode == 0, "Script execution failed"
	assert result.stdout.strip() == "Hello, World!"


#---------------------------------------------
def test_executable():
	'''3. Sayss "Hello, World!" by default'''
	result = subprocess.run([prg], capture_output=True, text=True)
	assert result.returncode == 0, 'Execution failed'
	assert result.stdout.strip() == 'Hello, World!'


#----------------------------------------------
@pytest.mark.parametrize('flag', ['-h', '--help'])
def test_uasge(flag):
	'''4. usage (check -h, --help option exist)'''
	result = subprocess.run([prg, flag], capture_output=True, text=True)
	assert result.returncode == 0, f'{flag} execution failed'
	assert result.stdout.lower().startswith('usage'), f'No {flag} usage'


#----------------------------------------------
@pytest.mark.parametrize("option, val", [('-n', 'Universe'), ('--name', 'honguk')])
def test_input(option, val):
	'''5. test for input'''
	result = subprocess.run([prg, option, val], capture_output=True, text=True)
	assert result.returncode == 0, f"{option} {val} execution failed"
	assert result.stdout.strip() == f'Hello, {val}!', 'Unexpected output'
