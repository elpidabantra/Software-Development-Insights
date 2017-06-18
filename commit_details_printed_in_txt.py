import sys
import pygit2
import re
import string
import subprocess
import os






f = open("commit_details.txt", 'w')
sys.stdout = f


repo = pygit2.Repository('/Users/elpidabantra/Desktop/tacotron')
print(repo.path)
print(repo.workdir)
print("\n")

kr=subprocess.Popen('git log --author="Kyubyong Park" --oneline --shortstat',shell='False') #can be used to run the commandline command
print(kr)
commit = repo[repo.head.target]
commit.message

last = repo[repo.head.target]
for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print("The commit message is",commit.message)
    print(commit.commit_time)
    print("Committed by",commit.author.name, commit.author.email)
    print("\n")
f.close()




f = open("noi.txt", 'w')
sys.stdout = f


frequency_commit = {}
frequency_import = {}

document_text = open('commit_details.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{2,20}\b', text_string)

for word in match_pattern:

    if word == "commit":
        count_commit = frequency_commit.get(word,0)
        frequency_commit[word] = count_commit + 1

    if word == "import":
        count_import = frequency_import.get(word,0)
        frequency_import[word] = count_import + 1

frequency_list1 = frequency_commit.keys()
frequency_list2 = frequency_import.keys()


for words in frequency_list2:
    print(frequency_import[words])

for words in frequency_list1:
    print(frequency_commit[words])



f.close()







