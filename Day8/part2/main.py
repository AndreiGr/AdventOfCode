import os
import re
import math
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

waypoints = {

}
steps = []
test = ""
currentwaypoints = []
def getstep(step):
    if step == "L":
        return 0
    elif step == "R":
        return 1

# def nextstep():
#     sum = 0
#     stepindex = 0
#     while (True):
#         left = []
#         right = []
#         finalwaypoints = []
#         print(currentwaypoints)
#         {left.append(waypoints[element][0]) for element in currentwaypoints}
#         # left = waypoints[currentwaypoint][0]
#         {right.append(waypoints[element][1]) for element in currentwaypoints}
#         # right = waypoints[currentwaypoint][1]
#         {finalwaypoints.append(element) for element in currentwaypoints if re.match("[A-Y0-9][A-Y0-9]Z",element)}
#         direction = steps[0][stepindex] if stepindex < len(steps[0]) else steps[0][0]
#         nextstepindex = stepindex+1 if stepindex+1 < len(steps[0]) else 0
#         if len(finalwaypoints) != len(currentwaypoints):
#             sum += 1
#             stepindex = nextstepindex
#             currentwaypoints.clear()
#             if direction == "L":
#                 {currentwaypoints.append(element) for element in left}
#             elif direction == "R":
#                 {currentwaypoints.append(element) for element in right}
#         else:
#             break
#     return sum

def nextstep(waypoint):
    sum = 0
    currentwaypoint = waypoint
    stepindex = 0
    while (True):
        left = waypoints[currentwaypoint][0]
        right = waypoints[currentwaypoint][1]
        direction = steps[0][stepindex] if stepindex < len(steps[0]) else steps[0][0]
        nextstepindex = stepindex+1 if stepindex+1 < len(steps[0]) else 0
        if not re.match("[A-Y0-9][A-Y0-9]Z", currentwaypoint):
            sum += 1
            stepindex = nextstepindex
            currentwaypoint = left if direction == "L" else right
        else:
            break
    return sum


def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        steps.append(file.readline().strip())
        file.readline()
        lines = file.readlines()


    for line in lines:
        line = line.strip().split(" = ")
        origin = line[0]
        destinations = line[1].replace("(","").replace(")","").split(", ")
        waypoints[origin] = [destinations[0],destinations[1]]
    
    x = {currentwaypoints.append(key) for key in waypoints.keys() if key.endswith("A")}

    stepstofinal = []
    for wp in currentwaypoints:
        stepstofinal.append(nextstep(wp))

    lcm = 1
    for i in stepstofinal:
        lcm = lcm*i//math.gcd(lcm, i)
    print(lcm)
    # print(nextstep())


    print(stepstofinal)



if __name__ == '__main__':
    main()