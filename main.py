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

nouns = ['NN', 'NNP']
verbs = ['VB', 'VBD', 'VBG', 'VBN']

e_tag = open("englishTagged.txt", "r")
for line in e_tag: # each sentence
	words_tags = line.split(' ')
	tags = [word.split('_')[1].strip() for word in words_tags]
	words = [word.split('_')[0].strip() for word in words_tags]
	
	# combine two proper nouns into one proper noun
	for i, tag in enumerate(tags):
		if tags[i] == 'NNP' and tags[i+1] == 'NNP':
			words[i] = words[i] + ' ' + words[i+1]
			del words[i+1]
			del tags[i+1]

	# when determiner (a word that references a noun) occurs before a noun, combine them into one
	for i, tag in enumerate(tags):
		if tags[i] == 'DT' and tags[i+1] in nouns:
			words[i] = words[i] + ' ' + words[i+1]
			tags[i] = tags[i+1]
			del words[i+1]
			del tags[i+1]

	# VBD - verb past tense, IN - preposition/subordinating conjunction
	# when preposition follows noun, swap them
	# when verb past tense follows noun, swap them
	for i, tag in enumerate(tags):
		if tags[i] in nouns and (tags[i+1] == 'VBD' or tags[i+1] == 'IN'):
			# swap words and tags
			words[i], words[i+1] = words[i+1], words[i]
			tags[i], tags[i+1] = tags[i+1], tags[i]
			
			# append verb to noun
			words[i] = words[i] + ' ' + words[i+1]
			
			del words[i+1]
			del tags[i+1]

	#for i, tag in enumerate(tags):
	#	if words[i] == 'ne':
	#		j = i
	#		while j < len(tags) and tags[j] != 'VBD':
	#			print words[j]
	#			j += 1
	#		if j < len(tags):
	#			words[i] = words[j]
	#			tags[i] = tags[j]

	#			del words[j]
	#			del tags[j]

	#			break

	# today_NN ki_VBP date_NN in_IN

	# noun followed by ki followed by noun - replace with noun's noun
	# i.e. add apostrophe s
	# maintain first tag (i.e. noun)
	for i, tag in enumerate(tags):
		if i < (len(tags)-2):
			if tags[i] in nouns and words[i+1] == 'ki' and tags[i+2] in nouns:
				words[i] = words[i] + '\'s ' + words[i+2]
				del words[i+2]
				del tags[i+2]
				del words[i+1]
				del tags[i+1]

	# if VBZ (mostly 'is'/hai) comes after a verb, change the 'is' to 'has' and swap with the verb
	# maintain first tag (i.e. the verb's tag)
	for i, tag in enumerate(tags):
		if i < len(tags)-1:
			if tags[i+1] == 'VBZ' and tag in verbs:
				if words[i+1] == 'is':
					words[i+1] = 'has'

					# swap
					words[i], words[i+1] = words[i+1], words[i]

					words[i] = words[i] + ' ' + words[i+1]

					del words[i+1]
					del tags[i+1]
	
	# RB - adverb followed by verb, swap them
	for i, tag in enumerate(tags):
		if tag == 'RB' and tags[i+1] == 'VBD':
			words[i], words[i+1] = words[i+1], words[i]
			tags[i], tags[i+1] = tags[i+1], tags[i]
	"""
	for i, tag in enumerate(tags):
		if tags[i] in nouns and tags[i+1] in nouns and (tags[i+2] == 'VBD' or tags[i+2] == 'IN'):
			# insert at index i-1
			pp = words[i+2]
			t = tags[i+2]
			del words[i+2]
			del tags[i+2]
			words.insert(i, pp)
			tags.insert(i, t)
	"""

	# rule 7
	for i, tag in enumerate(tags):
		if words[i] == 'here' and words[i+1] == 'to' and words[i+2] == 'ki':
			del words[i+2]
			del words[i+1]
			del tags[i+2]
			del tags[i+1]
			words[i] = 'even'
		elif words[i] == 'give' and words[i+1] == 'been' and words[i+2] == 'is':
			del words[i+2]
			del words[i+1]
			del tags[i+2]
			del tags[i+1]
			words[i] = 'has been'

	print ' '.join(words)