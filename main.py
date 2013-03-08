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
	e.write(".\n")

"""
nouns = ['NN', 'NNP']
verbs = ['VB', 'VBD', 'VBG', 'VBN']

e_tag = open("englishTagged.txt", "r")
for line in e_tag: # each sentence
	words_tags = line.split(' ')
	tags = [word.split('_')[1].strip() for word in words_tags]
	words = [word.split('_')[0].strip() for word in words_tags]
	
	# rule 1
	for i, tag in enumerate(tags):
		if tags[i] == 'NNP' and tags[i+1] == 'NNP':
			words[i] = words[i] + " " + words[i+1]
			del words[i+1]
			del tags[i+1]

	# rule 1
	for i, tag in enumerate(tags):
		if tags[i] == 'DT' and tags[i+1] in nouns:
			words[i] = words[i] + " " + words[i+1]
			tags[i] = tags[i+1]
			del words[i+1]
			del tags[i+1]		

	# rule 2
	for i, tag in enumerate(tags):
		if tags[i] in nouns and (tags[i+1] == 'VBD' or tags[i+1] == 'IN'):
			words[i], words[i+1] = words[i+1], words[i]
			tags[i], tags[i+1] = tags[i+1], tags[i]

	# rule 3
	for i, tag in enumerate(tags):
		if i < (len(tags)-2):
			if tags[i] in nouns and words[i+1] == 'ki' and tags[i+2] in nouns:
				del words[i+1]
				del tags[i+1]
				words[i] = words[i] + '\'s'

	# rule 5
	for i, tag in enumerate(tags):
		if i < len(tags)-1:
			if tags[i+1] == 'VBZ' and tag in verbs:
				if words[i+1] == 'is':
					words[i+1] = 'has'
					words[i], words[i+1] = words[i+1], words[i]
					tags[i], tags[i+1] = tags[i+1], tags[i]

	# rule 6
	for i, tag in enumerate(tags):
		if tags[i] in nouns and tags[i+1] in nouns and (tags[i+2] == 'VBD' or tags[i+2] == 'IN'):
			# insert at index i-1
			pp = words[i+2]
			t = tags[i+2]
			del words[i+2]
			del tags[i+2]
			words.insert(i, pp)
			tags.insert(i, t)

	# rule 7
	for i, tag in enumerate(tags):
		if words[i] == 'here' and words[i+1] == 'to' and words[i+2] == 'ki':
			del words[i+2]
			del words[i+1]
			del tags[i+2]
			del tags[i+1]
			words[i] = 'even'

	print ' '.join(words)
"""