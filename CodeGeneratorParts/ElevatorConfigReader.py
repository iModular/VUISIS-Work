import os
config = open(r"C:\Users\weird\OneDrive\Documents\ElevatorConfig.txt")
configContent = config.read()

numElevators = int(configContent[21])

numFloors = int(configContent[41])



template = open(r"C:\Users\weird\OneDrive\Documents\ElevatorTemplate.txt")

templateContent = template.readlines()
buttonPressed = (templateContent[0:3])
buttonPressed = ''.join(buttonPressed)
globalVars = templateContent[3:7]
globalVars = ''.join(globalVars)
elevatorIdleFunc = templateContent[7:13]
elevatorIdleFunc = ''.join(elevatorIdleFunc)
elevDownFunc = templateContent[13:23]
elevDownFunc = ''.join(elevDownFunc)
elevUpFunc = templateContent[24:34]
elevUpFunc = ''.join(elevUpFunc)
elevGoFloorFuncp1 = ''.join(templateContent[34:50]).replace("1-5", "1-" + str(numFloors))
elevGoFloorFuncp2 = ''.join(templateContent[50:53])
elevGoFloorFuncp3 = ''.join(templateContent[60:65])
insideButton = templateContent[65:79]
insideButton = ''.join(insideButton)
elifClause = templateContent[79:89]
elifClause = ''.join(elifClause)
ifBusy = templateContent[89:94]
ifBusy = ''.join(ifBusy)
buttonUp = templateContent[95:103]
buttonUp = ''.join(buttonUp)
buttonDown = templateContent[111:120]
buttonDown = ''.join(buttonDown)
inputFloorFuncp1 = ''.join(templateContent[128:130])
inputFloorFuncp2 = ''.join(templateContent[131:133])
inputFloorFuncp3 = ''.join(templateContent[133:136])
inputDirectionFunc = ''.join (templateContent[136:150]).replace("numFloors", str(numFloors))
pressButtonFuncp1 = ''.join(templateContent[151:155])
pressButtonFuncp2 = ''.join(templateContent[155:160])
pressButtonFuncp3 = ''.join(templateContent[160:163]).replace("numFloors", str(numFloors))
initiate = ''.join(templateContent[164:165])
template.close()

code = open(r"C:\Users\weird\OneDrive\Documents\ElevatorCodeGenerated.txt", "w+")
code.truncate()
code.write(buttonPressed)
x = 2
for i in range(numElevators):
    code.write(globalVars + "\n")
    globalVars = globalVars.replace(str(x-1), str(x))
    x = x+1
a = 2
y=2
for i in range(numElevators):
    code.write(elevatorIdleFunc + "\n")
    elevatorIdleFunc = elevatorIdleFunc.replace("lev" + str(y-1), "lev" + str(y))
    code.write(elevDownFunc + "\n")
    elevDownFunc = elevDownFunc.replace("lev" + str(y-1), "lev" + str(y))
    code.write(elevUpFunc + "\n")
    elevUpFunc = elevUpFunc.replace("lev" + str(y-1), "lev" + str(y))
    code.write(elevGoFloorFuncp1 + "\n")
    elevGoFloorFuncp1 = elevGoFloorFuncp1.replace("lev" + str(y-1), "lev" + str(y))
    for i in range (numFloors):
        code.write(elevGoFloorFuncp2)
        elevGoFloorFuncp2 = ''.join(templateContent[50:52]).replace("== 1", "== " + str(a))
        elevGoFloorFuncp2 = elevGoFloorFuncp2.replace("ton1", "ton" + str(a))
        a= a+1
    elevGoFloorFuncp2 = ''.join(templateContent[50:52])
    code.write(elevGoFloorFuncp3)
    elevGoFloorFuncp3 = elevGoFloorFuncp3.replace("lev" + str(y-1), "lev" + str(y))

    a =2
    y = y+1


z = 2
a = 3
for i in range(numFloors):
    code.write(insideButton + "\n")
    for i in range(numElevators-1):
        code.write(elifClause)
        elifClause = elifClause.replace("lev" + str(a-1), "lev" + str(a))
        a = a+1
    a = 3
    elifClause = templateContent[78:88]
    elifClause = ''.join(elifClause).replace("(1,", "(" + str(z) + ",")
    code.write(ifBusy)
    ifBusy = ifBusy.replace(str(z-1), str(z))
    insideButton = insideButton.replace("B" + str(z-1), "B" + str(z))
    insideButton = insideButton.replace("ton" + str(z-1), "ton" + str(z)) 
    insideButton = insideButton.replace("ton " + str(z-1), "ton " + str(z))
    insideButton = insideButton.replace("oor " + str(z-1), "oor " + str(z))
    insideButton = insideButton.replace("(" + str(z-1) + ",", "(" + str(z) + ",")
    z = z+1
r = 2
a = 3
elifClause = ''.join(templateContent[120:123]).replace("(1,", "(2,")
ifBusy = ''.join(templateContent[123:127]).replace("oor 1" , "oor 2")   
for i in range(numFloors-1):
    buttonDown = buttonDown.replace("F" + str(r-1), "F" + str(r))
    buttonDown = buttonDown.replace("oor " + str(r-1), "oor " + str(r))
    buttonDown = buttonDown.replace("(" + str(r-1) + ",", "(" + str(r) + ",")
    code.write(buttonDown)
    r = r+1
    for i in range(numElevators-1):
        code.write(elifClause)
        elifClause = elifClause.replace("lev" + str(a-1), "lev" + str(a))
        a = a+1
    a = 3
    elifClause = ''.join(templateContent[120:123]).replace("(1,", "(" + str(r) + ",")    
    code.write(ifBusy)
    ifBusy = ''.join(templateContent[123:127]).replace("oor 1", "oor " + str(r))

elifClause = ''.join(templateContent[103:106])
ifBusy = ''.join(templateContent[106:111])
r = 2
a = 3
for i in range (numFloors-1):
    code.write(buttonUp)
    buttonUp = buttonUp.replace("F" + str(r-1), "F" + str(r))
    buttonUp = buttonUp.replace("oor " + str(r-1), "oor " + str(r))
    buttonUp = buttonUp.replace("(" + str(r-1) + ",", "(" + str(r) + ",")
    for i in range(numElevators-1):
        code.write(elifClause)
        elifClause = elifClause.replace("lev" + str(a-1), "lev" + str(a))
        a = a+1
    a = 3
    code.write(ifBusy)
    elifClause = ''.join(templateContent[103:106]).replace("(1,", "(" + str(r) + ",")    
    ifBusy = ''.join(templateContent[106:111]).replace("oor 1", "oor " + str(r))
    r = r+1
a = 2
code.write(inputFloorFuncp1)
for i in range(numFloors):
    code.write(inputFloorFuncp2)
    inputFloorFuncp2 = inputFloorFuncp2.replace(str(a-1), str(a))
    a = a+1
code.write(inputFloorFuncp3)
code.write(inputDirectionFunc)

a = 3
code.write(pressButtonFuncp1)
for i in range(numFloors-2):
    code.write(pressButtonFuncp2)
    pressButtonFuncp2 = pressButtonFuncp2.replace(str(a-1), str(a))
code.write(pressButtonFuncp3)
code.write(initiate)
code.close()

originalFile = r"C:\Users\weird\OneDrive\Documents\ElevatorCodeGenerated.txt"
newFile = r"C:\Users\weird\OneDrive\Documents\ElevatorCodeGenerated.py"

if os.path.exists(newFile):
        os.remove(newFile)
os.rename(originalFile, newFile)
print("File renamed from " + originalFile + " to " + newFile)