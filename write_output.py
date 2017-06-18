import sys
import pygit2
import re
import string

f = open("output.txt", 'w') 

""" 
the output will be written in a .txt file with name output.txt
the output are the commits in a given repository in GitHub
later the repository URL will be represented with an input variable
we are doing text analysis on the output.txt file

"""
sys.stdout = f

repo = pygit2.Repository('/Users/elpidabantra/tacotron')
repo.path
repo.workdir
commit = repo[repo.head.target]
commit.message

last = repo[repo.head.target]
for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print(commit.message)

f.close()

