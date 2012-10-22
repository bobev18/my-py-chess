# -*- coding: utf-8 -*-

from piece import piece

#const
plainboardinit = {'a8':'br', 'b8':'bn', 'c8':'bb', 'd8':'bq', 'e8':'bk', 'f8':'bb', 'g8':'bn', 'h8':'br',
                 'a7':'bp', 'b7':'bp', 'c7':'bp', 'd7':'bp', 'e7':'bp', 'f7':'bp', 'g7':'bp', 'h7':'bp',
                 'a6':'  ', 'b6':'  ', 'c6':'  ', 'd6':'  ', 'e6':'  ', 'f6':'  ', 'g6':'  ', 'h6':'  ',
                 'a5':'  ', 'b5':'  ', 'c5':'  ', 'd5':'  ', 'e5':'  ', 'f5':'  ', 'g5':'  ', 'h5':'  ',
                 'a4':'  ', 'b4':'  ', 'c4':'  ', 'd4':'  ', 'e4':'  ', 'f4':'  ', 'g4':'  ', 'h4':'  ',
                 'a3':'  ', 'b3':'  ', 'c3':'  ', 'd3':'  ', 'e3':'  ', 'f3':'  ', 'g3':'  ', 'h3':'  ',
                 'a2':'wp', 'b2':'wp', 'c2':'wp', 'd2':'wp', 'e2':'wp', 'f2':'wp', 'g2':'wp', 'h2':'wp',
                 'a1':'wr', 'b1':'wn', 'c1':'wb', 'd1':'wq', 'e1':'wk', 'f1':'wb', 'g1':'wn', 'h1':'wr',}

emptyboardinit = {'a8':'  ', 'b8':'  ', 'c8':'  ', 'd8':'  ', 'e8':'  ', 'f8':'  ', 'g8':'  ', 'h8':'  ',
                 'a7':'  ', 'b7':'  ', 'c7':'  ', 'd7':'  ', 'e7':'  ', 'f7':'  ', 'g7':'  ', 'h7':'  ',
                 'a6':'  ', 'b6':'  ', 'c6':'  ', 'd6':'  ', 'e6':'  ', 'f6':'  ', 'g6':'  ', 'h6':'  ',
                 'a5':'  ', 'b5':'  ', 'c5':'  ', 'd5':'  ', 'e5':'  ', 'f5':'  ', 'g5':'  ', 'h5':'  ',
                 'a4':'  ', 'b4':'  ', 'c4':'  ', 'd4':'  ', 'e4':'  ', 'f4':'  ', 'g4':'  ', 'h4':'  ',
                 'a3':'  ', 'b3':'  ', 'c3':'  ', 'd3':'  ', 'e3':'  ', 'f3':'  ', 'g3':'  ', 'h3':'  ',
                 'a2':'  ', 'b2':'  ', 'c2':'  ', 'd2':'  ', 'e2':'  ', 'f2':'  ', 'g2':'  ', 'h2':'  ',
                 'a1':'  ', 'b1':'  ', 'c1':'  ', 'd1':'  ', 'e1':'  ', 'f1':'  ', 'g1':'  ', 'h1':'  ',}

p2s2d = {(1,1):"a1",(1,2):"a2",(1,3):"a3",(1,4):"a4",(1,5):"a5",(1,6):"a6",(1,7):"a7",(1,8):"a8",
        (2,1):"b1",(2,2):"b2",(2,3):"b3",(2,4):"b4",(2,5):"b5",(2,6):"b6",(2,7):"b7",(2,8):"b8",
        (3,1):"c1",(3,2):"c2",(3,3):"c3",(3,4):"c4",(3,5):"c5",(3,6):"c6",(3,7):"c7",(3,8):"c8",
        (4,1):"d1",(4,2):"d2",(4,3):"d3",(4,4):"d4",(4,5):"d5",(4,6):"d6",(4,7):"d7",(4,8):"d8",
        (5,1):"e1",(5,2):"e2",(5,3):"e3",(5,4):"e4",(5,5):"e5",(5,6):"e6",(5,7):"e7",(5,8):"e8",
        (6,1):"f1",(6,2):"f2",(6,3):"f3",(6,4):"f4",(6,5):"f5",(6,6):"f6",(6,7):"f7",(6,8):"f8",
        (7,1):"g1",(7,2):"g2",(7,3):"g3",(7,4):"g4",(7,5):"g5",(7,6):"g6",(7,7):"g7",(7,8):"g8",
        (8,1):"h1",(8,2):"h2",(8,3):"h3",(8,4):"h4",(8,5):"h5",(8,6):"h6",(8,7):"h7",(8,8):"h8",}

s2p = {'f1': (6, 1), 'f2': (6, 2), 'f3': (6, 3), 'f4': (6, 4), 'b2': (2, 2), 'f6': (6, 6), 'f7': (6, 7), 'h2': (8, 2), 'h3': (8, 3), 'h1': (8, 1), 'h6': (8, 6), 'h7': (8, 7), 'h4': (8, 4), 'h5': (8, 5), 'b4': (2, 4), 'b5': (2, 5), 'b6': (2, 6), 'b7': (2, 7), 'b1': (2, 1), 'd8': (4, 8), 'c2': (3, 2), 'd6': (4, 6), 'd7': (4, 7), 'd4': (4, 4), 'd5': (4, 5), 'b8': (2, 8), 'c1': (3, 1), 'd1': (4, 1), 'f5': (6, 5), 'c7': (3, 7), 'e5': (5, 5), 'd3': (4, 3), 'f8': (6, 8), 'c5': (3, 5), 'h8': (8, 8), 'c4': (3, 4), 'g7': (7, 7), 'g6': (7, 6), 'g5': (7, 5), 'g4': (7, 4), 'g3': (7, 3), 'g2': (7, 2), 'g1': (7, 1), 'g8': (7, 8), 'a1': (1, 1), 'a3': (1, 3), 'a2': (1, 2), 'a5': (1, 5), 'e8': (5, 8), 'a7': (1, 7), 'a6': (1, 6), 'c3': (3, 3), 'e4': (5, 4), 'e7': (5, 7), 'e6': (5, 6), 'e1': (5, 1), 'c6': (3, 6), 'e3': (5, 3), 'e2': (5, 2), 'b3': (2, 3), 'd2': (4, 2), 'a8': (1, 8), 'c8': (3, 8), 'a4': (1, 4)}

bmap = {
'f1':{'king': ['f2', 'g2', 'g1', 'e1', 'e2'], 'E': ['g1', 'h1'], 'knight': ['e3', 'd2', 'g3', 'h2'], 'wpawn': [], 'NE': ['g2', 'h3'], 'N': ['f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'], 'bpawn': ['g2', 'e2'], 'S': [], 'W': ['e1', 'd1', 'c1', 'b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['e2', 'd3', 'c4', 'b5', 'a6']},
'h8':{'king': ['h7', 'g7', 'g8'], 'E': [], 'knight': ['f7', 'g6'], 'wpawn': ['g7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['h7', 'h6', 'h5', 'h4', 'h3', 'h2', 'h1'], 'W': ['g8', 'f8', 'e8', 'd8', 'c8', 'b8', 'a8'], 'SW': ['g7', 'f6', 'e5', 'd4', 'c3', 'b2', 'a1'], 'SE': [], 'NW': []},
'f3':{'king': ['f4', 'g4', 'g3', 'g2', 'f2', 'e2', 'e3', 'e4'], 'E': ['g3', 'h3'], 'knight': ['e5', 'd4', 'd2', 'e1', 'g5', 'h4', 'h2', 'g1'], 'wpawn': ['g2', 'e2'], 'NE': ['g4', 'h5'], 'N': ['f4', 'f5', 'f6', 'f7', 'f8'], 'bpawn': ['g4', 'e4'], 'S': ['f2', 'f1'], 'W': ['e3', 'd3', 'c3', 'b3', 'a3'], 'SW': ['e2', 'd1'], 'SE': ['g2', 'h1'], 'NW': ['e4', 'd5', 'c6', 'b7', 'a8']},
'f4':{'king': ['f5', 'g5', 'g4', 'g3', 'f3', 'e3', 'e4', 'e5'], 'E': ['g4', 'h4'], 'knight': ['e6', 'd5', 'd3', 'e2', 'g6', 'h5', 'h3', 'g2'], 'wpawn': ['g3', 'e3'], 'NE': ['g5', 'h6'], 'N': ['f5', 'f6', 'f7', 'f8'], 'bpawn': ['g5', 'e5'], 'S': ['f3', 'f2', 'f1'], 'W': ['e4', 'd4', 'c4', 'b4', 'a4'], 'SW': ['e3', 'd2', 'c1'], 'SE': ['g3', 'h2'], 'NW': ['e5', 'd6', 'c7', 'b8']},
'f5':{'king': ['f6', 'g6', 'g5', 'g4', 'f4', 'e4', 'e5', 'e6'], 'E': ['g5', 'h5'], 'knight': ['e7', 'd6', 'd4', 'e3', 'g7', 'h6', 'h4', 'g3'], 'wpawn': ['g4', 'e4'], 'NE': ['g6', 'h7'], 'N': ['f6', 'f7', 'f8'], 'bpawn': ['g6', 'e6'], 'S': ['f4', 'f3', 'f2', 'f1'], 'W': ['e5', 'd5', 'c5', 'b5', 'a5'], 'SW': ['e4', 'd3', 'c2', 'b1'], 'SE': ['g4', 'h3'], 'NW': ['e6', 'd7', 'c8']},
'f6':{'king': ['f7', 'g7', 'g6', 'g5', 'f5', 'e5', 'e6', 'e7'], 'E': ['g6', 'h6'], 'knight': ['e8', 'd7', 'd5', 'e4', 'g8', 'h7', 'h5', 'g4'], 'wpawn': ['g5', 'e5'], 'NE': ['g7', 'h8'], 'N': ['f7', 'f8'], 'bpawn': ['g7', 'e7'], 'S': ['f5', 'f4', 'f3', 'f2', 'f1'], 'W': ['e6', 'd6', 'c6', 'b6', 'a6'], 'SW': ['e5', 'd4', 'c3', 'b2', 'a1'], 'SE': ['g5', 'h4'], 'NW': ['e7', 'd8']},
'f7':{'king': ['f8', 'g8', 'g7', 'g6', 'f6', 'e6', 'e7', 'e8'], 'E': ['g7', 'h7'], 'knight': ['d8', 'd6', 'e5', 'h8', 'h6', 'g5'], 'wpawn': ['g6', 'e6'], 'NE': ['g8'], 'N': ['f8'], 'bpawn': ['g8', 'e8'], 'S': ['f6', 'f5', 'f4', 'f3', 'f2', 'f1'], 'W': ['e7', 'd7', 'c7', 'b7', 'a7'], 'SW': ['e6', 'd5', 'c4', 'b3', 'a2'], 'SE': ['g6', 'h5'], 'NW': ['e8']},
'f8':{'king': ['g8', 'g7', 'f7', 'e7', 'e8'], 'E': ['g8', 'h8'], 'knight': ['d7', 'e6', 'h7', 'g6'], 'wpawn': ['g7', 'e7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['f7', 'f6', 'f5', 'f4', 'f3', 'f2', 'f1'], 'W': ['e8', 'd8', 'c8', 'b8', 'a8'], 'SW': ['e7', 'd6', 'c5', 'b4', 'a3'], 'SE': ['g7', 'h6'], 'NW': []},
'h3':{'king': ['h4', 'h2', 'g2', 'g3', 'g4'], 'E': [], 'knight': ['g5', 'f4', 'f2', 'g1'], 'wpawn': ['g2'], 'NE': [], 'N': ['h4', 'h5', 'h6', 'h7', 'h8'], 'bpawn': ['g4'], 'S': ['h2', 'h1'], 'W': ['g3', 'f3', 'e3', 'd3', 'c3', 'b3', 'a3'], 'SW': ['g2', 'f1'], 'SE': [], 'NW': ['g4', 'f5', 'e6', 'd7', 'c8']},
'b3':{'king': ['b4', 'c4', 'c3', 'c2', 'b2', 'a2', 'a3', 'a4'], 'E': ['c3', 'd3', 'e3', 'f3', 'g3', 'h3'], 'knight': ['a5', 'a1', 'c5', 'd4', 'd2', 'c1'], 'wpawn': ['c2', 'a2'], 'NE': ['c4', 'd5', 'e6', 'f7', 'g8'], 'N': ['b4', 'b5', 'b6', 'b7', 'b8'], 'bpawn': ['c4', 'a4'], 'S': ['b2', 'b1'], 'W': ['a3'], 'SW': ['a2'], 'SE': ['c2', 'd1'], 'NW': ['a4']},
'h6':{'king': ['h7', 'h5', 'g5', 'g6', 'g7'], 'E': [], 'knight': ['g8', 'f7', 'f5', 'g4'], 'wpawn': ['g5'], 'NE': [], 'N': ['h7', 'h8'], 'bpawn': ['g7'], 'S': ['h5', 'h4', 'h3', 'h2', 'h1'], 'W': ['g6', 'f6', 'e6', 'd6', 'c6', 'b6', 'a6'], 'SW': ['g5', 'f4', 'e3', 'd2', 'c1'], 'SE': [], 'NW': ['g7', 'f8']},
'h7':{'king': ['h8', 'h6', 'g6', 'g7', 'g8'], 'E': [], 'knight': ['f8', 'f6', 'g5'], 'wpawn': ['g6'], 'NE': [], 'N': ['h8'], 'bpawn': ['g8'], 'S': ['h6', 'h5', 'h4', 'h3', 'h2', 'h1'], 'W': ['g7', 'f7', 'e7', 'd7', 'c7', 'b7', 'a7'], 'SW': ['g6', 'f5', 'e4', 'd3', 'c2', 'b1'], 'SE': [], 'NW': ['g8']},
'h4':{'king': ['h5', 'h3', 'g3', 'g4', 'g5'], 'E': [], 'knight': ['g6', 'f5', 'f3', 'g2'], 'wpawn': ['g3'], 'NE': [], 'N': ['h5', 'h6', 'h7', 'h8'], 'bpawn': ['g5'], 'S': ['h3', 'h2', 'h1'], 'W': ['g4', 'f4', 'e4', 'd4', 'c4', 'b4', 'a4'], 'SW': ['g3', 'f2', 'e1'], 'SE': [], 'NW': ['g5', 'f6', 'e7', 'd8']},
'h5':{'king': ['h6', 'h4', 'g4', 'g5', 'g6'], 'E': [], 'knight': ['g7', 'f6', 'f4', 'g3'], 'wpawn': ['g4'], 'NE': [], 'N': ['h6', 'h7', 'h8'], 'bpawn': ['g6'], 'S': ['h4', 'h3', 'h2', 'h1'], 'W': ['g5', 'f5', 'e5', 'd5', 'c5', 'b5', 'a5'], 'SW': ['g4', 'f3', 'e2', 'd1'], 'SE': [], 'NW': ['g6', 'f7', 'e8']},
'b4':{'king': ['b5', 'c5', 'c4', 'c3', 'b3', 'a3', 'a4', 'a5'], 'E': ['c4', 'd4', 'e4', 'f4', 'g4', 'h4'], 'knight': ['a6', 'a2', 'c6', 'd5', 'd3', 'c2'], 'wpawn': ['c3', 'a3'], 'NE': ['c5', 'd6', 'e7', 'f8'], 'N': ['b5', 'b6', 'b7', 'b8'], 'bpawn': ['c5', 'a5'], 'S': ['b3', 'b2', 'b1'], 'W': ['a4'], 'SW': ['a3'], 'SE': ['c3', 'd2', 'e1'], 'NW': ['a5']},
'b5':{'king': ['b6', 'c6', 'c5', 'c4', 'b4', 'a4', 'a5', 'a6'], 'E': ['c5', 'd5', 'e5', 'f5', 'g5', 'h5'], 'knight': ['a7', 'a3', 'c7', 'd6', 'd4', 'c3'], 'wpawn': ['c4', 'a4'], 'NE': ['c6', 'd7', 'e8'], 'N': ['b6', 'b7', 'b8'], 'bpawn': ['c6', 'a6'], 'S': ['b4', 'b3', 'b2', 'b1'], 'W': ['a5'], 'SW': ['a4'], 'SE': ['c4', 'd3', 'e2', 'f1'], 'NW': ['a6']},
'b6':{'king': ['b7', 'c7', 'c6', 'c5', 'b5', 'a5', 'a6', 'a7'], 'E': ['c6', 'd6', 'e6', 'f6', 'g6', 'h6'], 'knight': ['a8', 'a4', 'c8', 'd7', 'd5', 'c4'], 'wpawn': ['c5', 'a5'], 'NE': ['c7', 'd8'], 'N': ['b7', 'b8'], 'bpawn': ['c7', 'a7'], 'S': ['b5', 'b4', 'b3', 'b2', 'b1'], 'W': ['a6'], 'SW': ['a5'], 'SE': ['c5', 'd4', 'e3', 'f2', 'g1'], 'NW': ['a7']},
'b7':{'king': ['b8', 'c8', 'c7', 'c6', 'b6', 'a6', 'a7', 'a8'], 'E': ['c7', 'd7', 'e7', 'f7', 'g7', 'h7'], 'knight': ['a5', 'd8', 'd6', 'c5'], 'wpawn': ['c6', 'a6'], 'NE': ['c8'], 'N': ['b8'], 'bpawn': ['c8', 'a8'], 'S': ['b6', 'b5', 'b4', 'b3', 'b2', 'b1'], 'W': ['a7'], 'SW': ['a6'], 'SE': ['c6', 'd5', 'e4', 'f3', 'g2', 'h1'], 'NW': ['a8']},
'b1':{'king': ['b2', 'c2', 'c1', 'a1', 'a2'], 'E': ['c1', 'd1', 'e1', 'f1', 'g1', 'h1'], 'knight': ['a3', 'c3', 'd2'], 'wpawn': [], 'NE': ['c2', 'd3', 'e4', 'f5', 'g6', 'h7'], 'N': ['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'], 'bpawn': ['c2', 'a2'], 'S': [], 'W': ['a1'], 'SW': [], 'SE': [], 'NW': ['a2']},
'd8':{'king': ['e8', 'e7', 'd7', 'c7', 'c8'], 'E': ['e8', 'f8', 'g8', 'h8'], 'knight': ['b7', 'c6', 'f7', 'e6'], 'wpawn': ['e7', 'c7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['d7', 'd6', 'd5', 'd4', 'd3', 'd2', 'd1'], 'W': ['c8', 'b8', 'a8'], 'SW': ['c7', 'b6', 'a5'], 'SE': ['e7', 'f6', 'g5', 'h4'], 'NW': []},
'e4':{'king': ['e5', 'f5', 'f4', 'f3', 'e3', 'd3', 'd4', 'd5'], 'E': ['f4', 'g4', 'h4'], 'knight': ['d6', 'c5', 'c3', 'd2', 'f6', 'g5', 'g3', 'f2'], 'wpawn': ['f3', 'd3'], 'NE': ['f5', 'g6', 'h7'], 'N': ['e5', 'e6', 'e7', 'e8'], 'bpawn': ['f5', 'd5'], 'S': ['e3', 'e2', 'e1'], 'W': ['d4', 'c4', 'b4', 'a4'], 'SW': ['d3', 'c2', 'b1'], 'SE': ['f3', 'g2', 'h1'], 'NW': ['d5', 'c6', 'b7', 'a8']},
'd6':{'king': ['d7', 'e7', 'e6', 'e5', 'd5', 'c5', 'c6', 'c7'], 'E': ['e6', 'f6', 'g6', 'h6'], 'knight': ['c8', 'b7', 'b5', 'c4', 'e8', 'f7', 'f5', 'e4'], 'wpawn': ['e5', 'c5'], 'NE': ['e7', 'f8'], 'N': ['d7', 'd8'], 'bpawn': ['e7', 'c7'], 'S': ['d5', 'd4', 'd3', 'd2', 'd1'], 'W': ['c6', 'b6', 'a6'], 'SW': ['c5', 'b4', 'a3'], 'SE': ['e5', 'f4', 'g3', 'h2'], 'NW': ['c7', 'b8']},
'd7':{'king': ['d8', 'e8', 'e7', 'e6', 'd6', 'c6', 'c7', 'c8'], 'E': ['e7', 'f7', 'g7', 'h7'], 'knight': ['b8', 'b6', 'c5', 'f8', 'f6', 'e5'], 'wpawn': ['e6', 'c6'], 'NE': ['e8'], 'N': ['d8'], 'bpawn': ['e8', 'c8'], 'S': ['d6', 'd5', 'd4', 'd3', 'd2', 'd1'], 'W': ['c7', 'b7', 'a7'], 'SW': ['c6', 'b5', 'a4'], 'SE': ['e6', 'f5', 'g4', 'h3'], 'NW': ['c8']},
'd4':{'king': ['d5', 'e5', 'e4', 'e3', 'd3', 'c3', 'c4', 'c5'], 'E': ['e4', 'f4', 'g4', 'h4'], 'knight': ['c6', 'b5', 'b3', 'c2', 'e6', 'f5', 'f3', 'e2'], 'wpawn': ['e3', 'c3'], 'NE': ['e5', 'f6', 'g7', 'h8'], 'N': ['d5', 'd6', 'd7', 'd8'], 'bpawn': ['e5', 'c5'], 'S': ['d3', 'd2', 'd1'], 'W': ['c4', 'b4', 'a4'], 'SW': ['c3', 'b2', 'a1'], 'SE': ['e3', 'f2', 'g1'], 'NW': ['c5', 'b6', 'a7']},
'd5':{'king': ['d6', 'e6', 'e5', 'e4', 'd4', 'c4', 'c5', 'c6'], 'E': ['e5', 'f5', 'g5', 'h5'], 'knight': ['c7', 'b6', 'b4', 'c3', 'e7', 'f6', 'f4', 'e3'], 'wpawn': ['e4', 'c4'], 'NE': ['e6', 'f7', 'g8'], 'N': ['d6', 'd7', 'd8'], 'bpawn': ['e6', 'c6'], 'S': ['d4', 'd3', 'd2', 'd1'], 'W': ['c5', 'b5', 'a5'], 'SW': ['c4', 'b3', 'a2'], 'SE': ['e4', 'f3', 'g2', 'h1'], 'NW': ['c6', 'b7', 'a8']},
'b8':{'king': ['c8', 'c7', 'b7', 'a7', 'a8'], 'E': ['c8', 'd8', 'e8', 'f8', 'g8', 'h8'], 'knight': ['a6', 'd7', 'c6'], 'wpawn': ['c7', 'a7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['b7', 'b6', 'b5', 'b4', 'b3', 'b2', 'b1'], 'W': ['a8'], 'SW': ['a7'], 'SE': ['c7', 'd6', 'e5', 'f4', 'g3', 'h2'], 'NW': []},
'd3':{'king': ['d4', 'e4', 'e3', 'e2', 'd2', 'c2', 'c3', 'c4'], 'E': ['e3', 'f3', 'g3', 'h3'], 'knight': ['c5', 'b4', 'b2', 'c1', 'e5', 'f4', 'f2', 'e1'], 'wpawn': ['e2', 'c2'], 'NE': ['e4', 'f5', 'g6', 'h7'], 'N': ['d4', 'd5', 'd6', 'd7', 'd8'], 'bpawn': ['e4', 'c4'], 'S': ['d2', 'd1'], 'W': ['c3', 'b3', 'a3'], 'SW': ['c2', 'b1'], 'SE': ['e2', 'f1'], 'NW': ['c4', 'b5', 'a6']},
'd1':{'king': ['d2', 'e2', 'e1', 'c1', 'c2'], 'E': ['e1', 'f1', 'g1', 'h1'], 'knight': ['c3', 'b2', 'e3', 'f2'], 'wpawn': [], 'NE': ['e2', 'f3', 'g4', 'h5'], 'N': ['d2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'], 'bpawn': ['e2', 'c2'], 'S': [], 'W': ['c1', 'b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['c2', 'b3', 'a4']},
'e1':{'king': ['e2', 'f2', 'f1', 'd1', 'd2'], 'E': ['f1', 'g1', 'h1'], 'knight': ['d3', 'c2', 'f3', 'g2'], 'wpawn': [], 'NE': ['f2', 'g3', 'h4'], 'N': ['e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'], 'bpawn': ['f2', 'd2'], 'S': [], 'W': ['d1', 'c1', 'b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['d2', 'c3', 'b4', 'a5']},
'd2':{'king': ['d3', 'e3', 'e2', 'e1', 'd1', 'c1', 'c2', 'c3'], 'E': ['e2', 'f2', 'g2', 'h2'], 'knight': ['c4', 'b3', 'b1', 'e4', 'f3', 'f1'], 'wpawn': ['e1', 'c1'], 'NE': ['e3', 'f4', 'g5', 'h6'], 'N': ['d3', 'd4', 'd5', 'd6', 'd7', 'd8'], 'bpawn': ['e3', 'c3'], 'S': ['d1'], 'W': ['c2', 'b2', 'a2'], 'SW': ['c1'], 'SE': ['e1'], 'NW': ['c3', 'b4', 'a5']},
'h2':{'king': ['h3', 'h1', 'g1', 'g2', 'g3'], 'E': [], 'knight': ['g4', 'f3', 'f1'], 'wpawn': ['g1'], 'NE': [], 'N': ['h3', 'h4', 'h5', 'h6', 'h7', 'h8'], 'bpawn': ['g3'], 'S': ['h1'], 'W': ['g2', 'f2', 'e2', 'd2', 'c2', 'b2', 'a2'], 'SW': ['g1'], 'SE': [], 'NW': ['g3', 'f4', 'e5', 'd6', 'c7', 'b8']},
'f2':{'king': ['f3', 'g3', 'g2', 'g1', 'f1', 'e1', 'e2', 'e3'], 'E': ['g2', 'h2'], 'knight': ['e4', 'd3', 'd1', 'g4', 'h3', 'h1'], 'wpawn': ['g1', 'e1'], 'NE': ['g3', 'h4'], 'N': ['f3', 'f4', 'f5', 'f6', 'f7', 'f8'], 'bpawn': ['g3', 'e3'], 'S': ['f1'], 'W': ['e2', 'd2', 'c2', 'b2', 'a2'], 'SW': ['e1'], 'SE': ['g1'], 'NW': ['e3', 'd4', 'c5', 'b6', 'a7']},
'e3':{'king': ['e4', 'f4', 'f3', 'f2', 'e2', 'd2', 'd3', 'd4'], 'E': ['f3', 'g3', 'h3'], 'knight': ['d5', 'c4', 'c2', 'd1', 'f5', 'g4', 'g2', 'f1'], 'wpawn': ['f2', 'd2'], 'NE': ['f4', 'g5', 'h6'], 'N': ['e4', 'e5', 'e6', 'e7', 'e8'], 'bpawn': ['f4', 'd4'], 'S': ['e2', 'e1'], 'W': ['d3', 'c3', 'b3', 'a3'], 'SW': ['d2', 'c1'], 'SE': ['f2', 'g1'], 'NW': ['d4', 'c5', 'b6', 'a7']},
'e2':{'king': ['e3', 'f3', 'f2', 'f1', 'e1', 'd1', 'd2', 'd3'], 'E': ['f2', 'g2', 'h2'], 'knight': ['d4', 'c3', 'c1', 'f4', 'g3', 'g1'], 'wpawn': ['f1', 'd1'], 'NE': ['f3', 'g4', 'h5'], 'N': ['e3', 'e4', 'e5', 'e6', 'e7', 'e8'], 'bpawn': ['f3', 'd3'], 'S': ['e1'], 'W': ['d2', 'c2', 'b2', 'a2'], 'SW': ['d1'], 'SE': ['f1'], 'NW': ['d3', 'c4', 'b5', 'a6']},
'g7':{'king': ['g8', 'h8', 'h7', 'h6', 'g6', 'f6', 'f7', 'f8'], 'E': ['h7'], 'knight': ['e8', 'e6', 'f5', 'h5'], 'wpawn': ['h6', 'f6'], 'NE': ['h8'], 'N': ['g8'], 'bpawn': ['h8', 'f8'], 'S': ['g6', 'g5', 'g4', 'g3', 'g2', 'g1'], 'W': ['f7', 'e7', 'd7', 'c7', 'b7', 'a7'], 'SW': ['f6', 'e5', 'd4', 'c3', 'b2', 'a1'], 'SE': ['h6'], 'NW': ['f8']},
'g6':{'king': ['g7', 'h7', 'h6', 'h5', 'g5', 'f5', 'f6', 'f7'], 'E': ['h6'], 'knight': ['f8', 'e7', 'e5', 'f4', 'h8', 'h4'], 'wpawn': ['h5', 'f5'], 'NE': ['h7'], 'N': ['g7', 'g8'], 'bpawn': ['h7', 'f7'], 'S': ['g5', 'g4', 'g3', 'g2', 'g1'], 'W': ['f6', 'e6', 'd6', 'c6', 'b6', 'a6'], 'SW': ['f5', 'e4', 'd3', 'c2', 'b1'], 'SE': ['h5'], 'NW': ['f7', 'e8']},
'g5':{'king': ['g6', 'h6', 'h5', 'h4', 'g4', 'f4', 'f5', 'f6'], 'E': ['h5'], 'knight': ['f7', 'e6', 'e4', 'f3', 'h7', 'h3'], 'wpawn': ['h4', 'f4'], 'NE': ['h6'], 'N': ['g6', 'g7', 'g8'], 'bpawn': ['h6', 'f6'], 'S': ['g4', 'g3', 'g2', 'g1'], 'W': ['f5', 'e5', 'd5', 'c5', 'b5', 'a5'], 'SW': ['f4', 'e3', 'd2', 'c1'], 'SE': ['h4'], 'NW': ['f6', 'e7', 'd8']},
'g4':{'king': ['g5', 'h5', 'h4', 'h3', 'g3', 'f3', 'f4', 'f5'], 'E': ['h4'], 'knight': ['f6', 'e5', 'e3', 'f2', 'h6', 'h2'], 'wpawn': ['h3', 'f3'], 'NE': ['h5'], 'N': ['g5', 'g6', 'g7', 'g8'], 'bpawn': ['h5', 'f5'], 'S': ['g3', 'g2', 'g1'], 'W': ['f4', 'e4', 'd4', 'c4', 'b4', 'a4'], 'SW': ['f3', 'e2', 'd1'], 'SE': ['h3'], 'NW': ['f5', 'e6', 'd7', 'c8']},
'g3':{'king': ['g4', 'h4', 'h3', 'h2', 'g2', 'f2', 'f3', 'f4'], 'E': ['h3'], 'knight': ['f5', 'e4', 'e2', 'f1', 'h5', 'h1'], 'wpawn': ['h2', 'f2'], 'NE': ['h4'], 'N': ['g4', 'g5', 'g6', 'g7', 'g8'], 'bpawn': ['h4', 'f4'], 'S': ['g2', 'g1'], 'W': ['f3', 'e3', 'd3', 'c3', 'b3', 'a3'], 'SW': ['f2', 'e1'], 'SE': ['h2'], 'NW': ['f4', 'e5', 'd6', 'c7', 'b8']},
'g2':{'king': ['g3', 'h3', 'h2', 'h1', 'g1', 'f1', 'f2', 'f3'], 'E': ['h2'], 'knight': ['f4', 'e3', 'e1', 'h4'], 'wpawn': ['h1', 'f1'], 'NE': ['h3'], 'N': ['g3', 'g4', 'g5', 'g6', 'g7', 'g8'], 'bpawn': ['h3', 'f3'], 'S': ['g1'], 'W': ['f2', 'e2', 'd2', 'c2', 'b2', 'a2'], 'SW': ['f1'], 'SE': ['h1'], 'NW': ['f3', 'e4', 'd5', 'c6', 'b7', 'a8']},
'g1':{'king': ['g2', 'h2', 'h1', 'f1', 'f2'], 'E': ['h1'], 'knight': ['f3', 'e2', 'h3'], 'wpawn': [], 'NE': ['h2'], 'N': ['g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'], 'bpawn': ['h2', 'f2'], 'S': [], 'W': ['f1', 'e1', 'd1', 'c1', 'b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['f2', 'e3', 'd4', 'c5', 'b6', 'a7']},
'h1':{'king': ['h2', 'g1', 'g2'], 'E': [], 'knight': ['g3', 'f2'], 'wpawn': [], 'NE': [], 'N': ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'], 'bpawn': ['g2'], 'S': [], 'W': ['g1', 'f1', 'e1', 'd1', 'c1', 'b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['g2', 'f3', 'e4', 'd5', 'c6', 'b7', 'a8']},
'b2':{'king': ['b3', 'c3', 'c2', 'c1', 'b1', 'a1', 'a2', 'a3'], 'E': ['c2', 'd2', 'e2', 'f2', 'g2', 'h2'], 'knight': ['a4', 'c4', 'd3', 'd1'], 'wpawn': ['c1', 'a1'], 'NE': ['c3', 'd4', 'e5', 'f6', 'g7', 'h8'], 'N': ['b3', 'b4', 'b5', 'b6', 'b7', 'b8'], 'bpawn': ['c3', 'a3'], 'S': ['b1'], 'W': ['a2'], 'SW': ['a1'], 'SE': ['c1'], 'NW': ['a3']},
'g8':{'king': ['h8', 'h7', 'g7', 'f7', 'f8'], 'E': ['h8'], 'knight': ['e7', 'f6', 'h6'], 'wpawn': ['h7', 'f7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['g7', 'g6', 'g5', 'g4', 'g3', 'g2', 'g1'], 'W': ['f8', 'e8', 'd8', 'c8', 'b8', 'a8'], 'SW': ['f7', 'e6', 'd5', 'c4', 'b3', 'a2'], 'SE': ['h7'], 'NW': []},
'a1':{'king': ['a2', 'b2', 'b1'], 'E': ['b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'], 'knight': ['b3', 'c2'], 'wpawn': [], 'NE': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'], 'N': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'], 'bpawn': ['b2'], 'S': [], 'W': [], 'SW': [], 'SE': [], 'NW': []},
'a3':{'king': ['a4', 'b4', 'b3', 'b2', 'a2'], 'E': ['b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'], 'knight': ['b5', 'c4', 'c2', 'b1'], 'wpawn': ['b2'], 'NE': ['b4', 'c5', 'd6', 'e7', 'f8'], 'N': ['a4', 'a5', 'a6', 'a7', 'a8'], 'bpawn': ['b4'], 'S': ['a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b2', 'c1'], 'NW': []},
'c8':{'king': ['d8', 'd7', 'c7', 'b7', 'b8'], 'E': ['d8', 'e8', 'f8', 'g8', 'h8'], 'knight': ['a7', 'b6', 'e7', 'd6'], 'wpawn': ['d7', 'b7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['c7', 'c6', 'c5', 'c4', 'c3', 'c2', 'c1'], 'W': ['b8', 'a8'], 'SW': ['b7', 'a6'], 'SE': ['d7', 'e6', 'f5', 'g4', 'h3'], 'NW': []},
'a5':{'king': ['a6', 'b6', 'b5', 'b4', 'a4'], 'E': ['b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'], 'knight': ['b7', 'c6', 'c4', 'b3'], 'wpawn': ['b4'], 'NE': ['b6', 'c7', 'd8'], 'N': ['a6', 'a7', 'a8'], 'bpawn': ['b6'], 'S': ['a4', 'a3', 'a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b4', 'c3', 'd2', 'e1'], 'NW': []},
'e8':{'king': ['f8', 'f7', 'e7', 'd7', 'd8'], 'E': ['f8', 'g8', 'h8'], 'knight': ['c7', 'd6', 'g7', 'f6'], 'wpawn': ['f7', 'd7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['e7', 'e6', 'e5', 'e4', 'e3', 'e2', 'e1'], 'W': ['d8', 'c8', 'b8', 'a8'], 'SW': ['d7', 'c6', 'b5', 'a4'], 'SE': ['f7', 'g6', 'h5'], 'NW': []},
'a7':{'king': ['a8', 'b8', 'b7', 'b6', 'a6'], 'E': ['b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'], 'knight': ['c8', 'c6', 'b5'], 'wpawn': ['b6'], 'NE': ['b8'], 'N': ['a8'], 'bpawn': ['b8'], 'S': ['a6', 'a5', 'a4', 'a3', 'a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b6', 'c5', 'd4', 'e3', 'f2', 'g1'], 'NW': []},
'a6':{'king': ['a7', 'b7', 'b6', 'b5', 'a5'], 'E': ['b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'], 'knight': ['b8', 'c7', 'c5', 'b4'], 'wpawn': ['b5'], 'NE': ['b7', 'c8'], 'N': ['a7', 'a8'], 'bpawn': ['b7'], 'S': ['a5', 'a4', 'a3', 'a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b5', 'c4', 'd3', 'e2', 'f1'], 'NW': []},
'e5':{'king': ['e6', 'f6', 'f5', 'f4', 'e4', 'd4', 'd5', 'd6'], 'E': ['f5', 'g5', 'h5'], 'knight': ['d7', 'c6', 'c4', 'd3', 'f7', 'g6', 'g4', 'f3'], 'wpawn': ['f4', 'd4'], 'NE': ['f6', 'g7', 'h8'], 'N': ['e6', 'e7', 'e8'], 'bpawn': ['f6', 'd6'], 'S': ['e4', 'e3', 'e2', 'e1'], 'W': ['d5', 'c5', 'b5', 'a5'], 'SW': ['d4', 'c3', 'b2', 'a1'], 'SE': ['f4', 'g3', 'h2'], 'NW': ['d6', 'c7', 'b8']},
'a8':{'king': ['b8', 'b7', 'a7'], 'E': ['b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'], 'knight': ['c7', 'b6'], 'wpawn': ['b7'], 'NE': [], 'N': [], 'bpawn': [], 'S': ['a7', 'a6', 'a5', 'a4', 'a3', 'a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'], 'NW': []},
'e7':{'king': ['e8', 'f8', 'f7', 'f6', 'e6', 'd6', 'd7', 'd8'], 'E': ['f7', 'g7', 'h7'], 'knight': ['c8', 'c6', 'd5', 'g8', 'g6', 'f5'], 'wpawn': ['f6', 'd6'], 'NE': ['f8'], 'N': ['e8'], 'bpawn': ['f8', 'd8'], 'S': ['e6', 'e5', 'e4', 'e3', 'e2', 'e1'], 'W': ['d7', 'c7', 'b7', 'a7'], 'SW': ['d6', 'c5', 'b4', 'a3'], 'SE': ['f6', 'g5', 'h4'], 'NW': ['d8']},
'e6':{'king': ['e7', 'f7', 'f6', 'f5', 'e5', 'd5', 'd6', 'd7'], 'E': ['f6', 'g6', 'h6'], 'knight': ['d8', 'c7', 'c5', 'd4', 'f8', 'g7', 'g5', 'f4'], 'wpawn': ['f5', 'd5'], 'NE': ['f7', 'g8'], 'N': ['e7', 'e8'], 'bpawn': ['f7', 'd7'], 'S': ['e5', 'e4', 'e3', 'e2', 'e1'], 'W': ['d6', 'c6', 'b6', 'a6'], 'SW': ['d5', 'c4', 'b3', 'a2'], 'SE': ['f5', 'g4', 'h3'], 'NW': ['d7', 'c8']},
'c7':{'king': ['c8', 'd8', 'd7', 'd6', 'c6', 'b6', 'b7', 'b8'], 'E': ['d7', 'e7', 'f7', 'g7', 'h7'], 'knight': ['a8', 'a6', 'b5', 'e8', 'e6', 'd5'], 'wpawn': ['d6', 'b6'], 'NE': ['d8'], 'N': ['c8'], 'bpawn': ['d8', 'b8'], 'S': ['c6', 'c5', 'c4', 'c3', 'c2', 'c1'], 'W': ['b7', 'a7'], 'SW': ['b6', 'a5'], 'SE': ['d6', 'e5', 'f4', 'g3', 'h2'], 'NW': ['b8']},
'c6':{'king': ['c7', 'd7', 'd6', 'd5', 'c5', 'b5', 'b6', 'b7'], 'E': ['d6', 'e6', 'f6', 'g6', 'h6'], 'knight': ['b8', 'a7', 'a5', 'b4', 'd8', 'e7', 'e5', 'd4'], 'wpawn': ['d5', 'b5'], 'NE': ['d7', 'e8'], 'N': ['c7', 'c8'], 'bpawn': ['d7', 'b7'], 'S': ['c5', 'c4', 'c3', 'c2', 'c1'], 'W': ['b6', 'a6'], 'SW': ['b5', 'a4'], 'SE': ['d5', 'e4', 'f3', 'g2', 'h1'], 'NW': ['b7', 'a8']},
'c5':{'king': ['c6', 'd6', 'd5', 'd4', 'c4', 'b4', 'b5', 'b6'], 'E': ['d5', 'e5', 'f5', 'g5', 'h5'], 'knight': ['b7', 'a6', 'a4', 'b3', 'd7', 'e6', 'e4', 'd3'], 'wpawn': ['d4', 'b4'], 'NE': ['d6', 'e7', 'f8'], 'N': ['c6', 'c7', 'c8'], 'bpawn': ['d6', 'b6'], 'S': ['c4', 'c3', 'c2', 'c1'], 'W': ['b5', 'a5'], 'SW': ['b4', 'a3'], 'SE': ['d4', 'e3', 'f2', 'g1'], 'NW': ['b6', 'a7']},
'c4':{'king': ['c5', 'd5', 'd4', 'd3', 'c3', 'b3', 'b4', 'b5'], 'E': ['d4', 'e4', 'f4', 'g4', 'h4'], 'knight': ['b6', 'a5', 'a3', 'b2', 'd6', 'e5', 'e3', 'd2'], 'wpawn': ['d3', 'b3'], 'NE': ['d5', 'e6', 'f7', 'g8'], 'N': ['c5', 'c6', 'c7', 'c8'], 'bpawn': ['d5', 'b5'], 'S': ['c3', 'c2', 'c1'], 'W': ['b4', 'a4'], 'SW': ['b3', 'a2'], 'SE': ['d3', 'e2', 'f1'], 'NW': ['b5', 'a6']},
'c3':{'king': ['c4', 'd4', 'd3', 'd2', 'c2', 'b2', 'b3', 'b4'], 'E': ['d3', 'e3', 'f3', 'g3', 'h3'], 'knight': ['b5', 'a4', 'a2', 'b1', 'd5', 'e4', 'e2', 'd1'], 'wpawn': ['d2', 'b2'], 'NE': ['d4', 'e5', 'f6', 'g7', 'h8'], 'N': ['c4', 'c5', 'c6', 'c7', 'c8'], 'bpawn': ['d4', 'b4'], 'S': ['c2', 'c1'], 'W': ['b3', 'a3'], 'SW': ['b2', 'a1'], 'SE': ['d2', 'e1'], 'NW': ['b4', 'a5']},
'a2':{'king': ['a3', 'b3', 'b2', 'b1', 'a1'], 'E': ['b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'], 'knight': ['b4', 'c3', 'c1'], 'wpawn': ['b1'], 'NE': ['b3', 'c4', 'd5', 'e6', 'f7', 'g8'], 'N': ['a3', 'a4', 'a5', 'a6', 'a7', 'a8'], 'bpawn': ['b3'], 'S': ['a1'], 'W': [], 'SW': [], 'SE': ['b1'], 'NW': []},
'c1':{'king': ['c2', 'd2', 'd1', 'b1', 'b2'], 'E': ['d1', 'e1', 'f1', 'g1', 'h1'], 'knight': ['b3', 'a2', 'd3', 'e2'], 'wpawn': [], 'NE': ['d2', 'e3', 'f4', 'g5', 'h6'], 'N': ['c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], 'bpawn': ['d2', 'b2'], 'S': [], 'W': ['b1', 'a1'], 'SW': [], 'SE': [], 'NW': ['b2', 'a3']},
'c2':{'king': ['c3', 'd3', 'd2', 'd1', 'c1', 'b1', 'b2', 'b3'], 'E': ['d2', 'e2', 'f2', 'g2', 'h2'], 'knight': ['b4', 'a3', 'a1', 'd4', 'e3', 'e1'], 'wpawn': ['d1', 'b1'], 'NE': ['d3', 'e4', 'f5', 'g6', 'h7'], 'N': ['c3', 'c4', 'c5', 'c6', 'c7', 'c8'], 'bpawn': ['d3', 'b3'], 'S': ['c1'], 'W': ['b2', 'a2'], 'SW': ['b1'], 'SE': ['d1'], 'NW': ['b3', 'a4']},
'a4':{'king': ['a5', 'b5', 'b4', 'b3', 'a3'], 'E': ['b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'], 'knight': ['b6', 'c5', 'c3', 'b2'], 'wpawn': ['b3'], 'NE': ['b5', 'c6', 'd7', 'e8'], 'N': ['a5', 'a6', 'a7', 'a8'], 'bpawn': ['b5'], 'S': ['a3', 'a2', 'a1'], 'W': [], 'SW': [], 'SE': ['b3', 'c2', 'd1'], 'NW': []},}

def sq2pos(sq):
    x = ord(sq[0])-96
    y = int(sq[1:])
    return x,y

def p2s(xy):
    x,y=xy
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)

def p2s2(xy):
    try:
        return p2s2d[xy]
    except KeyError:
        return 'n/a'

class MoveException(Exception):
    def __init__(self, *args):
        # *args is used to get a list of the parameters passed in
        self.args = [a for a in args]

class board():
    def __init__(self,board_state='',winch=False,binch=False):
        self.whites = []
        self.blacks = []
        self.backtrack = []
        self.wk = ''
        self.bk = ''
        self.winch = False
        self.binch = False
        if board_state == '':
            self.board = emptyboardinit.copy()
        else:
            self.piecefy(board_state)
            self.winch = self.sq_in_check(self.wk,'b')
            self.binch = self.sq_in_check(self.bk,'w')

    def initialset(self):
        self.piecefy(plainboardinit)

    def piecefy(self,board_state):
        self.board = board_state.copy()
        self.whites = []
        self.blacks = []
        for sq in self.board:
            if self.board[sq]!='  ':
                if self.board[sq][0]=='w':
                    self.whites.append(piece(self.board[sq][0],self.board[sq][1],sq))
                    if self.board[sq][1]=='k':
                        self.wk = sq
                else:
                    self.blacks.append(piece(self.board[sq][0],self.board[sq][1],sq))
                    if self.board[sq][1]=='k':
                        self.bk = sq

    def fullset(self):
        return self.whites+self.blacks

    def hashit(self,board_state=''):
        if board_state == '':
            return self.board["a1"]+self.board["a2"]+self.board["a3"]+self.board["a4"]+self.board["a5"]+self.board["a6"]+self.board["a7"]+self.board["a8"]+self.board["b1"]+self.board["b2"]+self.board["b3"]+self.board["b4"]+self.board["b5"]+self.board["b6"]+self.board["b7"]+self.board["b8"]+self.board["c1"]+self.board["c2"]+self.board["c3"]+self.board["c4"]+self.board["c5"]+self.board["c6"]+self.board["c7"]+self.board["c8"]+self.board["d1"]+self.board["d2"]+self.board["d3"]+self.board["d4"]+self.board["d5"]+self.board["d6"]+self.board["d7"]+self.board["d8"]+self.board["e1"]+self.board["e2"]+self.board["e3"]+self.board["e4"]+self.board["e5"]+self.board["e6"]+self.board["e7"]+self.board["e8"]+self.board["f1"]+self.board["f2"]+self.board["f3"]+self.board["f4"]+self.board["f5"]+self.board["f6"]+self.board["f7"]+self.board["f8"]+self.board["g1"]+self.board["g2"]+self.board["g3"]+self.board["g4"]+self.board["g5"]+self.board["g6"]+self.board["g7"]+self.board["g8"]+self.board["h1"]+self.board["h2"]+self.board["h3"]+self.board["h4"]+self.board["h5"]+self.board["h6"]+self.board["h7"]+self.board["h8"]
        else:
            return board_state["a1"]+board_state["a2"]+board_state["a3"]+board_state["a4"]+board_state["a5"]+board_state["a6"]+board_state["a7"]+board_state["a8"]+board_state["b1"]+board_state["b2"]+board_state["b3"]+board_state["b4"]+board_state["b5"]+board_state["b6"]+board_state["b7"]+board_state["b8"]+board_state["c1"]+board_state["c2"]+board_state["c3"]+board_state["c4"]+board_state["c5"]+board_state["c6"]+board_state["c7"]+board_state["c8"]+board_state["d1"]+board_state["d2"]+board_state["d3"]+board_state["d4"]+board_state["d5"]+board_state["d6"]+board_state["d7"]+board_state["d8"]+board_state["e1"]+board_state["e2"]+board_state["e3"]+board_state["e4"]+board_state["e5"]+board_state["e6"]+board_state["e7"]+board_state["e8"]+board_state["f1"]+board_state["f2"]+board_state["f3"]+board_state["f4"]+board_state["f5"]+board_state["f6"]+board_state["f7"]+board_state["f8"]+board_state["g1"]+board_state["g2"]+board_state["g3"]+board_state["g4"]+board_state["g5"]+board_state["g6"]+board_state["g7"]+board_state["g8"]+board_state["h1"]+board_state["h2"]+board_state["h3"]+board_state["h4"]+board_state["h5"]+board_state["h6"]+board_state["h7"]+board_state["h8"]

    def show(self,board_state=''):
        rez = ''
        if board_state == '':
            board_state = self.board

        for i in range(8,0,-1):
            rez+='|'
            for j in range(97,105):
                rez+=board_state[chr(j)+str(i)]+'|'
            rez+='\n'# -- -- -- -- -- -- -- --\n'

        return rez

    def piece_by_sq(self,sq,verbose=0):
        for p in self.fullset():
            if verbose >0: print(p,p.sq==sq)
            if p.sq == sq:
                return p

        return None

    def relocate(self,piece_or_sq,tosq,verbose=0): # more in the meaning of relocate piece P (piece at SQ) to an empty square TOSQ
        if type(piece_or_sq) == str:
            piece = self.piece_by_sq(piece_or_sq)
            orriginal_sq = piece_or_sq # will be needed to remove the piece from that sq
        else:
            piece = piece_or_sq
            orriginal_sq = piece.sq # will be needed to remove the piece from that sq

        if self.piece_by_sq(tosq) != None:
            msg = 'Are you blind - there is another piece at that spot: '+repr(self.piece_by_sq(tosq))
            if verbose>0:
                print msg+'\n'+'>>> board\n'+self.show()
                print '>>> piece',piece
                print '>>> orriginal_sq',orriginal_sq
                print '>>> to sq',tosq
            raise MoveException(msg)

        if piece == None:
            msg = 'Trying to move the air at '+piece_or_sq
            raise MoveException(msg)
        
        if verbose>0:
            print '>>> board\n'+self.show()
            print '>>> piece',piece
            print '>>> orriginal_sq',orriginal_sq
            print '>>> to sq',tosq

        piece.sq = tosq
        piece.x = ord(piece.sq[0])-96
        piece.y = int(piece.sq[1])

        #the following code covers for the boardify:
        self.board[tosq]=piece.col+piece.type
        self.board[orriginal_sq]='  '

    def take(self,piece_or_sq):
        if type(piece_or_sq) == str:
            piece = self.piece_by_sq(piece_or_sq)
        else:
            piece = piece_or_sq

        if piece == None:
            msg = 'Trying to move the air at '+piece_or_sq
            print self.show()
            raise MoveException(msg)

        #the following code covers for the boardify:
        self.board[piece.sq]='  '
        
        if piece.col == 'w':
            self.whites.remove(piece)
        else:
            self.blacks.remove(piece)

    def add(self,col,tip='',piece_or_sq=''):
        if type(piece_or_sq) == str:
            sq = piece_or_sq
            if tip=='' and sq=='': # reads convention wq@g8
                sq = col[-2:]
                tip = col[1]
                col = col[0]

            if self.piece_by_sq(sq) != None:
                msg = 'Are you blind - there is another piece at that spot: '+repr(self.piece_by_sq(tosq))
                raise MoveException(msg)

            p = piece(col,tip,sq)

        else: # piece_or_sq referrs to piece object
            p = piece_or_sq # reuse piece that has been taken off the board
            col= p.col
        
        if col == 'w':
            self.whites.append(p)
        else:
            self.blacks.append(p)

        #the following code covers for the boardify:
        self.board[p.sq]=p.col+p.type

    def prep_move(self,piece,exp,verbose=0):#,virtual=False):
        # determines board action for given move
        actions=[]
        undo=[]
        if exp[0]=='m':
            actions.append(['reloc',piece,exp[1]])
            undo.append(['reloc',exp[1],piece.sq])
        elif exp[0]=='t':
            taken = self.piece_by_sq(exp[1])
            actions.append(['take',exp[1]])
            actions.append(['reloc',piece,exp[1]])
            undo.append(['reloc',exp[1],piece.sq])
            undo.append(['add',None,None,taken])
        elif exp[0]=='e':
            taken = self.piece_by_sq(exp[1][0]+piece.sq[1])
            actions.append(['take',exp[1][0]+piece.sq[1]])
            actions.append(['reloc',piece,exp[1]])
            undo.append(['reloc',exp[1],piece.sq])
            undo.append(['add',None,None,taken])
        elif exp[0]=='p':
            actions.append(['add',piece.col,exp[2][-1].lower(),exp[1]])
            actions.append(['take',piece])
            undo.append(['add',None,None,piece])
            undo.append(['take',exp[1]])
        elif exp[0]=='+':
            taken = self.piece_by_sq(exp[1])
            actions.append(['take',exp[1]])
            actions.append(['add',piece.col,exp[2][-1].lower(),exp[1]])
            actions.append(['take',piece])
            undo.append(['add',None,None,piece])
            undo.append(['take',exp[1]])
            undo.append(['add',None,None,taken])
        elif exp[0]=='c':
            if exp[2]=='O-O':
                actions.append(['reloc','h'+piece.sq[1], 'f'+piece.sq[1]])
                actions.append(['reloc',piece, exp[1]])
                undo.append(['reloc',exp[1],piece.sq])
                undo.append(['reloc','f'+piece.sq[1],'h'+piece.sq[1]])
            else: #O-O-O
                actions.append(['reloc','a'+piece.sq[1], 'd'+piece.sq[1]])
                actions.append(['reloc',piece, exp[1]])
                undo.append(['reloc',exp[1],piece.sq])
                undo.append(['reloc','d'+piece.sq[1],'a'+piece.sq[1]])

        return actions,undo
        
    def do_actions(self,actions,verbose=0):
        for a in actions:
            if a[0]=='reloc':
                self.relocate(a[1],a[2])
            elif a[0]=='take':
                self.take(a[1])
            elif a[0]=='add':
                self.add(a[1],a[2],a[3])
            elif a[0]=='data':
                self.wk = a[1]
                self.bk = a[2]
                self.winch = a[3]
                self.binch = a[4]

    def undo_move(self,actions,verbose=0):
        self.do_actions(actions,verbose)
        self.backtrack.pop() # this is used to check on stalemate by repetition

    def exec_move(self,piece,exp,verbose=0):#,virtual=False):
        # the function that applies actions to the piece set (and thus the board)
        if verbose>0:
            print 'piece',piece
            print 'exp',exp
        actions, undo = self.prep_move(piece,exp,verbose)
        origin_sq=piece.sq
        if verbose>0:
            print 'actions',actions
        self.do_actions(actions,verbose)

        #invalidation
        if piece.type == 'k' or self.winch or self.binch: #this are the old values of winch & binch
            is_valid = self.validate_all_moves(piece,exp,verbose)
        else:
            is_valid = self.validate_move(piece,origin_sq,verbose)
            
        if verbose>0:
            print 'is_valid',is_valid
        if not is_valid:
            self.do_actions(undo,verbose)
            return None
        # --- end of invalidation ---

        self.backtrack.append(self.hashit()) # this is used to check on stalemate by repetition
        undo.append(['data',self.wk,self.bk,self.winch,self.binch,])
        if piece.col == 'w':
            self.binch = self.sq_in_check(self.bk,piece.col,'',verbose)
            if piece.type == 'k':
                self.wk = exp[1]
        else:
            if piece.type == 'k':
                self.bk = exp[1]
            self.winch = self.sq_in_check(self.wk,piece.col,'',verbose)
        
        return undo

    def virt_move(self,piece,exp,verbose=0):#,virtual=False):
        # the function returns board state with applied given expansion EXP to the board
        
        if verbose>0:
            print(']]]',piece,exp)
        new_state=self.board.copy()

        if exp[0]=='m':
            if new_state[exp[1]]!='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            #new_state = mv(new_state,piece.sq,exp[1])
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='t':
            if new_state[exp[1]]=='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='e':
            if new_state[exp[1]]!='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            new_state[exp[1][0]+piece.sq[1]]= '  '  #exp[1][0] is the file of the pawn being taken, piece.sq[1] is the rank of the pawn executing the e.p. before the move
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='p':
            if new_state[exp[1]]!='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            new_state[exp[1]] = piece.col+exp[2][-1].lower()
            new_state[piece.sq] = '  '
        elif exp[0]=='+':
            if new_state[exp[1]]=='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            new_state[exp[1]] = piece.col+exp[2][-1].lower()
            new_state[piece.sq] = '  '
        elif exp[0]=='c':
            if new_state[exp[1]]!='  ': raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
            if exp[2].count('O')==2: #O-O # not exact matching, to avoid 'O-O!'
                new_state[exp[1]] = piece.col+piece.type
                new_state[piece.sq] = '  '
                new_state['h'+piece.sq[1]]='  '
                new_state['f'+piece.sq[1]]=piece.col+'r'
            else: #O-O-O
                new_state[exp[1]] = piece.col+piece.type
                new_state[piece.sq] = '  '
                new_state['a'+piece.sq[1]]='  '
                new_state['d'+piece.sq[1]]=piece.col+'r'

        if verbose > 0:
            print(self.show(new_state))

        if piece.type == 'k':
            if piece.col == 'w':
                wksq = exp[1]
                bksq = self.bk
            else:
                wksq = self.wk
                bksq = exp[1]
        else:
            wksq = self.wk
            bksq = self.bk

        return new_state,wksq,bksq

    def validate_move(self,piece,origin_sq,verbose=0):
        # only validates against position, cannot reject moves based on history conditions
        if piece.col == 'w':
            opposite_col = 'b'
            ksq = self.wk
        else:
            opposite_col = 'w'
            ksq = self.bk

        is_in_check = self.discover_check(ksq,opposite_col,origin_sq)

        if verbose > 0:
            print 'origin_sq',origin_sq
            print 'checking check against',ksq, self.piece_by_sq(ksq)
            print('is_in_check',is_in_check)

        return not is_in_check # False == invalid move

    def validate_all_moves(self,piece,move,verbose=0):
        # only validates against position, cannot reject moves based on history conditions
        if piece.col == 'w':
            opposite_col = 'b'
            castle_row = '1'
            ksq = self.wk
        else:
            opposite_col = 'w'
            castle_row = '8'
            ksq = self.bk

        if verbose>0:
            print 'opp col',opposite_col,'ksq',ksq

        if piece.type=='k':
            is_in_check = self.sq_in_check(move[1],opposite_col) # use ksq to get the original position
            if move[0]=='c':
                is_in_check = is_in_check or self.sq_in_check(ksq,opposite_col) # the current sq
                if move[2].count('O')==2:
                    ksq='f'+castle_row
                if move[2].count('O')==3:
                    ksq='d'+castle_row
                is_in_check = is_in_check or self.sq_in_check(ksq,opposite_col) # jump-over sq
        else:
            is_in_check = self.sq_in_check(ksq,opposite_col)  

        if verbose > 0:
            print 'move',move
            print 'checking check against',ksq
            print('is_in_check',is_in_check)

        return not is_in_check # False == invalid move

    #===============================================================================================================

    def old_validate_move(self,piece,move,verbose=0):
        # only validates against position, cannot reject moves based on history conditions
        state_tobe_checked,wksq,bksq = self.virt_move(piece,move,verbose)
        if piece.col == 'w':
            opposite_col = 'b'
            ksq = wksq
        else:
            opposite_col = 'w'
            ksq = bksq

        is_in_check = self.discover_check(ksq,opposite_col,piece.sq,state_tobe_checked,verbose)

        if verbose > 0:
            print 'move',move
            print 'checking check against',ksq
            print('is_in_check',is_in_check)

        return not is_in_check # False == invalid move

    def old_validate_all_moves(self,piece,move,verbose=0):
        # only validates against position, cannot reject moves based on history conditions
        state_tobe_checked,wksq,bksq = self.virt_move(piece,move,verbose)
        if piece.col == 'w':
            opposite_col = 'b'
            castle_row = '1'
            ksq = wksq
        else:
            opposite_col = 'w'
            castle_row = '8'
            ksq = bksq

        if verbose>0:
            print 'opp col',opposite_col,'ksq',ksq

        if piece.type=='k':
            is_in_check = self.sq_in_check(move[1],opposite_col,state_tobe_checked,verbose)  # the destination sq
            if move[0]=='c':
                is_in_check = is_in_check or self.sq_in_check(piece.sq,opposite_col,state_tobe_checked,verbose) # the current sq
                if move[2].count('O')==2:
                    ksq='f'+castle_row
                if move[2].count('O')==3:
                    ksq='d'+castle_row
                is_in_check = is_in_check or self.sq_in_check(ksq,opposite_col,state_tobe_checked,verbose) # jump-over sq
        else:
            is_in_check = self.sq_in_check(ksq,opposite_col,state_tobe_checked,verbose)  # the destination sq

        if verbose > 0:
            print 'move',move
            print 'checking check against',ksq
            print('is_in_check',is_in_check)

        return not is_in_check # False == invalid move

    def sq_in_check(self,sq,by_col,b_state='',verbose=0):
        if verbose >0:
            print 30*'[]'+sq+'|'+by_col
        if 1==0 and sq=='e8' and by_col=='w':
            print '\n---------------'
            print 'sq',sq,'by col',by_col
            verbose = 1
        else:
            verbose = 0

        if b_state=='':
            board_state = self.board
        else:
            board_state = b_state

        rez = False
        if sq=='':
            print self.show(board_state)
            print 'sq',sq, 'by',by_col

        for dsq in bmap[sq]['knight']:
            if board_state[dsq] == by_col+'n':
                return True

        if by_col == 'w':
            for dsq in bmap[sq]['wpawn']:
                if board_state[dsq] == 'wp':
                    return True

        else: #by_col == 'b':
            for dsq in bmap[sq]['bpawn']:
                if board_state[dsq] == 'bp':
                    return True
                    
        for dsq in bmap[sq]['king']:
            if board_state[dsq] == by_col+'k':
                return True

        for d in ['N','E','S','W']:
            for i in range(len(bmap[sq][d])):
                dsq = bmap[sq][d][i]
                if verbose>0:
                    print i,')','dsq',dsq,'board_state[dsq]',board_state[dsq]
                if board_state[dsq] != '  ':
                    if board_state[dsq] == by_col+'q' or board_state[dsq] == by_col+'r':
                        return True # relevant displacement operator at distance i
                    break # the direction is blocked if an enemy piece doesnt operate in that direction or own piece
                    
        for d in ['NE','SE','SW','NW']:
            for i in range(len(bmap[sq][d])):
                dsq = bmap[sq][d][i]
                if board_state[dsq] != '  ':
                    if board_state[dsq] == by_col+'q' or board_state[dsq] == by_col+'b':
                        return True # relevant displacement operator at distance i
                    break # the direction is blocked if an enemy piece doesnt operate in that direction or own piece

        return False

    def discover_check(self,ksq,by_col,msq,board_state='',verbose=0): # msq = move sq
        # checks specific file,rank or diagonal for a threath
        if verbose>0: print '--- discover_check(king square:',ksq,'by col:',by_col,'move sq:',msq, 'verbose:',verbose,') -----------'
        if board_state == '':
            board_state = self.board
            
        kx,ky = s2p[ksq]
        mx,my = s2p[msq]
        dx=kx-mx
        dy=ky-my
        if verbose>0: print ksq,msq,kx,ky,mx,my,dx,dy
        zdir=''
        if dx == 0:
            if dy>0:
                zdir = 'S'
            else:
                zdir = 'N'
        if dy == 0:
            if dx >0:
                zdir = 'W'
            else:
                zdir = 'E'
        if dx==dy:
            if dx>0:
                zdir='SW'
            else:
                zdir='NE'
        if dx==-dy:
            if dx>0:
                zdir='NW'
            else:
                zdir='SE'

        if verbose>0: print 'zdir',zdir
        if zdir=='':
            return False

        if zdir in ['N','E','S','W']: # have to use list, because >> SW in NESW == True
            actuator = 'r'
        else:
            actuator = 'b'

        if verbose>0: print 'actuator:',actuator
        for i in range(len(bmap[ksq][zdir])):
            dsq = bmap[ksq][zdir][i]
            if verbose>0:
                print 'dsq',dsq, board_state[dsq]
            if board_state[dsq] != '  ':
                #if verbose>0:
                #    print 'checking',board_state[dsq],'==', by_col+'q',' or ',board_state[dsq],'==', by_col+actuator
                if board_state[dsq] == by_col+'q' or board_state[dsq] == by_col+actuator:
                    if verbose>0: print '--- discover_check returns TRUE -----------'
                    return True # relevant displacement operator at distance i
                break # the direction is blocked if an enemy piece doesnt operate in that direction or own piece

        if verbose>0: print '--- discover_check returns FALSE -----------'
        return False

    def valids(self,piece, verbose=0):
        # return list of hist independant valid moves for given piece
        expansions = piece.expand(self.board) # these are from the dict + basic check of move rules
        if piece.type == 'k' or self.winch or self.binch:
            val_func = self.old_validate_all_moves
            if verbose>0:
                print 'func',val_func
        else:
            val_func = self.old_validate_move
        
        if verbose>0:
            print(self.show())
            print('unreduced expansions:',expansions)
        
        return [z for z in expansions if val_func(piece,z,verbose)]
