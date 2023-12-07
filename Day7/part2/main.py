import os
import copy
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

cardss = {
	"A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3,
    "J": 2
}

five = []
four = []
full = []
three = []
two = []
one = []
high = []

class Hand:
    def __init__(self, cards, bet, besthand):
        self.cards = cards
        self.bet = bet
        self.besthand = besthand
        
    def __str__(self):
        return f"{self.cards}({self.bet})[{self.besthand}]"
        
    __repr__ = __str__
    
    def __lt__(self, other):
        if self.cards[0] == other.cards[0]:
            if self.cards[1] == other.cards[1]:
                if self.cards[2] == other.cards[2]:
                    if self.cards[3] == other.cards[3]:
                        return cardss[self.cards[4]] < cardss[other.cards[4]]
                    else:
                        return cardss[self.cards[3]] < cardss[other.cards[3]]
                else:
                    return cardss[self.cards[2]] < cardss[other.cards[2]]
            else:
                return cardss[self.cards[1]] < cardss[other.cards[1]]
        else:
            return cardss[self.cards[0]] < cardss[other.cards[0]]
        
def getcardsscore(cards):
    counts = {char: cards.count(char) for char in set(cards)}
    uniques = len(set(cards))

    if any(count == 5 for count in counts.values()):
        return 6
    elif any(count == 4 for count in counts.values()):
        return 5
    elif uniques == 2 and any(count == 3 for count in counts.values()):
        return 4
    elif any(count == 3 for count in counts.values()):
        return 3
    elif uniques == 3 and any(count == 2 for count in counts.values()):
        return 2
    elif uniques == 4:
        return 1
    else:
        return 0

def getstongesthand(cards):
    score = -1
    besthand = ""
    cardreplaced = ""
    if cards.count("J") == 5:
        return cards
    for el in set(cards.replace("J","")):
        newscore = getcardsscore(cards.replace("J",el)) 
        if newscore > score:
            score = newscore
            besthand = cards.replace("J",el)
            cardreplaced = el
        elif newscore == score:
            if cardss[el] > cardss[cardreplaced]:
                besthand = cards.replace("J",el)
                cardreplaced = el
    return besthand

def checkhand(hand):
    counts = {char: hand.besthand.count(char) for char in set(hand.besthand)}
    uniques = len(set(hand.besthand))

    if any(count == 5 for count in counts.values()):
        five.append(hand)
    elif any(count == 4 for count in counts.values()):
        four.append(hand)
    elif uniques == 2 and any(count == 3 for count in counts.values()):
        full.append(hand)
    elif any(count == 3 for count in counts.values()):
        three.append(hand)
    elif uniques == 3 and any(count == 2 for count in counts.values()):
        two.append(hand)
    elif uniques == 4:
        one.append(hand)
    else:
        high.append(hand)



def sortlists():
    five.sort()
    four.sort()
    full.sort()
    three.sort()
    two.sort()
    one.sort()
    high.sort()

def calculateranksum():
    rank = 1
    ranksum = 0
    for element in high:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in one:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in two:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in three:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in full:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in four:
        print(element)
        ranksum += rank * element.bet
        rank += 1
    for element in five:
        print(element)
        ranksum += rank * element.bet
        rank += 1

    print(ranksum)

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip().split(" ")
        checkhand(Hand(line[0],int(line[1]),getstongesthand(line[0])))

    sortlists()
    calculateranksum()


if __name__ == '__main__':
    main()