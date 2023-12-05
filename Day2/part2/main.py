import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")

def processLine(line):
    minRed = 0
    minGreen = 0
    minBlue = 0
    for turn in line[1].split("; "):
        cubes = turn.strip().split(", ")
        for cube in cubes:
            cube = cube.split(" ")
            if cube[1]=="red" and int(cube[0])> minRed:
                minRed = int(cube[0])
            elif cube[1]=="green" and int(cube[0])> minGreen:
                minGreen = int(cube[0])
            elif cube[1]=="blue" and int(cube[0])> minBlue:
                minBlue = int(cube[0])
    return minRed*minBlue*minGreen

def main():
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        line = line.replace("Game ","")
        total += processLine(line.split(": "))
    
    print(total)

if __name__ == '__main__':
    main()