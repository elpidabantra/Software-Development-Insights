import sys
import pygit2
import re
import string
import subprocess
import os




f = open("commit_by_author.txt", 'w')
sys.stdout = f


repo = pygit2.Repository('/Users/elpidabantra/Desktop/tacotron')

kr=subprocess.Popen('git log --author="Kyubyong Park" --oneline --shortstat',shell='False') #can be used to run the commandline command
commit = repo[repo.head.target]
commit.message

last = repo[repo.head.target]


for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print(commit.author.name)


f.close()



f = open("noa.txt", 'w')
sys.stdout = f

list_of_authors = []


with open('commit_by_author.txt') as f:
	for word in f:
		if word not in list_of_authors:
			list_of_authors.append(word)

for i in list_of_authors:
	print(i)

print(len(list_of_authors))


f.close()








