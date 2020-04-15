import itertools
import numpy as np

hearts = list(itertools.product('h', range(2,15)))
diamonds = list(itertools.product('d', range(2,15)))
spades = list(itertools.product('s', range(2,15)))
clubs = list(itertools.product('c', range(2,15)))

deck = []
deck.append(hearts)
deck.append(diamonds)
deck.append(spades)
deck.append(clubs)
shuffled_deck = [[], [], [], []]
number_of_hokms = np.around(np.random.normal(10, 1.2, 4))

def card_choice(lst):
    index1 = np.random.randint(0, len(lst))
    choice = lst[index1]
    del lst[index1]
    return choice

def suit_choice(index2):
    suit_set = {0,1,2,3}
    index2_reverse = list(suit_set - {index2})
    choice = np.random.choice(index2_reverse)
    return choice

def convertlist(lst):
    cl = []
    for cnt in range(0, len(lst)):
        cl = cl + lst[cnt]
    return cl

def shuffle():
    for cnt1 in range(0,13):
        for cnt2 in range(0,4):
            if cnt1 < number_of_hokms[cnt2]:
                shuffled_deck[cnt2].append(card_choice(deck[cnt2]))
    cl = convertlist(deck)
    for cnt1 in range(0,13):
        for cnt2 in range(0,4):
            if len(shuffled_deck[cnt2]) == 13:
                pass
            else:
                shuffled_deck[cnt2].append(card_choice(cl))
    return shuffled_deck

shuffle()
