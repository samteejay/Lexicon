lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun'
}


def scan(sentence):
    words = sentence.split()
    result = []
	
    for word in words:
        lowered_case = word.lower()
		
        if lowered_case in lexicon:
            
            pair = (lexicon[lowered_case], lowered_case)
            result.append(pair)
		
        elif lowered_case.isdigit():
            number = convert_number(lowered_case)
            
            pair = ('number', number)
            result.append(pair)
	    
        else:
            error_word = word
            pair = ('error', error_word)
            result.append(pair)
			
			
    return result
			
			
	
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return none

