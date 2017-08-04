# -*- coding:utf-8 -*-
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
            return len(self._cards)

    def __getitem__(self, position):# 支持切片操作
            return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
# print(len(deck))
# print(deck[0])
# print(deck[-1])

# # 从序列中随机抽取一个元素
# from random import choice
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))

# print(deck[:3])# 前3张
# print(deck[12::13])# A牌，先取A再每隔13张拿1张

# for card in deck:#正向迭代
#     print(card)

# for card in reversed(deck): # 反向迭代
#     print(card)

# 没有实现__contains__方法，in运算符按顺序做一次迭代搜索，返回True or False
print(Card('A','hearts') in deck)
print(Card('J','123') in deck)

# 规定大小
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
