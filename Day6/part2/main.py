import os
import math
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

races = []
times = []

def checkhighesthold(racetime,record):
    for i in range(racetime,1,-1):
        if i * (racetime - i) > record:
            return i
    
def checklowesthold(racetime,record):
    for i in range(1,racetime):
        if i * (racetime - i) > record:
            return i


def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        line = file.readline().replace("Time:","").strip().replace(" ","")
        racetime = int(line)
        line = file.readline().replace("Distance:","").strip().replace(" ","")
        record = int(line)
    
    print(checkhighesthold(racetime,record)-checklowesthold(racetime,record)+1)

if __name__ == '__main__':
    main()