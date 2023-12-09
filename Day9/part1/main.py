import os
import pandas
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

def getnextelement(series):
    last = []
    last.append(series.iloc[-1])
    diff = series.diff().dropna()
    iszero = list(set(diff))
    while not (len(iszero) == 1 and iszero[0] == 0):
        # print(diff)
        last.append(diff.iloc[-1])
        diff = diff.diff().dropna()
        iszero = list(set(diff))
    
    next = 0
    for el in reversed(last):
        next += el
    
    return next



def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()

    sum = 0
    for line in lines:
        sum += getnextelement(pandas.Series(list(map(int, line.split(" ")))))
    
    print(sum)


if __name__ == '__main__':
    main()