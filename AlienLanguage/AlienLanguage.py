#https://code.google.com/codejam/contest/90101/dashboard#s=p0
import re
#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
output_file = open('out.txt', 'w')

#input
j = 0
line = {}#dictionary
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

line[0] = line[0].split()
num_words = int(line[0][1])
N = int(line[0][2])#number of test cases

#put dictionary words into a new array(dictionary)
word = {}#dictionary
for i in range(1,num_words+1):
    word[i-1] = line[i]

#for each case determine the number of possible combinations
possibilities = {}
k = 0
for i in range(num_words+1, num_words+1+N):
    possibilities[k] = 0

    #replace brackets with braces for python regex
    line[i] = line[i].replace('(','[')
    line[i] = line[i].replace(')',']')

    #for each dictionary entry test patter
    for j in range(len(word)):
        #if match then increment
        match = re.search(line[i], word[j])
        if match:
            possibilities[k] = possibilities[k] + 1
    k = k+1

output = ""
for i in range(N):
    output = output + "case #" + str(i+1) + ": " + str(possibilities[i]) + "\n"
output_file.write(output)
output_file.close()