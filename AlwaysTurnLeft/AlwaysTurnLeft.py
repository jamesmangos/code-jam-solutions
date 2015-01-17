line = {}

class Maze:
    description = "0"
    north = "1" #the following four lines set each direction to true initially for each element in the maze
    south = "1"
    east = "1"
    west = "1"

def turn_around():
    global cardinal_direction
    if cardinal_direction == "north":
        cardinal_direction = cardinal_direction.replace("north","south")
    elif cardinal_direction == "south":
        cardinal_direction = cardinal_direction.replace("south","north")
    elif cardinal_direction == "east":
        cardinal_direction = cardinal_direction.replace("east","west")
    elif cardinal_direction == "west":
        cardinal_direction = cardinal_direction.replace("west","east")

def turn_left():
    global cardinal_direction
    if cardinal_direction == "north":
        cardinal_direction = cardinal_direction.replace("north","west")
    elif cardinal_direction == "south":
        cardinal_direction = cardinal_direction.replace("south","east")
    elif cardinal_direction == "east":
        cardinal_direction = cardinal_direction.replace("east","north")
    elif cardinal_direction == "west":
        cardinal_direction = cardinal_direction.replace("west","south")
        
def turn_right():
    global cardinal_direction
    if cardinal_direction == "north":
        cardinal_direction = cardinal_direction.replace("north","east")
    elif cardinal_direction == "south":
        cardinal_direction = cardinal_direction.replace("south","west")
    elif cardinal_direction == "east":
        cardinal_direction = cardinal_direction.replace("east","south")
    elif cardinal_direction == "west":
        cardinal_direction = cardinal_direction.replace("west","north")
        
def move_forward():
    global current_y
    global current_x
    global max_y
    global max_x
    global min_x
    global min_y
    if cardinal_direction == "north":
        current_y = current_y + 1
        if current_y > max_y:
            max_y = current_y
    elif cardinal_direction == "south":
        current_y = current_y - 1
        if current_y < min_y:
            min_y = current_y
    elif cardinal_direction == "east":
        current_x = current_x + 1
        if current_x > max_x:
            max_x = current_x
    elif cardinal_direction == "west":
        current_x = current_x - 1
        if current_x < min_x:
            min_x = current_x

def dead_end(): #exit to the right
    if cardinal_direction == "north": #only east
        maze[current_x][current_y].description = "8"
    elif cardinal_direction == "south": #only west
        maze[current_x][current_y].description = "4"
    elif cardinal_direction == "east": #only south
        maze[current_x][current_y].description = "2"
    elif cardinal_direction == "west": #only north
        maze[current_x][current_y].description = "1"

def turn_right_description(): #exit on the right of the direction faced
    if cardinal_direction == "north": #only south and east
        maze[current_x][current_y].description = "a"
    elif cardinal_direction == "south": #only north and west
        maze[current_x][current_y].description = "5"
    elif cardinal_direction == "east": #only west and south
        maze[current_x][current_y].description = "6"
    elif cardinal_direction == "west": #only east and north
        maze[current_x][current_y].description = "9"

def cant_turn_left(): #left not possible
    if cardinal_direction == "north": 
        maze[current_x][current_y].west = "" #sets this value to effectivly false
    elif cardinal_direction == "south": 
        maze[current_x][current_y].east = ""
    elif cardinal_direction == "east": 
        maze[current_x][current_y].north = ""
    elif cardinal_direction == "west": 
        maze[current_x][current_y].south = ""

def update_maze_description():
    #add a first direction check for two forwards
    if len(line[i][0]) < 4 and len(line[i][1]) < 4: #two or three directions
        if line[i][0][1] == "W":
            maze[0][0].description = "3" #only north and south
        elif line[i][0][1] == "L":
            maze[0][0].description = "9" #only north and east
        elif line[i][0][1] == "R":
            maze[0][0].description = "5" #only north and west
    for j in range(columns):
        for k in range(rows):
            if maze[j][k].description == "0":
                if maze[j][k].north:
                    if maze[j][k].south:
                        if maze[j][k].east:
                            if maze[j][k].west:
                                maze[j][k].description = "f" #all directions
                            else:
                                maze[j][k].description = "b" #not west
                        else:
                            if maze[j][k].west:
                                maze[j][k].description = "7" #not east
                            else:
                                maze[j][k].description = "3" #north and south
                    else: #north, not south
                        maze[j][k].description = "d"
                else: #not north
                    if maze[j][k].south:
                        maze[j][k].description = "e"
                    elif maze[j][k].west and maze[j][k].east:
                        maze[j][k].description = "c" #east and west

def go_through_maze(directions, update_maze):
    #updating done before movement
    for i in range(1, len(directions)-1): #for each instruction in the directions except the first and last (first and last are outside the maze)
        if directions[i] == "W":
            if directions[i-1] == "W": # two 'W's and the last direction wasn't a turn
                if update_maze:
                    cant_turn_left() #left not possible on first box
            move_forward()
        elif directions[i] == "L":
            turn_left()
        elif directions[i] == "R":
            if directions[i-1] == "R": # two 'R's
                if update_maze:
                    dead_end() #dead end to the right
            else:
                if update_maze:
                    turn_right_description() #only entrance and exit are possible in this box
            turn_right()
    if directions[len(directions)-2] == "W" and update_maze:
        cant_turn_left()

def find_maze_size():
    global rows
    global columns
    rows = abs(max_y-min_y) + 1 #+1 needed for the fact that 0-0 will lead to 0, not 1
    columns = abs(max_x-min_x) + 1

#input
N = int(input(""))
for i in range(N):
    line[i] = input("")

#process
for i in range(N):
    #reset these value for each case
    current_x = 0
    current_y = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    
    line[i] = line[i].split()#split each line at spaces, thereby seperating the directions in opposite directions

    #go through the maze both ways, not updating the description but finding the dimensions of the maze
    cardinal_direction = "south"
    go_through_maze(line[i][0], "")
    turn_around()
    go_through_maze(line[i][1], "")
    find_maze_size()

    #update the position so that indicies will match up
    #at this point the x and y position will be at the entrance
    current_x = int(current_x + abs(min_x)) #adds the offset from 0, min_x < 0 always
    current_y = int(abs(min_y)) #adds the offset from 0, min_y < 0 always #current_y not needed since current_y will always be 0 (before offset)

    #create maze with correct dimensions
    maze = [[Maze() for y in range(rows)] for x in range(columns)]

    #go through the maze both ways, updating the maze decription as you go
    cardinal_direction = "south"
    go_through_maze(line[i][0], "true")
    turn_around()
    go_through_maze(line[i][1], "true")
    update_maze_description()
    
    #output
    print("case #" + str(i+1) + ":")
    for y in range(rows-1, -1, -1):
        for x in range(columns):
            print(maze[x][y].description, end = "")
        print()
