import os
import math
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

races = []
times = []

def checkhigherhold(holdtime,index):
    speed = holdtime
    distance = (races[index]-holdtime)*speed
    if distance > times[index]:
        return 1+checkhigherhold(holdtime+1,index)
    return 0
    
def checklowerhold(holdtime,index):
    speed = holdtime
    distance = (races[index]-holdtime)*speed
    if distance > times[index]:
        return 1+checklowerhold(holdtime-1,index)
    return 0

def checkhalfhold(holdtime,index):
    speed = holdtime
    distance = (races[index]-holdtime)*speed
    if distance > times[index]:
        return 1 + checkhigherhold(holdtime+1,index) + checklowerhold(holdtime-1,index)
    else:
        return 0 + checkhigherhold(holdtime+1,index)


def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        line = file.readline().replace("Time:","").strip().split(" ")
        for element in line:
            if element != "":
                races.append(int(element))
        line = file.readline().replace("Distance:","").strip().split(" ")
        for element in line:
            if element != "":
                times.append(int(element))

    total = 1
    for i in range(0,len(races)):
        x = checkhalfhold(math.floor(races[i]/2),i)
        print(x)
        total = total*x
    
    print(total)

if __name__ == '__main__':
    main()