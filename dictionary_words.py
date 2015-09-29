import random
from sys import argv

content = open('/usr/share/dict/words').read().split()
openfile_list = []
for words in content:
    openfile_list.append(words)
sentence = []
while len(sentence) < int(argv[1]):
        sentence.append(openfile_list[random.randint(0, len(openfile_list))])
        print(*sentence)
    # argv - method for the command line with the index of
    # 1 so a valid argument can be passed,
    # instead of an index of 0
