import time
def wait():
    print("No Elevators Are Available")
global Elev1Busy
global currentElev1Floor
currentElev1Floor = 1
Elev1Busy = False

global Elev2Busy
global currentElev2Floor
currentElev2Floor = 2
Elev2Busy = False

global Elev3Busy
global currentElev3Floor
currentElev3Floor = 3
Elev3Busy = False


def elev1Idle(x):
    global Elev1Busy
    global currentElev1Floor
    currentElev1Floor = x
    Elev1Busy = False


def elev1Down(x, r):
    global currentElev1Floor
    y = currentElev1Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev1Floor = y - f
        f = f + 1
        print("Floor " + str(currentElev1Floor))
        time.sleep(2)


def elev1Up(x, r):
    global currentElev1Floor
    y = currentElev1Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev1Floor = y + f
        f = f + 1
        print("Floor " + str(currentElev1Floor))
        time.sleep(2)


def elev1GoFloor(n, direction):
	#stuff
    global currentElev1Floor
    global Elev1Busy
    Elev1Busy == True
    if currentElev1Floor > n:
        elev1Down(currentElev1Floor, n)
    elif currentElev1Floor < n:
        elev1Up(currentElev1Floor, n)
    print("Doors Opening")
    time.sleep(2)
    print("Doors open")
    time.sleep(2)
    if direction != 3:
        floorSelected = int(input("What floor, 1-4, would you like to go to? "))

        if floorSelected == 1:
            lightButton1(1)

        if floorSelected == 2:
            lightButton2(1)
        if floorSelected == 3:
            lightButton3(1)
        if floorSelected == 4:
            lightButton4(1)
    else:
        print("Doors Closing")
        time.sleep(2)
        print("Doors Closed")
    elev1Idle(n)

def elev2Idle(x):
    global Elev2Busy
    global currentElev2Floor
    currentElev2Floor = x
    Elev2Busy = False


def elev2Down(x, r):
    global currentElev2Floor
    y = currentElev2Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev2Floor = y - f
        f = f + 1
        print("Floor " + str(currentElev2Floor))
        time.sleep(2)


def elev2Up(x, r):
    global currentElev2Floor
    y = currentElev2Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev2Floor = y + f
        f = f + 1
        print("Floor " + str(currentElev2Floor))
        time.sleep(2)


def elev2GoFloor(n, direction):
	#stuff
    global currentElev2Floor
    global Elev2Busy
    Elev2Busy == True
    if currentElev2Floor > n:
        elev2Down(currentElev2Floor, n)
    elif currentElev2Floor < n:
        elev2Up(currentElev2Floor, n)
    print("Doors Opening")
    time.sleep(2)
    print("Doors open")
    time.sleep(2)
    if direction != 3:
        floorSelected = int(input("What floor, 1-4, would you like to go to? "))

        if floorSelected == 1:
            lightButton1(1)
        if floorSelected == 2:
            lightButton2(1)
        if floorSelected == 3:
            lightButton3(1)
        if floorSelected == 4:
            lightButton4(1)
    else:
        print("Doors Closing")
        time.sleep(2)
        print("Doors Closed")
    elev2Idle(n)

def elev3Idle(x):
    global Elev3Busy
    global currentElev3Floor
    currentElev3Floor = x
    Elev3Busy = False


def elev3Down(x, r):
    global currentElev3Floor
    y = currentElev3Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev3Floor = y - f
        f = f + 1
        print("Floor " + str(currentElev3Floor))
        time.sleep(2)


def elev3Up(x, r):
    global currentElev3Floor
    y = currentElev3Floor
    f = 1
    for i in range(abs(x - r)):
        currentElev3Floor = y + f
        f = f + 1
        print("Floor " + str(currentElev3Floor))
        time.sleep(2)


def elev3GoFloor(n, direction):
	#stuff
    global currentElev3Floor
    global Elev3Busy
    Elev3Busy == True
    if currentElev3Floor > n:
        elev3Down(currentElev3Floor, n)
    elif currentElev3Floor < n:
        elev3Up(currentElev3Floor, n)
    print("Doors Opening")
    time.sleep(2)
    print("Doors open")
    time.sleep(2)
    if direction != 3:
        floorSelected = int(input("What floor, 1-4, would you like to go to? "))

        if floorSelected == 1:
            lightButton1(1)
        if floorSelected == 2:
            lightButton2(1)
        if floorSelected == 3:
            lightButton3(1)
        if floorSelected == 4:
            lightButton4(1)
    else:
        print("Doors Closing")
        time.sleep(2)
        print("Doors Closed")
    elev3Idle(n)

def lightButton1(c):
    B1 = c
    if B1:
        print("Button 1 lit")
        if Elev1Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev1GoFloor(1, 3)


        elif Elev2Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev2GoFloor(1, 3)

        elif Elev3Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev3GoFloor(1, 3)
	
        else:
            wait()
    else:
        print("Button 1 unlit")

def lightButton2(c):
    B2 = c
    if B2:
        print("Button 2 lit")
        if Elev1Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 2")
            time.sleep(1)
            elev1GoFloor(2, 3)

            elev1GoFloor(2, 3)

        elif Elev2Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev1GoFloor(2, 3)

        elif Elev3Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
	
        else:
            wait()
    else:
        print("Button 2 unlit")

def lightButton3(c):
    B3 = c
    if B3:
        print("Button 3 lit")
        if Elev1Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 3")
            time.sleep(1)
            elev1GoFloor(3, 3)

            elev1GoFloor(3, 3)

        elif Elev2Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev1GoFloor(3, 3)

        elif Elev3Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
	
        else:
            wait()
    else:
        print("Button 3 unlit")

def lightButton4(c):
    B4 = c
    if B4:
        print("Button 4 lit")
        if Elev1Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 4")
            time.sleep(1)
            elev1GoFloor(4, 3)

            elev1GoFloor(4, 3)

        elif Elev2Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
            elev1GoFloor(4, 3)

        elif Elev3Busy == False:
            time.sleep(1)
            print("Doors Closing")
            time.sleep(2)
            print("Doors Closed")
            time.sleep(1)
            print("Person going to Floor 1")
            time.sleep(1)
	
        else:
            wait()
    else:
        print("Button 4 unlit")

def lightButtonF2Down(c):
    BF2D = c
    if BF2D:
        print("Button Floor 2 Down lit")
        print("elev going to Floor 2")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(2, 1)
        elif Elev2Busy == False:
            time.sleep(1)
            elev2GoFloor(2, 1)
        elif Elev3Busy == False:
            time.sleep(1)
            elev3GoFloor(2, 1)
        else:
            wait()
    else:
        print("Button Floor 2 Down unlit")

def lightButtonF3Down(c):
    BF3D = c
    if BF3D:
        print("Button Floor 3 Down lit")
        print("elev going to Floor 3")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(3, 1)
        elif Elev2Busy == False:
            time.sleep(1)
            elev2GoFloor(3, 1)
        elif Elev3Busy == False:
            time.sleep(1)
            elev3GoFloor(3, 1)
        else:
            wait()
    else:
        print("Button Floor 3 Down unlit")

def lightButtonF4Down(c):
    BF4D = c
    if BF4D:
        print("Button Floor 4 Down lit")
        print("elev going to Floor 4")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(4, 1)
        elif Elev2Busy == False:
            time.sleep(1)
            elev2GoFloor(4, 1)
        elif Elev3Busy == False:
            time.sleep(1)
            elev3GoFloor(4, 1)
        else:
            wait()
    else:
        print("Button Floor 4 Down unlit")
def lightButtonF1Up(c):
    BF1U = c
    if BF1U:
        print("Button Floor 1 Up lit")
        print("elev going to Floor 1")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(1, 0)
        elif Elev2Busy == False:
            time.sleep(1)
            elev1GoFloor(1, 0)
        elif Elev3Busy == False:
            time.sleep(1)
            elev1GoFloor(1, 0)
        else:
            wait()
    else:
        print("Button Floor 1 Up unlit")

def lightButtonF2Up(c):
    BF2U = c
    if BF2U:
        print("Button Floor 2 Up lit")
        print("elev going to Floor 2")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(2, 0)
        elif Elev2Busy == False:
            time.sleep(1)
            elev1GoFloor(2, 0)
        elif Elev3Busy == False:
            time.sleep(1)
            elev1GoFloor(2, 0)
        else:
            wait()
    else:
        print("Button Floor 2 Up unlit")

def lightButtonF3Up(c):
    BF3U = c
    if BF3U:
        print("Button Floor 3 Up lit")
        print("elev going to Floor 3")
        if Elev1Busy == False:
            time.sleep(1)
            elev1GoFloor(3, 0)
        elif Elev2Busy == False:
            time.sleep(1)
            elev1GoFloor(3, 0)
        elif Elev3Busy == False:
            time.sleep(1)
            elev1GoFloor(3, 0)
        else:
            wait()
    else:
        print("Button Floor 3 Up unlit")

def personInputFloor():
        floor = str(input("What Floor are you starting on?"))
        if floor == "1":
            personInputDirection(floor)
        if floor == "2":
            personInputDirection(floor)
        if floor == "3":
            personInputDirection(floor)
        if floor == "4":
            personInputDirection(floor)
        else:
            print("Invalid choice, please try again")
            personInputFloor()

def personInputDirection(floor):
    desiredDirection = str(input("Would you like to go up or down?"))
    if desiredDirection.lower() != "up" and desiredDirection.lower() != "down":
        print("Invalid choice, please try again")
        personInputDirection(floor)
    elif desiredDirection.lower() == "down" and floor == "1":
        print("You cannot go down on floor 1")
        personInputDirection(floor)
    elif desiredDirection.lower() == "up" and floor == 4:
        print("You cannot go up on Floor 4")
        personInputDirection(floor)
    else:
        personPressesButton(floor, desiredDirection.lower())
def personPressesButton(floor, desiredDirection):
    if floor == "1":
        if desiredDirection.lower() == "up":
            lightButtonF1Up(1)
    if floor == "2":
        if desiredDirection.lower() == "up":
            lightButtonF2Up(1)
        elif desiredDirection.lower() == "down":
            lightButtonF2Down(1)
    if floor == "3":
        if desiredDirection.lower() == "up":
            lightButtonF3Up(1)
        elif desiredDirection.lower() == "down":
            lightButtonF3Down(1)
    if floor == "4":
        if desiredDirection.lower() == "down": 
                lightButtonF4Down(1)
personInputFloor()