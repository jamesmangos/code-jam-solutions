#https://code.google.com/codejam/contest/189252/dashboard#s=p0
#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
output_file = open('out.txt', 'w')
output = ""

case = 0
T = int(input_file.readline())
for line in input_file:
	unique_symbols = [] #empty list
	line = line.rstrip('\n') #remove the end line character

	#find number of unique symbols, this will yield the minimum base
	for i in range(len(line)):
		if line[i] not in unique_symbols:
			unique_symbols = unique_symbols + list(line[i])
	base = len(unique_symbols) #store the minimum base of the number system
	if base == 1:
		base = 2 #if there is only 1 unique symbol then it is a base two system since the aliens do not use unary

	#find minimum_seconds
	if len(line) == 1:
		minimum_seconds = 1
	else: 
		minimum_seconds = pow(base, len(line)-1)
		if len(unique_symbols) == 1: #if there is only one unique symbol then there is no need to search for another unique symbol
			unique_symbols = ['++++', line[0]] #set the 1-equivalent character as the 1th element of the list
		else:
			unique_symbols = ['++++', line[0]] #set the 1-equivalent character as the 1th element of the list
			j = 1
			while j < len(line)-1 and line[j] == line[j-1]: #go to the first case of the second unique symbol
				j = j + 1
			unique_symbols[0] = line[j]#set the second unique symbol as the zero-equivalnt character
		for i in range(1, len(line)): #for the rest of the characters
			if line[i] not in unique_symbols:
				unique_symbols = unique_symbols + list(line[i])
			minimum_seconds = minimum_seconds + unique_symbols.index(line[i]) * pow(base, len(line)-1-i)

	output = output + "case #" + str(case+1) + ": " + str(minimum_seconds) + "\n"
	case = case + 1

input_file.close()
output_file.write(output)
output_file.close()