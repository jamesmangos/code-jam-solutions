input_file = open('C-large-practice.in', 'r')
output_file = open('out.txt', 'w')
line = {}
number_message = {}
message = ""

#input
N = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()


#process
for i in range(N):
    number_message[i] = ""
    #this part is for the first element only since the rest of the code checks the previous element which creates an out of bounds error
    if line[i][0] == "a":
        number_message[i] = number_message[i] + "2"
    elif line[i][0] == "b":
        number_message[i] = number_message[i] + "22"
    elif line[i][0] == "c":
        number_message[i] = number_message[i] + "222"
        ################################    
    elif line[i][0] == "d":
        number_message[i] = number_message[i] + "3"
    elif line[i][0] == "e":
            number_message[i] = number_message[i] + "33"
    elif line[i][0] == "f":
        number_message[i] = number_message[i] + "333"
        ##################################    
    elif line[i][0] == "g":
        number_message[i] = number_message[i] + "4"
    elif line[i][0] == "h":
        number_message[i] = number_message[i] + "44"
    elif line[i][0] == "i":
        number_message[i] = number_message[i] + "444"
        ##################################
    elif line[i][0] == "j":
        number_message[i] = number_message[i] + "5"
    elif line[i][0] == "k":
        number_message[i] = number_message[i] + "55"
    elif line[i][0] == "l":
        number_message[i] = number_message[i] + "555"
    #########################################
    elif line[i][0] == "m":
        number_message[i] = number_message[i] + "6"
    elif line[i][0] == "n":
        number_message[i] = number_message[i] + "66"
    elif line[i][0] == "o":
        number_message[i] = number_message[i] + "666"
    ##########################################
    elif line[i][0] == "p":
        number_message[i] = number_message[i] + "7"
    elif line[i][0] == "q":
        number_message[i] = number_message[i] + "77"
    elif line[i][0] == "r":
        number_message[i] = number_message[i] + "777"
    elif line[i][0] == "s":
        number_message[i] = number_message[i] + "7777"
    #########################################
    elif line[i][0] == "t":
        number_message[i] = number_message[i] + "8"
    elif line[i][0] == "u":
        number_message[i] = number_message[i] + "88"
    elif line[i][0] == "v":
        number_message[i] = number_message[i] + "888"
    ##########################################
    elif line[i][0] == "w":
        number_message[i] = number_message[i] + "9"
    elif line[i][0] == "x":
        number_message[i] = number_message[i] + "99"
    elif line[i][0] == "y":
        number_message[i] = number_message[i] + "999"
    elif line[i][0] == "z":
        number_message[i] = number_message[i] + "9999"
    elif line[i][0] == " ":
        number_message[i] = number_message[i] + "0"

    
    for j in range(1,len(line[i])):
        ##############################
        if line[i][j] == "a":
            if line[i][j-1] == "a" or line[i][j-1] == "b" or line[i][j-1] == "c":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "2"
        elif line[i][j] == "b":
            if line[i][j-1] == "a" or line[i][j-1] == "b" or line[i][j-1] == "c":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "22"
        elif line[i][j] == "c":
            if line[i][j-1] == "a" or line[i][j-1] == "b" or line[i][j-1] == "c":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "222"
        ################################    
        elif line[i][j] == "d":
            if line[i][j-1] == "d" or line[i][j-1] == "e" or line[i][j-1] == "f":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "3"
        elif line[i][j] == "e":
            if line[i][j-1] == "d" or line[i][j-1] == "e" or line[i][j-1] == "f":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "33"
        elif line[i][j] == "f":
            if line[i][j-1] == "d" or line[i][j-1] == "e" or line[i][j-1] == "f":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "333"
        ##################################    
        elif line[i][j] == "g":
            if line[i][j-1] == "g" or line[i][j-1] == "h" or line[i][j-1] == "i":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "4"
        elif line[i][j] == "h":
            if line[i][j-1] == "g" or line[i][j-1] == "h" or line[i][j-1] == "i":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "44"
        elif line[i][j] == "i":
            if line[i][j-1] == "g" or line[i][j-1] == "h" or line[i][j-1] == "i":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "444"
        ##################################
        elif line[i][j] == "j":
            if line[i][j-1] == "j" or line[i][j-1] == "k" or line[i][j-1] == "l":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "5"
        elif line[i][j] == "k":
            if line[i][j-1] == "j" or line[i][j-1] == "k" or line[i][j-1] == "l":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "55"
        elif line[i][j] == "l":
            if line[i][j-1] == "j" or line[i][j-1] == "k" or line[i][j-1] == "l":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "555"
        #########################################
        elif line[i][j] == "m":
            if line[i][j-1] == "m" or line[i][j-1] == "n" or line[i][j-1] == "o":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "6"
        elif line[i][j] == "n":
            if line[i][j-1] == "m" or line[i][j-1] == "n" or line[i][j-1] == "o":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "66"
        elif line[i][j] == "o":
            if line[i][j-1] == "m" or line[i][j-1] == "n" or line[i][j-1] == "o":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "666"
        ##########################################
        elif line[i][j] == "p":
            if line[i][j-1] == "p" or line[i][j-1] == "q" or line[i][j-1] == "r" or line[i][j-1] == "s":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "7"
        elif line[i][j] == "q":
            if line[i][j-1] == "p" or line[i][j-1] == "q" or line[i][j-1] == "r" or line[i][j-1] == "s":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "77"
        elif line[i][j] == "r":
            if line[i][j-1] == "p" or line[i][j-1] == "q" or line[i][j-1] == "r" or line[i][j-1] == "s":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "777"
        elif line[i][j] == "s":
            if line[i][j-1] == "p" or line[i][j-1] == "q" or line[i][j-1] == "r" or line[i][j-1] == "s":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "7777"
        #########################################
        elif line[i][j] == "t":
            if line[i][j-1] == "t" or line[i][j-1] == "u" or line[i][j-1] == "v":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "8"
        elif line[i][j] == "u":
            if line[i][j-1] == "t" or line[i][j-1] == "u" or line[i][j-1] == "v":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "88"
        elif line[i][j] == "v":
            if line[i][j-1] == "t" or line[i][j-1] == "u" or line[i][j-1] == "v":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "888"
        ##########################################
        elif line[i][j] == "w":
            if line[i][j-1] == "w" or line[i][j-1] == "x" or line[i][j-1] == "y" or line[i][j-1] == "z":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "9"
        elif line[i][j] == "x":
            if line[i][j-1] == "w" or line[i][j-1] == "x" or line[i][j-1] == "y" or line[i][j-1] == "z":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "99"
        elif line[i][j] == "y":
            if line[i][j-1] == "w" or line[i][j-1] == "x" or line[i][j-1] == "y" or line[i][j-1] == "z":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "999"
        elif line[i][j] == "z":
            if line[i][j-1] == "w" or line[i][j-1] == "x" or line[i][j-1] == "y" or line[i][j-1] == "z":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "9999"
        ###########################################
        elif line[i][j] == " ":
            if line[i][j-1] == " ":
                number_message[i] = number_message[i] + " "
            number_message[i] = number_message[i] + "0"
            
for i in range(len(line)):
    message = message + "case #" + str(i+1) + ": " + str(number_message[i]) + "\n"
output_file.write(message)

output_file.close()
