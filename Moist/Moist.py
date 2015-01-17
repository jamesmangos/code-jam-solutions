#input_file = open('A-small-practice-1.in', 'r')
input_file = open('A-small-practice-2.in', 'r')
#input_file = open('ExampleInput.txt', 'r')
output_file = open('out.txt', 'w')
line = {}
cost = {}
card = {}
T = {}

#input
N = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#sort the input
case = 0
i = 0
while i < len(line):
    T[case] = line[i]
    i = i + 1
    card[j] = ""
    for k in range(int(T[case])):
        card[case] = card[case] + line[i]
        i = i + 1
    card[case] = card[case].rstrip('\n') #remove the last newline character
    card[case] = card[case].split('\n') #split the string at newline caracters
    case = case + 1

#process
for case in range(N): #for each case
    #insetion sort
    cost[case] = 0
    for index in range(1, len(card[case])):
        if card[case][index] < card[case][index-1]:
            current_value = card[case][index]
            position = index
            while  position > 0 and card[case][position-1] > current_value:
                card[case][position] = card[case][position-1]
                position = position - 1
            card[case][position] = current_value
            cost[case] = cost[case] + 1

#output
message = ""
for i in range(N):
    message = message + "case #" + str(i+1) + ": " + str(cost[i]) + "\n"
output_file.write(message)

output_file.close()
