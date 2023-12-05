import os
import re
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

possiblegears = {
}

def addnumbertodict(i, j, number):
    if (i,j) in possiblegears:
        possiblegears[i,j].append(number)
    else:
        possiblegears[i,j] = [number]

def processnumber(line0, line1, line2, start, end, row, number):
    if start < 0:
        start = 0

    if end >= len(line1):
        end = len(line1)-1

    for i in range(start,end+1):
        if line0 == "":
            if re.match("\*",line1[i]):
                addnumbertodict(row, i, number)
            if re.match("\*",line2[i]):
                addnumbertodict(row+1, i, number)
        elif line2 == "":
            if re.match("\*",line0[i]):
                addnumbertodict(row-1, i, number)
            if re.match("\*",line1[i]):
                addnumbertodict(row, i, number)
        else:
            if re.match("\*",line0[i]):
                addnumbertodict(row-1, i, number)
            if re.match("\*",line1[i]):
                addnumbertodict(row, i, number)
            if re.match("\*",line2[i]):
                addnumbertodict(row+1, i, number)

def processlines(line0, line1, line2, index):
    for number in re.finditer("[0-9]+", line1): 
        start = int(number.start())
        end = int(number.end())
        processnumber(line0, line1, line2, number.start()-1, number.end(), index, line1[start:end])

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()

    for i in range(0,len(lines)):
        if i == 0:
            processlines("", lines[i].strip(), lines[i+1].strip(), i)
        elif i == len(lines)-1:
            processlines(lines[i-1].strip(), lines[i].strip(), "", i)
        else:
            processlines(lines[i-1].strip(), lines[i].strip(), lines[i+1].strip(), i) 

    gearratio = 0
    for i in possiblegears.keys():
        if len(possiblegears[i]) == 2:
            gearratio += int(possiblegears[i][0]) * int(possiblegears[i][1])
    
    print (gearratio)


if __name__ == '__main__':
    main()