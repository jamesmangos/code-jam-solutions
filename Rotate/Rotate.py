#input_file = open('ExampleInput.txt', 'r')
#input_file = open('A-small-practice.in', 'r')
input_file = open('A-large-practice.in', 'r')
output_file = open('out.txt', 'w')
line = {}
output = ""

def player_has_won(token, number, x, y , x_offset, y_offset):
	global rotated_board
	in_a_row = 0
	try:
		while "true": 
			if rotated_board[y][x] == token: #if the next element matches the symbol then increment the number of tokens in a row
				in_a_row = in_a_row + 1
				if in_a_row >= number: #check if the number of tokens in a row is the minimum number
					return "true"
				x = x + x_offset #change the x and y values so that the board is traversed in the desired direction, up, down, left, right or diagonally
				y = y + y_offset
			else:
				return ""
			if x < 0 or y < 0:
				raise IndexError
	except IndexError: #in case of out of bounds error return false since there cannot possibly be enough in a row
		return ""

#file input
T = int(input_file.readline())
j = 0
for i in input_file:
    line[j] = i
    j = j + 1
input_file.close()

#sort input and process
case = 0
line_index = 0
while line_index < len(line):
	winner = "Neither"
	line[line_index] = line[line_index].split()
	N = int(line[line_index][0])
	K = int(line[line_index][1])
	line_index = line_index + 1
	board = [[ '' for y in range(N)] for x in range(N)] #create board
	for y in range(N-1,-1,-1): #for each line of the board from top to bottom
		line[line_index] = list(line[line_index]) #split into an array of characters
		board[y] = line[line_index] #and set that array of characters as a row on the board
		line_index = line_index + 1

	####    rotate the board   #####
	rotated_board = [[ '.' for y in range(N)] for x in range(N)] #create a rotated board
	for x in range(N): #rotate the board clockwise
		for y in range(N):
			rotated_board[y][x] = board[x][N-y-1]  #clockwise, if board[x][y] then flips along y=x axis, if board[N-x-1][y] flips counter clockwise

	####   account for gravity   ######
	for x in range(N): # for each collumn
		offset = 0 #set the number of offsets to 0 for each collumn
		for y in range(N): #going up the collumn
			if rotated_board[y][x] == ".": #if this is an empty slot then increase the offset so that future tokens will fall down the right amount
				offset = offset + 1
			if rotated_board[y][x] != "." and offset > 0: #if offsetting then move this token down several places and set the current element to empty
				rotated_board[y-offset][x] = rotated_board[y][x]
				rotated_board[y][x] = "."

	####  check if anyone has won  ###### 
	token = "R" #first check if red has won
	for x in range(N):#for each element on the board check if the player has won in any direction
		for y in range(N):#each of the conditions below mean right, down, left, right, up, up and right, down and right, down and left, up and left
			if player_has_won(token,K,x,y,1,0) or player_has_won(token,K,x,y,0,-1) or player_has_won(token,K,x,y,-1,0) or player_has_won(token,K,x,y,0,1) or player_has_won(token,K,x,y,1,1) or player_has_won(token,K,x,y,1,-1) or player_has_won(token,K,x,y,-1,-1) or player_has_won(token,K,x,y,-1,1):
				winner = "Red"
				break
		else: #these three lines mean that both loops will be broken out of if the break statement is used
			continue
		break
	token = "B" #now check if blue has won
	for x in range(N): #for each element on the board check if the player has won in any direction
		for y in range(N): #each of the conditions below mean right, down, left, right, up, up and right, down and right, down and left, up and left
			if player_has_won(token,K,x,y,1,0) or player_has_won(token,K,x,y,0,-1) or player_has_won(token,K,x,y,-1,0) or player_has_won(token,K,x,y,0,1) or player_has_won(token,K,x,y,1,1) or player_has_won(token,K,x,y,1,-1) or player_has_won(token,K,x,y,-1,-1) or player_has_won(token,K,x,y,-1,1):
				if winner == "Neither":
					winner = "Blue"
				elif winner == "Red":
					winner = "Both"
				break
		else: #these three lines mean that both loops will be broken out of if the break statement is used
			continue
		break

	output = output + "case #" + str(case+1) + ": " + str(winner) + "\n"
	case = case + 1

#write output
output_file.write(output)
output_file.close()