import os
import re
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

engineparts = []
def processnumber(line0, line1, line2, start, end):
    if start < 0:
        start = 0

    if end >= len(line1):
        end = len(line1)-1

    for i in range(start,end+1):
        if line0 == "":
            if re.match("[^a-zA-Z0-9_.]",line1[i]) or re.match("[^a-zA-Z0-9_.]",line2[i]):
                return True
        elif line2 == "":
            if re.match("[^a-zA-Z0-9_.]",line0[i]) or re.match("[^a-zA-Z0-9_.]",line1[i]):
                return True
        else:
            if re.match("[^a-zA-Z0-9_.]",line0[i]) or re.match("[^a-zA-Z0-9_.]",line1[i]) or re.match("[^a-zA-Z0-9_.]",line2[i]):
                return True
    return False

def processlines(line0, line1, line2):
    for number in re.finditer("[0-9]+", line1): 
        if processnumber(line0, line1, line2, number.start()-1, number.end()):
            start = int(number.start())
            end = int(number.end())
            engineparts.append(int(line1[start:end]))

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()

    for i in range(0,len(lines)):
        if i == 0:
             processlines("", lines[i].strip(), lines[i+1].strip())
        elif i == len(lines)-1:
             processlines(lines[i-1].strip(), lines[i].strip(), "")
        else:
             processlines(lines[i-1].strip(), lines[i].strip(), lines[i+1].strip())

    print(sum(engineparts)) 
    

if __name__ == '__main__':
    main()