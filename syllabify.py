# This Python file uses the following encoding: utf-8

# Script written by Julia Carbajal, adapted from a perl script written by Xavier López Morrás.
# Original perl script: http://www.aucel.com/pln/transbase.html

#import sys

#word = str(sys.argv[1])
punctuation = [',', '.', '?', '!', ';', ':', '#', '”', '“']

obstruents_in_OL_clusters = ['p','t','k','b','d','g','f','β','ɣ','ð']
liquids = ['r','l']

unstressed_vowels = ['a','e','i','o','u']
stressed_vowels = ['A','E','I','O','U']
all_vowels = unstressed_vowels + stressed_vowels

semivowels = ['j', 'w']

onset_consonants = ['b','β','d','ð','f','g','ɣ','h','k','l','ʎ','m','M','n','N','ɲ','ŋ','p','r','R','s','t','v','x','X','y','z','θ','ʝ']
coda_consonants = ['b','d','ð','g','k','l','m','M','n','N','ŋ','ʎ','θ','p','r','s','x','z']

NSV = ['n','s','a','e','i','o','u']

def is_OL_cluster(phon1,phon2):
	if phon1 in obstruents_in_OL_clusters and phon2 in liquids:
		return True
	else:
		return False

def syllabify(current_word):
#	for n, current_word in enumerate(phrase):
	if current_word not in punctuation:
		phonemes = '~~~~' + current_word.replace('tʃ','X') + '~'
		k = len(phonemes)-2
		syllables = []
		stressed_syllable_found = 0
		while phonemes[k] != '~':
			last_phon = phonemes[k]     # Last phoneme in the sequence
			minus1_phon = phonemes[k-1] # Previous to last
			minus2_phon = phonemes[k-2] # Second to last
			minus3_phon = phonemes[k-3] # Third to last
			minus4_phon = phonemes[k-4] # Fourth to last
			next_phon = phonemes[k+1]   # Next phoneme
			
			# CV
			if last_phon in all_vowels and minus1_phon in onset_consonants and not is_OL_cluster(minus2_phon,minus1_phon):
				syllable = minus1_phon + last_phon
				k = k - 2

			#CVC
			elif last_phon in coda_consonants and minus1_phon in all_vowels and minus2_phon in onset_consonants and not is_OL_cluster(minus3_phon,minus2_phon):
				syllable = minus2_phon + minus1_phon + last_phon
				k = k - 3
			
			# V
			elif last_phon in all_vowels and not minus1_phon in onset_consonants + semivowels:
				syllable = last_phon;
				k = k - 1

			#VC
			elif last_phon in coda_consonants and minus1_phon in all_vowels + semivowels and not minus2_phon in onset_consonants + semivowels:
				syllable = minus1_phon + last_phon
				k = k - 2
				
			#VCC
			elif last_phon == 's' and minus1_phon in ['k','n'] and minus2_phon in all_vowels and not is_OL_cluster(minus4_phon,minus3_phon):
				syllable = minus2_phon + minus1_phon + last_phon
				k = k - 3
				
			#CCV
			elif last_phon in all_vowels and is_OL_cluster(minus2_phon,minus1_phon):
				syllable = minus2_phon + minus1_phon + last_phon
				k = k - 3
				
			#CCVC
			elif last_phon in coda_consonants and minus1_phon in all_vowels and is_OL_cluster(minus3_phon,minus2_phon):
				syllable = minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 4
			
			# CVCC
			elif last_phon == 's' and minus1_phon == 'b' and minus2_phon in all_vowels and minus3_phon == 's':
				syllable = minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 4
				
			#CCVCC
			elif last_phon == 's' and minus1_phon == 'n' and minus2_phon in all_vowels and is_OL_cluster(minus4_phon,minus3_phon):
				syllable = minus4_phon + minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 5
			
			# DIPHTHONGS
			#CVS & VS
			elif last_phon in semivowels and minus1_phon in unstressed_vowels and not is_OL_cluster(minus3_phon,minus2_phon):
				if minus2_phon in onset_consonants:
					syllable = minus2_phon + minus1_phon + last_phon
					k = k - 3
				else:
					syllable = minus1_phon + last_phon
					k = k - 2
					
			#CSV
			elif last_phon in all_vowels and minus1_phon in semivowels and minus2_phon in onset_consonants and not is_OL_cluster(minus3_phon,minus2_phon): #unless encontrada == 1??
				syllable = minus2_phon + minus1_phon + last_phon
				k = k - 3
			
			#SV
			elif last_phon in unstressed_vowels and minus1_phon in semivowels and not minus2_phon in onset_consonants + liquids:
				syllable = minus1_phon + last_phon
				k = k - 2
			
			#SVC
			elif last_phon in coda_consonants and minus1_phon in unstressed_vowels and minus2_phon in semivowels and not minus3_phon in onset_consonants:
				syllable = minus2_phon + minus1_phon + last_phon
				k = k - 3

			#CSVC
			elif last_phon in ['c','k','s','z','n','N','p','l','r','m','ŋ','θ'] and minus1_phon in all_vowels and minus2_phon in semivowels and minus3_phon in onset_consonants: #cksznNplrçm
				syllable = minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 4
				
			#CCSV
			elif last_phon in all_vowels and minus1_phon in semivowels and is_OL_cluster(minus3_phon,minus2_phon):
				syllable = minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 4
			
			#CCVS
			elif last_phon in semivowels and minus1_phon in unstressed_vowels and is_OL_cluster(minus3_phon,minus2_phon):
				syllable = minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 4

			#CCSVC
			elif last_phon in ['c','k','s','z','n','N','p','l','r','m','ŋ'] and minus1_phon in unstressed_vowels and minus2_phon in semivowels and is_OL_cluster(minus4_phon,minus3_phon):
				syllable = minus4_phon + minus3_phon + minus2_phon + minus1_phon + last_phon
				k = k - 5

			# #Other cases
			
                # if ( ($letra0=~/[jw]/) )  {
                # unless ( $letra1=~/[aeioubBcdDfgGhklLmnNñprRstvxXyzZ]/  ) {
                # $silaba= $letra0;
                # ##print "$silaba*<br>";
                # ##$tonica_encontrada=1;
                # }
                        # if ($letra1=~/[bBcdDfgGhklLmnNñprRstvxXyzZ]/) {
                        # $silaba=$letra1.$letra0;
                        # print "$silaba:<br>";
                        # $n2--;
                        # }
                # }

			else:
				syllable = '#'
			
			# If already contains a stressed vowel:
			if any(phon in stressed_vowels for phon in syllable):
				syllable = "'" + syllable
				stressed_syllable_found = True
				
			syllables.insert(0,syllable)
			
			if syllable == '#':
				syllables = '#'
				templist = list(phonemes)
				templist[k] = '~'
				phonemes = ''.join(templist)
		
		## FINDING STRESSED SYLLABLE ##
		if (stressed_syllable_found == False) and (len(syllables) > 1):
			if syllables[-1][-1] not in NSV:
				syllables[-1] = "'" + syllables[-1]
			else:
				syllables[-2] = "'" + syllables[-2]
		elif (stressed_syllable_found == False) and (len(syllables) == 1):
			if (syllables[0] in ['ir', 'ba']) or (len(syllables[0]) >= 3 and syllables[0] not in ['los', 'las']):
				syllables[0] = "'" + syllables[0]
				
		return '-'.join(syllables).replace('X','tʃ')

# word = 'jerβa'
# print(word)
# print(syllabify(word))
# word = 'kasa'
# print(word)
# print(syllabify(word))
# word = 'komer'
# print(word)
# print(syllabify(word))
# word = 'papelOn'
# print(word)
# print(syllabify(word))
# word = 'mar'
# print(word)
# print(syllabify(word))
# word = 'lo'
# print(word)
# print(syllabify(word))
# word = 'los'
# print(word)
# print(syllabify(word))
# word = 'komponen'
# print(word)
# print(syllabify(word))
# word = 'beloθ'
# print(word)
# print(syllabify(word))

# word = 'kosta'
# print(word)
# print('-'.join(syllabify(word)))
# word = 'kordOn'
# print(word)
# print('-'.join(syllabify(word)))
# word = 'katre'
# print(word)
# print('-'.join(syllabify(word)))
# word = 'transporte'
# print(word)
# print('-'.join(syllabify(word)))
# word = 'a'
# print(word)
# print('-'.join(syllabify(word)))