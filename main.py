# build dictionary
d = open("dict.txt", "r")
hindidict = dict()

for line in d:
	words = line.split("\t")
	if words[0] == '\n':
		continue
	hindidict[words[0]] = words[1].strip()

d.close()

# read hindi sentences
h = open("hindi.txt", "r")
sentences = []

for line in h:
	words = line.split(" ")
	english_trans = []
	for i, word in enumerate(words):
		if word[-1] == '\n' or word[-1] == ',':
			word = word[:-1]
		english_trans.append(hindidict[word].strip())
	sentences.append(" ".join(english_trans))

h.close()

# write translated words to new file
e = open("english.txt", "w")
for sentence in sentences:
	e.write(sentence)
	e.write("\n")