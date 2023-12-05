import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

cards = {

}

def countcards(cardnumber,count=1):
    if cardnumber not in cards:
        cards[cardnumber] = count
    else:
        cards[cardnumber] += count

def checkwinnings(line):
    points = 0
    line = line.split(": ")
    cardnumber = int(line[0].replace("Card ",""))
    countcards(cardnumber)
    numbers = line[1].split(" | ")
    winningnumbers = list(filter(None, numbers[0].split(" ")))
    mynumbers = list(filter(None, numbers[1].split(" ")))
    # print(winningnumbers)
    # print(mynumbers)
    for number in mynumbers:
        if number in winningnumbers:
            points += 1
    
    for i in range(cardnumber+1,cardnumber+points+1):
        countcards(i,cards[cardnumber])


    

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()

    for line in lines:
        checkwinnings(line.strip())

    totalcards = 0
    for key in cards.keys():
        totalcards += cards[key]

    print(totalcards)

if __name__ == '__main__':
    main()