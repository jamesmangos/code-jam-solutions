#input_file = open('ExampleInput.txt', 'r')
input_file = open('B-small-practice.in', 'r')
#input_file = open('B-large-practice.in', 'r')
output_file = open('out.txt', 'w')
line = {}
N = {}
K = {}
B = {}
T ={}
X ={}
V = {}
output = ""

#file input
C = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#sort input
i = 0
for case in range(C):
	X[case] = {}
	V[case] = {}
	line[i] = line[i].split() #split the N K B T line at spaces
	N[case] = int(line[i][0])
	K[case] = int(line[i][1])
	B[case] = int(line[i][2])
	T[case] = int(line[i][3])
	i = i + 1
	line[i] = line[i].split() #split the X line at spaces
	for j in range(N[case]):
		X[case][j] = int(line[i][j]) #add the initial positions to an array
	i = i + 1	
	line[i] = line[i].split() #split the V line at spaces
	for j in range(N[case]):
		V[case][j] = int(line[i][j]) #add the veolicities to the array
	i = i + 1

#processing
for case in range(C): #for each case
	num_swaps = 0
	price_of_swap = 0
	num_chicks = 0 #set the number of chicks that have made it to 0
	chick_list = [] #list
	for i in range(N[case]): #for each chicken
		if (B[case]-X[case][i])/V[case][i] <= T[case]:#chech if the time fo rthe chicken to reach the barn is less than or eaual to the avalible time
			chick_list.append(i) #add the index of the chicken that will make it
	if len(chick_list) >= K[case]:
		for i in range(N[case]-1,-1,-1): #for each chicken; going backwards through the array
			if i in chick_list: #if chicken i finishes
				num_chicks = num_chicks + 1 #increment the number of chickens that have finished
				num_swaps = num_swaps + price_of_swap #increase the number of swaps by the number of non-finishing chickens in front of the current one, the current chicken will not need to swap with a finisher since they will both finish regardles
			else:
				price_of_swap = price_of_swap + 1 #if the chicken is not in the list then it will be overtaken by any chicken that starts before it hence each subsequent chicken will need to be swapped one more time
			if num_chicks == K[case]: #once the minimum number of chickens have made it end the loop that increases the number of swaps
				break
		output = output + "case #" + str(case+1) + ": " + str(num_swaps) + "\n"
	else: # if impossible
		output = output + "case #" + str(case+1) + ": " + "IMPOSSIBLE\n"

output_file.write(output)
output_file.close()