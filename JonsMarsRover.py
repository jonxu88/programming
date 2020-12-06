#"Nice to have" features: 
# -- detect when one rover collides with another

class Rover:
    def __init__(self, name, x_pos, y_pos, orientation, plateau_ur_corner_x, plateau_ur_corner_y):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.orientation = orientation
        self.plateau_ur_corner_x = plateau_ur_corner_x
        self.plateau_ur_corner_y = plateau_ur_corner_y
        #Print a message and quit if the rover is initially outside the plateau
        if self.isRoverInsidePlateau() == False:
            print("Rover is outside the plateau, please restart the program and choose a starting point inside the plateau.")
            quit()

    def isRoverInsidePlateau(self):
        if self.x_pos < 0 or self.y_pos < 0 or self.x_pos > self.plateau_ur_corner_x or self.y_pos > self.plateau_ur_corner_y:
            return False
        else:
            return True

    def move_forward(self):
        if self.orientation == "N":
            self.y_pos += 1
        elif self.orientation == "E":
            self.x_pos += 1
        elif self.orientation == "S":
            self.y_pos -= 1
        elif self.orientation == "W":
            self.x_pos -= 1 
        #Print a message and exit if the rover falls off the plateau
        if self.isRoverInsidePlateau() == False:
            print("The rover has fallen off the plateau. Please restart the program and try again.")
            quit()

    def turn_left(self):
        turning_left_dict = { "N" : "W", "E" : "N", "S" : "E", "W" : "S" }
        self.orientation = turning_left_dict[self.orientation]
    
    def turn_right(self):
        turning_right_dict = { "N" : "E", "E" : "S", "S" : "W", "W" : "N" }
        self.orientation = turning_right_dict[self.orientation]

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

    def print_stop_message(self):
        print(self.name + " has carried out its orders. It has stopped at (" + str(self.x_pos) + "," + str(self.y_pos) + "), and is facing " + self.orientation + ".")

# A function that takes in the string "(x,y)" (IMPORTANT, DON'T INPUT A TUPLE, INPUT A STRING) and returns the integers x and y
def extract_coords(xystring):
    x = xystring.split(',')[0]
    x = x.split('(')[1]
    x = int(x)
    y = xystring.split(',')[1]
    y = y.split(')')[0]
    y = int(y)  
    return x, y

#Program starts here
plateau_ur_corner = input("Enter (x,y) coordinate of the upper right coordinate of the plateau: ")
plateau_ur_corner_x, plateau_ur_corner_y = extract_coords(plateau_ur_corner)

number_of_rovers = input("Enter number of rovers: ")
number_of_rovers = int(number_of_rovers)
for i in range(0,number_of_rovers):
    rover_name = input("Enter the name of rover number {}: ".format(str(i+1)))
    rover_coord = input("Enter the starting (x,y) coordinate of rover number {}: ".format(str(i+1)))
    rover_coord_x, rover_coord_y = extract_coords(rover_coord)
    rover_initial_orientation = input("Enter the initial orientation of rover number {}: ".format(str(i+1)))
    #Instantiate a rover
    rover = Rover(rover_name, rover_coord_x, rover_coord_y, rover_initial_orientation, plateau_ur_corner_x, plateau_ur_corner_y)
    rover_instructions = input("Enter the string of instructions to send to rover number {} (the instructions will be read from left to right): ".format(str(i+1)))
    #Split the string into individual letters
    rover_instructions = [rover_instructions[i:i+1] for i in range(0, len(rover_instructions))]
    #Send the instructions to the rover
    for j in range(0,len(rover_instructions)):
        rover.issue_command(rover_instructions[j])
    rover.print_stop_message()
