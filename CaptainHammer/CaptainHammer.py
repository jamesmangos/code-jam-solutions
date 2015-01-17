input_file = open('B-small-practice.in', 'r')
#input_file = open('ExampleInput.txt', 'r')
output_file = open('out.txt', 'w')
line = {}
theta = {}
import math

#input
N = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    line[j] = line[j].split()
    j = j + 1
input_file.close()


#process
#given velocity and distance, g = 9.8 ms^-2, what is theta?
for i in range(N):
    try:
        #rearranging the range formula
        theta[i] = math.asin(9.8*int(line[i][1])/math.pow(int(line[i][0]),2))/2* 180/math.pi
    except ValueError:
        #due to the way computers store numbers, any input that should equate to asin(1) becomes asin(1.000...2) so the exception is caught and rounded to 1
        print("exception occured at case " + str(i+1))
        theta[i] = math.asin(1)/2 * 180/math.pi

#output
output = ""
for i in range(N):
    output = output + "case #" + str(i+1) + ": " + str(theta[i]) + "\n"
output_file.write(output)

output_file.close()
