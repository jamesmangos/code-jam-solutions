line = {}
base_source = {}
base_target = {}

def to_decimal(number): #converts source language number to a decimal number
    decimal_value = 0
    for j in range(len(number)): #for each digit in given number
        for k in range(base_source[i]): # check which source digit the alien digit corrosponds to
            if number[j] == line[i][1][k]: #if the digit matches the source digit
                decimal_value = decimal_value + k * pow(base_source[i], len(n) - 1 - j) #add the value (remembering its place value) to the total value
                break #once the corrosponding digit has been found, there is no need to continue searching for the matching digit
    return decimal_value

def to_target(number):  #converts decimal number to target language number
    translated_number = ""
    has_non_zero = "" #this is effectivly a value of false
    for power in range(1000, -1, -1): #go through each place value in the translated number  #1000 is an arbitary high number
        if pow(base_target[i],power) <= number: #if the decimal number is more than the base^power then this is a non-zero element
            for l in range(base_target[i]-1,0,-1): #for each symbol in the target language (except the zero), decending
                if l*pow(base_target[i],power) <= number: #the highest number that goes into the decimal value will be appended to the translated number
                    translated_number = translated_number + str(line[i][2][l]) #append the relevent symbol
                    number = number - l*pow(base_target[i], power) #subtract the corrosponding decimal value from the decimal value
                    has_non_zero = "true"
                    break #break to avoid subtracting zero. If this was not here a zero-equivalent symbol would appear
        else: #zero-element
            if has_non_zero: #add this if statement to avoid leading zeroes. zero-equivalent symbols will not apear until there has been a non-zero symbol
                translated_number = translated_number + str(line[i][2][0]) #append the zero-equivalent symbol since this place value should have zero
    return translated_number
            
#input
N = int(input(""))
for i in range(N):
    line[i] = input("")

#process
for i in range(N):
    line[i] = line[i].split() #split the line at spaces
    base_source[i] = len(line[i][1])
    base_target[i] = len(line[i][2])
    print("case #" + str(i+1) + ": " + str(to_target(to_decimal(line[i][0]))))
