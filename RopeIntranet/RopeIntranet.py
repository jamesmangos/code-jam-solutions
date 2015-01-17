#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
#input_file = open('ExampleInput.txt', 'r')
output_file = open('out.txt', 'w')
line = {}
num_wires = 0
wire_pair = {}
intersections = {}

#file input
N = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#to determine if each pair of wires intersect, test if A0 < A1 and B0 > B1 or other way around
#in other words the endpoints of one wire must be on opposite sides of the other wire

#put input into data structure
case = 0
line_index = 0
while line_index < len(line):
    num_wires = int(line[line_index]) #store the next line as an integer
    line_index = line_index + 1 #increment the line index so we look at the next line
    for i in range(num_wires): #for the next num_wires lines, read each line as wire endpoints
        wire_pair[i] = line[line_index]
        line_index = line_index + 1
        wire_pair[i] = wire_pair[i].split() #split the wire_pair at spaces
        for l in range(len(wire_pair[i])):
            wire_pair[i][l] = int(wire_pair[i][l]) #turn the two wire endpoints from strings into integers

    #find ouptut
    intersections[case] = 0
    for j in range(num_wires):#for each wire in the case
        for k in range(j+1,num_wires):#for each pair of wires
            if wire_pair[j][0] > wire_pair[k][0]: # if A1 is more than A2
                if wire_pair[j][1] < wire_pair[k][1]: #if nodes are on opposite sides of the wire then they cross
                    intersections[case] = intersections[case] + 1
            elif wire_pair[j][0] < wire_pair[k][0]: #if A2 is less than A2
                if wire_pair[j][1] > wire_pair[k][1]: #if nodes are on opposite sides of the wire then they cross
                    intersections[case] = intersections[case] + 1
    num_wires = []#reset the array/list to null values
    case = case + 1

#output
output = ""
for i in range(N):
    output = output + "case #" + str(i+1) + ": " + str(intersections[i]) + "\n"
output_file.write(output)

output_file.close()
