#Next to do: use magic method so that one can create more than one rover.
#"Nice to have" features: 
# -- detect when one rover collides with another
# -- detech when a rover "falls off" the plateau (otherwise what's the point of specifying the plateau?)

#Code to add 2d vectors without using numpy, copied from the Sololearn lesson on magic methods
#NOT USED
class Vect_2d:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __add__(self, other):
        return Vect_2d(self.x_pos + other.x_pos, self.y_pos + other.y_pos)

class Plateau:
    def __init__(self, x_upper_right, y_upper_right):
        self.x_upper_right = x_upper_right
        self.y_upper_right = y_upper_right

class Rover:
    def __init__(self, name, x_pos, y_pos, orientation):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.orientation = orientation

    def move_forward(self):
        if self.orientation == "N":
            self.y_pos += 1
        elif self.orientation == "E":
            self.x_pos += 1
        elif self.orientation == "S":
            self.y_pos -= 1
        elif self.orientation == "W":
            self.x_pos -= 1 

    def turn_left(self):
        if self.orientation == "N":
            self.orientation = "W"
        elif self.orientation == "E":
            self.orientation = "N"
        elif self.orientation == "S":
            self.orientation = "E"
        elif self.orientation == "W":
            self.orientation = "S" 
    
    def turn_right(self):
        if self.orientation == "N":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "N" 

    def issue_command(self, letter):
        if letter == "M":
            self.move_forward()
        elif letter == "L":
            self.turn_left()
        elif letter == "R":
            self.turn_right()
        else:
            print("Something is wrong with the input instructions sent to the rover named {}".format(self.name))
        print(self.name + " has moved to (" + str(self.x_pos) + "," + str(self.y_pos) + ") and is facing " + self.orientation + ".")

# A function that takes in the string "(x,y)" (IMPORTANT, DON'T INPUT A TUPLE, INPUT A STRING) and returns the integers x and y
def extract_coords(xystring):
    x = xystring.split(',')[0]
    x = x.split('(')[1]
    x = int(x)
    y = xystring.split(',')[1]
    y = y.split(')')[0]
    y = int(y)  
    return x, y

# Do for one rover first

# Enter x-coordinate of the upper right corner of the plateau
# Enter y-coordinate of the upper right corner of the plateau
# Enter name of rover
# Enter rovers initial x-coordinate
# Enter rovers initial y-coordinate
# Enter rovers orientation
# Enter string of instructions to send to rover (no spaces)
# Output the rover's final coordinates and heading

ur_corner = input("Enter (x,y) coordinate of the upper right coordinate of the plateau: ")
ur_corner_x, ur_corner_y = extract_coords(ur_corner)
#Create a plateau with (x,y) as the upper right corner
plateau = Plateau(ur_corner_x, ur_corner_y)

rover_name = input("Enter the name of the rover: ")
rover_coord = input("Enter (x,y) coordinate of the rover: ")
rover_coord_x, rover_coord_y = extract_coords(rover_coord)
rover_initial_orientation = input("Enter the rover's initial orientation: ")
#Instantiate a rover
rover = Rover(rover_name, rover_coord_x, rover_coord_y, rover_initial_orientation)
rover_instructions = input("Enter the string of instructions to send to rover (the instructions will be read from left to right): ")
#Split the string into individual letters
rover_instructions = [rover_instructions[i:i+1] for i in range(0, len(rover_instructions))]
print(rover_instructions)
for i in range(0,len(rover_instructions)):
    rover.issue_command(rover_instructions[i])
