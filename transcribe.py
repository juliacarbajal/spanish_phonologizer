# This Python file uses the following encoding: utf-8

# Script written by Julia Carbajal, adapted from a perl script written by Xavier López Morrás.
# Original perl script: http://www.aucel.com/pln/transbase.html

#import sys

#word = str(sys.argv[1])

def first_order_transcription(word):
	esp = 0
	voc = 0
	quality = 0
	vowels = ['a','e','i','o','u','á','é','í','ó','ú']
	liquids = ['r','l']
	transcription = ''
	skip = False
	esps = 0

	for n, current_letter in enumerate(word):
		if skip == False:
			if n == len(word)-1:
				next_letter = ''
				esps = 1
			else:
				next_letter = word[n+1]
			if n < len(word)-2:
				next_letter2 = word[n+2]
			else:
				next_letter2 = ''
			if n == 0:
				prev_letter = ''
			else:
				prev_letter = word[n-1]
			
			if (current_letter == "a"):
				phone=  "a"
				quality = "vocal"
				voc = "a"
				esp = 0

			elif (current_letter == "á"):
				phone=  "A"
				quality = "vocal"
				voc = "a"
				esp = 0
				

			elif (current_letter == "é"):
				phone=  "E"
				quality = "vocal"
				voc = "e"
				esp = 0 


			elif (current_letter == "í"):
				phone=  "I"
				quality = "vocal"
				voc = "ii"
				

			elif (current_letter == "ó"):
				phone=  "O"
				quality = "vocal"
				voc = "o"
				esp = 0 


			elif (current_letter == "ú"):
				phone=  "U"
				quality = "vocal"
				voc = "uu"
			
			#resto de letras
			elif (current_letter == "b"):
				if (quality == "vocal" or quality in liquids):
					if (next_letter in vowels + liquids):
						phone="β" 
					else:
						phone=  "b"
				else:
					phone=  "b"
				quality = "b"

			elif (current_letter == "c") :
				if ( next_letter == "h" ) :
					phone="tʃ"
					skip = True
					quality = "tS" 
				elif ( next_letter in ['e', 'i', 'í']) :
					phone="θ"
					quality ="Z" 
				else :
					phone=  "k"
					quality = "k" 
						

			elif (current_letter == "d") :
				if (quality == "vocal" or quality == "r"):
					if (next_letter in vowels + liquids):
						phone=  "ð"
					else :
						phone=  "d" 
				else:
					phone=  "d"
				quality= "d"
				

			elif (current_letter == "e") :
				phone=  "e"
				quality = "vocal"
				voc = "e"
				esp = 0 


			elif (current_letter == "f") :
				phone=  "f"
				quality = 'f' 

			elif (current_letter == "g") :
				if (next_letter in ['a', 'o', 'w'] ):
					if (quality == "vocal" or quality == "s" or quality == "r" or quality == "l") :
						phone=  "ɣ"
					else :
						phone=  "g" 
				elif (next_letter in ['e', 'i']) :
					phone=  "x"
				elif (next_letter == 'u') :
					if ( next_letter2 in ['e','i']) :
						skip = True
						if (quality == "vocal" or quality == "s" or quality == "r" or	quality == "l") :
							phone="ɣ" 
						else :
							phone=  "g" 
					else :
						if (quality == "vocal"or quality == "s" or quality == "r" or	quality == "l") :
							phone="ɣ" 
						else :
							phone=  "g"
				elif (next_letter in liquids) :
					if (quality == "vocal"):
						phone="ɣ"
						quality == "G"
					else :
						phone=  "g"
						quality == "g"
				else :
					phone=  "g" 
					quality = "g"
				
			elif (current_letter == "h") :
					phone = ''

				# ATENCION ACA
			elif (current_letter == "i") :
				if ( (quality == "vocal" or next_letter in vowels) and prev_letter != ''  ) :
					#unless (prev_letter=~/ /) :
					phone=  "j"
					quality = "vocal"
					voc = "ï"
				else :
					phone=  "i"
					quality = "vocal"
					voc = "i"
					
				if (prev_letter=='') :
					phone= "i"
					esp = 0
					
			elif (current_letter == "j") :
				phone=  "x"
				quality = 'x'

			elif (current_letter == "k") :
				phone=  "k"
				quality = "k"
				
			elif (current_letter == "l") :
				if (next_letter == "l" and next_letter2 != "l" and esps != 1) :
					if (quality == "vocal"):
						phone=  "ʎ"
					elif (quality != "vocal"):
						phone=  "ʎ"
					skip = True # equivalent to n++
				elif (next_letter == "l" and next_letter2 != "l" and esps == 1) :
					phone=  "l l"
					n = n+2
					esps = 0
				elif (next_letter == "l" and next_letter2 == "l" and esps == 1) :
					phone=  "ʎ ʎ"
					n = n+3
					esps = 0
						

				else :
					phone=  "l"
					quality = "l"
					esp = 0
				
				quality = "l"

				

			elif (current_letter == "m") :
				if (next_letter == "f") :
					phone=  "M" 
				else :
					phone=  "m"
						
				quality = "m"
				
			elif (current_letter == "n") :
				if (next_letter in ['t','d','z']):
					phone=  "N" 

				elif ((next_letter in ['c', 'q']) and (next_letter2 in ['a', 'o', 'u'])) :
					phone="ŋ" 

				elif (next_letter in ['b','v','p','m']):
					phone=  "m" 

				elif (next_letter in ['g', 'j']):
					phone="ŋ"

				elif (next_letter == "f"):
					phone=  "M"

				elif ((next_letter == "c") and (next_letter2 in ["e","i"])) :
					phone=  "N" 

				elif ( ((next_letter == "y") and (next_letter2 in ['a','e','i','o','u'])) or (next_letter == "l" and next_letter2 == "l") ) :
					phone=  "ɲ" 
				else :
					phone=  "n"
				
				quality = "n"

			elif (current_letter == "ñ") :
				phone=  "ɲ"
				quality ="ñ"
				
			elif (current_letter == "o") :
				phone=  "o"
				quality = "vocal"
				voc = "o"
				esp = 0

			elif (current_letter == "p") :
				phone=  "p"
				quality = "p"
				
			elif (current_letter == "q") :
				phone=  "k"
				skip = True
				quality = "q"
				

			elif (current_letter == "r") :
				if (quality in ['t', 'd', 'p', 'b', 'k', 'g', 'f']) :
					phone="r"
					quality = "r"
				elif (next_letter == "r") :
					phone = 'R'
					skip = True
					quality = "r"
				elif (next_letter != "r" and quality == "r" and esp != 1) :
					phone="R"
					quality = "R"
				elif (quality == "vocal" and next_letter != "r" and esp != 1) :
					phone=  "r"
					quality = "r"
				elif (quality != "vocal" and esp == 0) :
					phone=  "R"
					quality = "r"
				elif (esp == 1 and quality != "R") :
					phone=  "R"
					quality = "R"
				elif (esp == 1 and quality == "R") :
					phone=  "r"
					quality ="R"
					esp= 0
				else:
					phone=  "*"

			elif (current_letter == "s") :
				if (next_letter in ['b', 'v', 'd', 'l', 'm', 'n'] or (next_letter == "g" and (next_letter2 not in ["e", 'i'])) ) :
					phone=  "z"
					quality = "vocal"
				else :
					phone=  "s"
					quality = "s" 
			
			elif (current_letter == "t") :
				phone=  "t"
				quality = "t"
			

			elif (current_letter == "u") :
				if (quality == "vocal" and voc != "ï"):
					phone=  "w"
					quality = "vocal"
					voc = "w"
			   
				elif (next_letter in ['a', 'e', 'o', 'u', 'á', 'é', 'ó']) :
					phone=  "w"

				else :
					phone=  "u"
					quality = "vocal"
					voc = "u"
					esp = 0
			

			elif (current_letter == "v"):
				if (quality == "vocal" or quality == "l" or quality == "r") :
					if (next_letter in vowels+liquids):
						phone="β"
						quality ="B"
					else:
						phone=  "b"
				else:
					phone=  "b"
				quality = "b"

			elif (current_letter == "w") :
				phone=  "w"
				quality = "w"
			
			elif (current_letter == "x") :
				phone=  "ks"
				quality = "x" 

			elif (current_letter == "y") :
				if (next_letter in vowels and esps == 0) :
					phone= "y"
					quality= "vocal"
					voc="ï"
				elif (quality == "vocal" or esps == 1) :
					if ((quality == "vocal")):
						phone=  "i"  ##aproximante
						quality = "vocal"
						voc = "ï"
					else :
						phone=  "i"
						quality = "vocal"
						voc = "i"
				else :
					phone=  "y"
					esps = 0

			elif (current_letter == "z") :
				phone="θ"
				quality = "Z" 
					
			if (quality != "vocal"):
				voc = 0
			transcription = transcription + phone
		else:
			skip = False

	return transcription

#print(first_order_transcription(word))