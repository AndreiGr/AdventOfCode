import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "data/input.txt")

def processline(line):
    mins = []
    maxs = []

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("zero","0"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("zero","0"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("one","1"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("one","1"), i)], default="-1")) )
    
    mins.append( int(min([i for i in range(len(line)) if line.startswith(("two","2"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("two","2"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("three","3"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("three","3"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("four","4"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("four","4"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("five","5"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("five","5"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("six","6"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("six","6"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("seven","7"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("seven","7"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("eight","8"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("eight","8"), i)], default="-1")) )

    mins.append( int(min([i for i in range(len(line)) if line.startswith(("nine","9"), i)], default="99")) )
    maxs.append( int(max([i for i in range(len(line)) if line.startswith(("nine","9"), i)], default="-1")) )

    return int(str(mins.index(min(mins)))+str(maxs.index(max(maxs))))

def calibrate():
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        total += processline(line)
    
    print(total)


if __name__ == '__main__':
    calibrate()

