line = {}

#input
N = int(input())
for i in range(N):
    line[i] = input()

for i in range(N):
    print("case #" + str(i+1) + ": ", end = "") #second arguement: don't add a newline, add nothing at the end of these wordst
    line[i] = line[i].split() #split the line at spaces
    for j in range(len(line[i])-1, -1, -1): #in reverse order, print each word
        print(line[i][j], end = " ")#second arguement means that rather than a new line at the end of each word there is instead a space
    print() #start a new line after each case
