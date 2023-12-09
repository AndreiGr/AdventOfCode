import os
import pandas
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

def getnextelement(series):
    first = []
    first.append(series.iloc[0])
    diff = series.diff().dropna()
    iszero = list(set(diff))
    while not (len(iszero) == 1 and iszero[0] == 0):
        # print(diff)
        first.append(diff.iloc[0])
        diff = diff.diff().dropna()
        iszero = list(set(diff))
    first.append(0)

    previous = -1
    isfirsttime = True
    for el in reversed(first) :
        if isfirsttime:
            previous = el
            isfirsttime = False
        else:
            previous = el-previous
    
    return previous



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