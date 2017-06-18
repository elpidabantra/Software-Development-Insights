import sys
import pygit2
import re
import string
import subprocess
import os
import math


commits_by_author = {}

with open('noa.txt') as f1:
	for author in f1:
		commits_by_author[author] = 0;

f1.close()
	
	

with open('commit_by_author.txt') as f2:
	for author in f2:
		commits_by_author[author] = commits_by_author[author] + 1 ;
f2.close()


num_of_com = 0

with open('noi.txt',"r") as f1:
	f1.seek(0, 1)
	for k in f1:
		num_of_com = k

f1.close()



ratio_of_commits = []


for author in commits_by_author:
	if commits_by_author[author] is not 0:
		ratio_of_commits.append(int(commits_by_author[author]) / int(num_of_com))


f = open("ratio_of_commits.txt", 'w')
sys.stdout = f




print(ratio_of_commits)


f.close()



