class translator:
    
    # Initialize the spacecraft with its starting position and direction
    def __init__(self, x, y, z, direction):
        self.x = x 
        self.y = y 
        self.z = z 
        self.direction = direction
        self.last_direction = direction
        
        
    # Define a method to move the spacecraft forward or backward
    def move(self, command):
        # Check the current direction and update the position accordingly
        if self.direction == "N":
            if command == "f":
                self.y += 1
            elif command == "b":
                self.y -= 1
        elif self.direction == "S":
            if command == "f":
                self.y -= 1
            elif command == "b":
                self.y += 1
        elif self.direction == "E":
            if command == "f":
                self.x += 1
            elif command == "b":
                self.x -= 1
        elif self.direction == "W":
            if command == "f":
                self.x -= 1
            elif command == "b":
                self.x += 1
        elif self.direction == "Up":
            if command == "f":
                self.z += 1
            elif command == "b":
                self.z -= 1
        elif self.direction == "Down":
            if command == "f":
                self.z -= 1
            elif command == "b":
                self.z += 1

    # Define a method to turn the spacecraft left or right
    def turn(self, command):
        # Check the current direction and update it accordingly
        if self.direction == "N":
            if command == "l":
                self.direction = "W"
            elif command == "r":
                self.direction = "E"
        elif self.direction == "S":
            if command == "l":
                self.direction = "E"
            elif command == "r":
                self.direction = "W"
        elif self.direction == "E":
            if command == "l":
                self.direction = "N"
            elif command == "r":
                self.direction = "S"
        elif self.direction == "W":
            if command == "l":
                self.direction = "S"
            elif command == "r":
                self.direction = "N"
        #Direction is Up so we need last N, S, E, W direction to turn
        elif self.direction == "Up":
            if command == "l":
                if self.last_direction == "N":
                    self.direction = "W"
                elif self.last_direction == "S":
                    self.direction = "E"
                elif self.last_direction == "E":
                    self.direction = "N"
                elif self.last_direction == "W":
                    self.direction = "S"
            elif command == "r":
                if self.last_direction == "N":
                    self.direction = "E"
                elif self.last_direction == "S":
                    self.direction = "W"
                elif self.last_direction == "E":
                    self.direction = "N"
                elif self.last_direction == "S":
                    self.direction = "N"
        #Direction is Down so we need last N, S, E, W direction to turn
        elif self.direction == "Down":
            if command == "l":
                if self.last_direction == "N":
                    self.direction = "W"
                elif self.last_direction == "S":
                    self.direction = "E"
                elif self.last_direction == "E":
                    self.direction = "N"
                elif self.last_direction == "W":
                    self.direction = "S"
            elif command == "r":
                if self.last_direction == "N":
                    self.direction = "E"
                elif self.last_direction == "S":
                    self.direction = "W"
                elif self.last_direction == "E":
                    self.direction = "N"
                elif self.last_direction == "S":
                    self.direction = "N"

    # Define a method to turn the spacecraft up or down
    def tilt(self, command):
        # Check the current direction and update it accordingly
        if self.direction in ["N", "S", "E", "W"]:
            if command == "u":
                self.direction = "Up"
            elif command == "d":
                self.direction = "Down"
        elif self.direction in ["Up", "Down"]:
            if command in ["u", "d"]:
                # Do nothing as the spacecraft cannot tilt further up or down
                pass

    # Define a method to execute a list of commands
    def execute(self, commands):
        # Loop through the commands and call the appropriate methods
        for command in commands:
            #If while turning l or r the direction is up or down using last N, S, E, W direction
            if self.direction in ["N", "S", "E", "W"]:
                self.last_direction = self.direction 
            if command in ["f", "b"]:
                # Move the spacecraft forward or backward
                self.move(command)
            elif command in ["l", "r"]:
                # Turn the spacecraft left or right
                self.turn(command)
            elif command in ["u", "d"]:
                # Turn the spacecraft up or down
                self.tilt(command)

    # Define a method to print the current position and direction of the spacecraft
    def status(self):
        print(f"Position: ({self.x}, {self.y}, {self.z})")
        print(f"Direction: {self.direction}")


# Starting point (x, y, z)
# Initial direction (N, S, E, W, Up, Down)
#direction = translator(0, 0, 0, "N")

# Taking input for commands 
# Character array of commands (f, b, l, r, u, d)
#commands_input = input()
# Splitting input string into a list
#commands = commands_input.split()  

#direction.execute(commands)
#direction.status()