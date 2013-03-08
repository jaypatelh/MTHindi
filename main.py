import re

f = open("dict.txt", "r")
hindidict = dict()

for line in f:
	words = line.split("\t")
	if words[0] == '\n':
		continue
	hindidict[words[0]] = words[1].strip()

print hindidict