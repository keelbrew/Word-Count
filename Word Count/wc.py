text = open("wc.txt", "r") 
dictionary = dict() 
for lines in text: 
	lines = lines.strip() 
	lines = lines.lower()      
	words = lines.split(" ") 
	for word in words: 		
		if word in dictionary: 		
			dictionary[word] = dictionary[word] + 1
		else: 			 
			dictionary[word] = 1
for key in list(dictionary.keys()): 
	print(key.rjust(20), ":", dictionary[key]) 
