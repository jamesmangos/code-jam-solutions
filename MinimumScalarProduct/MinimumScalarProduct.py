#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
output_file = open('out.txt', 'w')
from itertools import *
import operator
output = ""

T = int(input_file.readline())
for case in range(T):
	n = int(input_file.readline())
	vector1 = input_file.readline()
	vector1 = vector1.split() 
	vector2 = input_file.readline()
	vector2 = vector2.split()
	for i in range(n): 				#convert elements of vector1 and vector2 into integers
		vector1[i] = int(vector1[i])
		vector2[i] = int(vector2[i])
	vector1.sort()					#sorts vector1 so it is ascending
	vector2.sort(reverse=True)		#sorts vector2 so it is descending

	output = output + "case #" + str(case+1) + ": " + str(sum(map(operator.mul, vector1, vector2))) + "\n"

input_file.close()
output_file.write(output)
output_file.close()
