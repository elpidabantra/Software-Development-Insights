import sys
import pygit2
import re
import string
import subprocess
import os
import math

list_of_functions = []

with open('test_fun.txt', 'r') as f1:
	for line in f1:
		line = str(line)
		if "def" in line:
			list_of_functions.append(line.split("def"))

print(list_of_functions)