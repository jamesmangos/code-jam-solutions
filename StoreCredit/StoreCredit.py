#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
#input_file = open('ExampleInput.txt', 'r')
output_file = open('out.txt', 'w')
line = {}
credit = {}
items = {}
price = {}
output = {}


#input
N = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#seperate inputs
case = 0
for i in range(len(line)):
    if i % 3 == 0: #if the remeinder of i divided by 3 is 0 (i.e. i is divisible by 3)
        credit[case] = int(line[i])
    elif i % 3 == 1: #if the remeinder of i divided by 3 is 1
        items[case] = line[i]
    elif i % 3 == 2: #if the remeinder of i divided by 3 is 2
        price[case] = line[i]
        case = case + 1 #every third line, increment the case
    

#process
for case in range(N): #for each case
    output[case] = ""
    price[case] = price[case].split() #split the price of the items at spaces
    for j in range(len(price[i])): #for each item
        for k in range(j+1, len(price[case])):# j+1 avoids repeating combinations. Otherwise each combination would be checked twice
            if int(price[case][j]) + int(price[case][k]) == credit[case]:
                output[case] = str(j+1) + " " + str(k+1) #if this combination is the correct one

#output
message = ""
for i in range(N):
    message = message + "case #" + str(i+1) + ": " + str(output[i]) + "\n"
output_file.write(message)

output_file.close()
