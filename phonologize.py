# This Python file uses the following encoding: utf-8
# This script has been written for Python 3.
#import re
import os
import re
#import subprocess
from subprocess import Popen, PIPE
from transcribe import first_order_transcription

root='corpora'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]

if not os.path.exists('output'):
	os.makedirs('output')

dico = {}
dico[","]=","
dico["?"]="?"
dico["!"]="!"
dico["."]="."
dico[";"]=";"
dico[":"]=":"
dico['*']='#'
dico['”']='”'
dico['“'] = '“'

process = Popen(["perl","transcriptor.pl"], stdin = PIPE, stdout = PIPE)

for corpusdir in dirlist:
	print('Recoding transcription of:', corpusdir)
	input_location  = 'corpora/' + corpusdir + '/clean'
	output_location = 'output/'  + corpusdir
	if not os.path.exists(output_location):
		os.makedirs(output_location)
	
	foutput = open(output_location + '/phonologized.txt', 'w', encoding = 'utf-8')
	
	with open(input_location + '/extract.txt', encoding = 'utf-8') as input_file:
		for line_ID, line_text in enumerate(input_file):
			line_text = re.sub('\(.*?\)', '', line_text)
			print(line_ID)
			newwords  = []
			full_line = line_text.lower().split()
			info  = full_line[:4] # ID and age
			words = full_line[4:] # Start reading in 5th column, first 4 are ID and age
			
			for i, word in enumerate(words[:-1]):
				if word in dico:
					newwords.append(dico[word])
				else:
					newwords.append(first_order_transcription(word)) #newwords.append(subprocess.check_output(["perl","transcriptor.pl",word]).decode("utf-8", errors = 'ignore'))
			
			newwords.append(full_line[-1])
			print(' '.join(info + newwords), file = foutput) # Concatenate with ID and age and print
	
	foutput.close()

