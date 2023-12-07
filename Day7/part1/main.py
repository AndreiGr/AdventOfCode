import os
import copy
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = os.path.join(FILE_PATH, "../data/input.txt")
TEST_FILE_PATH = os.path.join(FILE_PATH, "../data/test.txt")

cardss = {
	"A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

five = []
four = []
full = []
three = []
two = []
one = []
high = []

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        
    def __str__(self):
        return f"{self.cards}({self.bet})"
        
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
        
def checkhand(hand):
    localhand = copy.deepcopy(hand)
    hand.cards = ''.join(sorted(hand.cards, key=str.lower))
    if hand.cards.count(hand.cards[0]) == 5:
        five.append(localhand)
    elif hand.cards.count(hand.cards[0]) == 4:
        four.append(localhand)
    elif hand.cards.count(hand.cards[0]) == 3:
        hand.cards = hand.cards.replace(hand.cards[0],"")
        if hand.cards.count(hand.cards[0]) == 2:
            full.append(localhand)
        else:
            three.append(localhand)
    elif hand.cards.count(hand.cards[0]) == 2:
        hand.cards = hand.cards.replace(hand.cards[0],"")
        if  hand.cards.count(hand.cards[0]) == 3:
            full.append(localhand)
        elif (hand.cards.count(hand.cards[0]) == 2 ) or (hand.cards.count(hand.cards[1]) == 2 ) or (hand.cards.count(hand.cards[2]) == 2 ):
            two.append(localhand)
        else:
            one.append(localhand)
    elif hand.cards.count(hand.cards[0]) == 1:
        hand.cards = hand.cards.replace(hand.cards[0],"")
        if hand.cards.count(hand.cards[0]) == 4:
            four.append(localhand)
        elif hand.cards.count(hand.cards[0]) == 3:
            hand.cards = hand.cards.replace(hand.cards[0],"")
            if hand.cards.count(hand.cards[0]) == 2:
                full.append(localhand)
            else:
                three.append(localhand)
        elif hand.cards.count(hand.cards[0]) == 2:
            hand.cards = hand.cards.replace(hand.cards[0],"")
            if  hand.cards.count(hand.cards[0]) == 3:
                full.append(localhand)
            elif (hand.cards.count(hand.cards[0]) == 2 ) or (hand.cards.count(hand.cards[1]) == 2 ):
                two.append(localhand)
            else:
                one.append(localhand)
        elif hand.cards.count(hand.cards[0]) == 1:
            hand.cards = hand.cards.replace(hand.cards[0],"")
            if hand.cards.count(hand.cards[0]) == 3:
                three.append(localhand)
            elif hand.cards.count(hand.cards[0]) == 2:
                    two.append(localhand)
            elif hand.cards.count(hand.cards[0]) == 1:
                hand.cards = hand.cards.replace(hand.cards[0],"")
                if hand.cards.count(hand.cards[0]) == 2:
                    one.append(localhand)
                else:
                    high.append(localhand)

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
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in one:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in two:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in three:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in full:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in four:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    for element in five:
        # print("Rank: "+ str(rank) + ";" + str(element))
        ranksum += rank * element.bet
        rank += 1
    
    print(ranksum)

def main():
    # with open(TEST_FILE_PATH,"r") as file:
    with open(INPUT_FILE_PATH,"r") as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip().split(" ")
        checkhand(Hand(line[0],int(line[1])))

    sortlists()
    calculateranksum()


if __name__ == '__main__':
    main()