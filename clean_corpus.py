# This Python file uses the following encoding: utf-8
# This script has been adapted for Python 3.
import re
import os

root='corpora'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]

def clean_text(current_line):
	# This function cleans the CHAT annotations based on the
	# CHILDES transcription guidelines: http://talkbank.org/manuals/CHAT.pdf
	new_line = current_line.replace('www','*') # Untranscribed material
	new_line = new_line.replace('0','')        # Note: In CHAT manual they say 0 means omitted word, but in York they use it a lot even in words that are not likely to be omitted, so I will ignore it for the moment.
	new_line = new_line.replace('xxx','*')     # Unintelligible words
	new_line = new_line.replace('yyy','*')
	new_line = new_line.replace('xx','*')
	new_line = new_line.replace('yy','*')
	new_line = new_line.replace('["]',',')     # I decided to introduce a comma after a quote as there usually are prosodic boundaries.
	new_line = new_line.replace('[*]','')	   # This is a replacement marker (ignore)
	new_line = new_line.replace('[/]',',')	   # This marks a repetition, I will introduce a comma (in the manual it says: ...when a speaker begins to say something, stops and then repeats the earlier material...)
	new_line = new_line.replace('(.)',',')     # Pauses, replaced by commas
	new_line = new_line.replace('(..)',',')
	new_line = new_line.replace('(...)',',')
	new_line = new_line.replace(':eng','')           # This marks english words
	new_line = re.sub('\[:\s[^\]]*\]', '', new_line) # [: smth] This notes the intended word
	new_line = re.sub('\[=\s[^\]]*\]', '', new_line) # [= smth] This notes the meaning of a referent
	new_line = re.sub('\[%\s[^\]]*\]', '', new_line) # [% smth] This is an annotation.
	new_line = re.sub('\[[^\]]*\]', '', new_line)    # Delete the rest of the brackets.
	new_line = re.sub('&=[^ ]*', '', new_line)       # Delete &=event annotations.
	new_line = new_line.replace('+<', '')    # Overlaps (we ignore them)
	new_line = new_line.replace('+"/.', '.') # Quotation follows (included as normal speech)
	new_line = new_line.replace('+"', '')    # Quotation (included as normal speech)
	new_line = new_line.replace('+,', '')    # Completion of utterance after interruption
	new_line = new_line.replace('++', '')    # Other completion
	new_line = new_line.replace('+...', '.') # Incomplete utterance (trailing off).
	new_line = new_line.replace('+..?', '?') # Incomplete question (trailing off).
	new_line = new_line.replace('+.', '.')   # Transcription break
	new_line = new_line.replace('+!?',  '?') # Question with great amazement.
	new_line = new_line.replace('+/.',  '.') # Utterance interrupted.
	new_line = new_line.replace('+/?',  '?') # Question interrupted.
	new_line = new_line.replace('+//.', '.') # Self interruption.
	new_line = new_line.replace('+//?', '?') # Self interruption.
	new_line = new_line.replace('+/', '.')   # If any +/ left, replace by stop.
	new_line = new_line.replace('+', ' ')    # Separate words joined by +
	new_line = new_line.replace('_', '-')    # Composed words transcribed with _ replaced by -
	new_line = new_line.replace(',', ' ,')   # Add space before comma
	new_line = new_line.replace(';', ' ;')   # Add space before semicolon
	new_line = new_line.replace('..', '.')   # Correct double stops
	new_line = new_line.replace('. .', '.')  # Correct double stops
	new_line = new_line.replace('.', ' .')   # Add space before stops
	new_line = new_line.replace('?', ' ?')   # Add space before question mark
	new_line = new_line.replace('!', ' !')   # Add space before exclamation mark
	new_line = new_line.replace('<', '')     # < This marks repetitions, we delete the symbol but keep the citation
	new_line = new_line.replace('>', '')     # > This marks repetitions, we delete the symbol but keep the citation
	new_line = re.sub('.+',' ', new_line) # This is some code for audio files, to discard.
	new_line = re.sub('@.*? ',' ',new_line)   # Special annotations about certain words, we erase the annotation but keep the word.
	new_line = new_line.replace(':','')   # Except for :eng, the colon just indicates a stretch in the sound, so we erase it.
	new_line = new_line.replace("'","") # Remove apostrophe (these have no meaning or use in Spanish)
	new_line = new_line.replace('-', ' ') # Remove dash (these have no meaning or use in Spanish)
	new_line = new_line.replace("⌉","") # Remove this symbol, unclear what it is.
	new_line = new_line.replace("⌈","") # Remove this symbol, unclear what it is. # Note: it is not exactly the same symbol as in the previous line.
	new_line = new_line.replace("⌊","") # Remove this symbol, unclear what it is. # Note: it is not exactly the same symbol as in the previous line.
	new_line = new_line.replace("⌋","") # Remove this symbol, unclear what it is. # Note: it is not exactly the same symbol as in the previous line.
	new_line = new_line.replace('&','') # Remove the ampersand, which indicates an approximate transcription of a word that is not typically in a dictionary.
	new_line = new_line.replace('“', '“ ') # Add a space after opening quotation mark
	new_line = new_line.replace('”', ' ”') # Add a space before closing quotation mark
	return new_line

def print_line(current_line, processed_lines, filename):
	if (current_line[-1] not in ['.','?','!']):
		continue_line = 1 # If line is unfinished (continues in next line) combined processed lines
		processed_lines = processed_lines + current_line.strip() + ' '
	else:
		processed_lines = processed_lines + current_line
		# Final details (potentially multi-line problems):
		processed_lines = processed_lines.replace(', ,',',')
		processed_lines = processed_lines.replace('. .','.')
		processed_lines = processed_lines.replace(', .','.')
		processed_lines = processed_lines.replace(', ?','?')
		processed_lines = processed_lines.replace(', !','!')
		print(processed_lines, file = f)
		processed_lines = ''
		continue_line = 0
	return continue_line, processed_lines

for corpusdir in dirlist:
	print('Processing corpus:', corpusdir)
	input_location = root + '\\' + corpusdir + '\\raw'
	output_location = root + '\\' + corpusdir + '\\clean'
	if not os.path.exists(output_location):
		os.makedirs(output_location)
	
	output_file = output_location + '\\extract.txt'
	f = open(output_file,'w', encoding = 'utf-8')

	# Get filenames to analyse:
	chafiles = []
	counter = 0
	for file in os.listdir(input_location):
		try:
			if file.endswith(".cha"):
				print("cha file found:\t", file)
				chafiles.append(str(file))
				counter = counter + 1
		except Exception as e:
			raise e
			print("No cha files found.")

	print("Total files found:\t", counter)

	# Load participants and child's info:
	participants = []
	age = {}
	with open(root + '\\' + corpusdir + '\\participants.txt') as Plist:
		for line in Plist:
			line = line.replace('spa , eng', 'spa')
			aux = line.split()
			if (aux[0] == '0') and (aux[2] not in participants):
				participants.append(aux[2])
			if ('Target_Child' in aux[5]) or ((aux[2] == 'CHI') and (aux[1] not in age)):
				child_info = aux[5].split('|')
				age[aux[1]] = child_info[3]
				

	# Read and clean files:
	for file in chafiles:
		print("Analysing file: ", file)
		if file in age:
			child_age = age[file]
		else:
			child_age = 'x;xx.xx'
		if child_age[-1] == '.':
			child_age = child_age + '00' # Add 00 days if days missing from age, e.g. age = "2;8."
		elif child_age[-1] == ';':
			child_age = child_age + '0.00' # Add 0 months and 00 days if info missing from age, e.g. age = "2;"
		child_age = re.sub('[;\.]',' ',child_age) # Replace age written as "y;m.d" by "y m d"
		continue_line = 0
		processed_lines = ''
		with open(input_location +'\\'+ file, encoding = 'utf-8') as corpus:	
			for j, line in enumerate(corpus):
				line = line.strip()
				is_adult_speaking = ((line[0] == '*') and (line[1:4] in participants)) or (continue_line == 1)
				if is_adult_speaking:
					if (line[0] == '*'):
						start_text = 6
					else:
						start_text = 0
					thisline = line[start_text:]
					newline  = clean_text(thisline)
					# Final corrections (punctuation marks):
					newline = newline.split()
					if (len(newline) > 0):
						if (continue_line == 0) and (newline[0]==','): # Note: only do this in first line of a dialog
							newline = newline[1:] # Get rid of any comma left at the beginning of the line
						newline = ' '.join(newline)
						
						# Print:
						if (continue_line == 1):
							continue_line, processed_lines = print_line(newline, processed_lines, f)
						elif (continue_line == 0) and (newline != '.') and (newline != '* .') and (newline != '?') and (newline != '!'):
							print(file+' '+child_age,file = f, end = ' ')
							continue_line, processed_lines = print_line(newline, processed_lines, f)

	f.close()
	print('Corpus', corpusdir, 'done!\n')

# TO DO:
# - Remove "&" symbols (but keeping word)? I think it just means words that are not in the dictionary. If using the phonologizer based on orthography, it doesn't matter.
# - check repetitions of lines (e.g. nanananananana in 12f.cha).