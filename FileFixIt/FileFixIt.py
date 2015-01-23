#input_file = open('ExampleInput.txt', 'r')
#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
output_file = open('out.txt', 'w')
line = {}
num_commands = {}
N = {} #number of existing
M = {} #number of desired
desired_directories = {}
existing_directories = {}

#file input
T = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#put input into data structure
case = 0
line_index = 0
while line_index < len(line):
    line[line_index] = line[line_index].split() #split the line containing M and B at the space
    N[case] = int(line[line_index][0]) #number of existing
    M[case] = int(line[line_index][1]) #number of desired
    line_index = line_index + 1
    existing_directories[case] = {}
    desired_directories[case] = {}
    for j in range(N[case]):
        existing_directories[case][j] = line[line_index].rstrip('\n') #set each of the existing directories, removing the new line characters
        line_index = line_index + 1
    for j in range(M[case]):
        desired_directories[case][j] = line[line_index].rstrip('\n')
        line_index = line_index + 1
    case = case + 1
    
#process
#for each desired directory, split it at '/' and add each component in sequence, comparing this composition with each entry in the existing directories
#and the desired directories that have already had directories created
    
for case in range(T): #for all cases
    num_commands[case] = 0
    for i in range(M[case]):#for each of the desired directories repeat this process
        composition = "" #set the composition to nothing since this is the start of the next desired directory
        desired_directories[case][i] = desired_directories[case][i].split("/") #split the desired directory at each '/' i.e. at each level of the heirarchy
        for j in range(1, len(desired_directories[case][i])): #for each level in the desired directories' hierarchy
            matches = "false" #reset the matches boolean each time a new level is added
            composition = composition + "/" + str(desired_directories[case][i][j]) #add the next component to the composition string
            for k in range(len(existing_directories[case])): #for each of the existing directories, check if the composition folder already exists
                if composition == existing_directories[case][k]: #if the composition matches the existing directory i.e. the directory already exists
                    matches = "true"
            for k in range(0, i): #for each of the desired directories already created  # i, not i-1 since range() is not end inclusive
                if desired_directories[case][k].startswith(composition + '/') or desired_directories[case][k] == composition:#if the desired directory already exists
                    matches = "true"
            if matches == "false":
                num_commands[case] = num_commands[case] + 1 #add a new command if the composition folder does not already exist
        desired_directories[case][i] = composition #put string back together so that it is a string, not a list, for comparison

#output
output = ""
for i in range(T):
    output = output + "case #" + str(i+1) + ": " + str(num_commands[i]) + "\n"
output_file.write(output)

output_file.close()
