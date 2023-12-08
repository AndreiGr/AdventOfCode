import os
import copy
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

waypoints = {

}
steps = []
test = ""

def nextstep():
    sum = 0
    currentwaypoint = "AAA"
    stepindex = 0
    while (True):
        left = waypoints[currentwaypoint][0]
        right = waypoints[currentwaypoint][1]
        direction = steps[0][stepindex] if stepindex < len(steps[0]) else steps[0][0]
        nextstepindex = stepindex+1 if stepindex+1 < len(steps[0]) else 0
        if currentwaypoint != "ZZZ":
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
    
    print(nextstep())


if __name__ == '__main__':
    main()