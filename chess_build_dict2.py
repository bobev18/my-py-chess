capture_sign = 'x'

sqs = { 'a8':0.01, 'b8':0.01, 'c8':0.01, 'd8':0.01, 'e8':0.01, 'f8':0.01, 'g8':0.01, 'h8':0.01,
        'a7':0.01, 'b7':0.02, 'c7':0.02, 'd7':0.02, 'e7':0.02, 'f7':0.02, 'g7':0.02, 'h7':0.01,
        'a6':0.01, 'b6':0.02, 'c6':0.03, 'd6':0.03, 'e6':0.03, 'f6':0.03, 'g6':0.02, 'h6':0.01,
        'a5':0.01, 'b5':0.02, 'c5':0.03, 'd5':0.04, 'e5':0.04, 'f5':0.03, 'g5':0.02, 'h5':0.01,
        'a4':0.01, 'b4':0.02, 'c4':0.03, 'd4':0.04, 'e4':0.04, 'f4':0.03, 'g4':0.02, 'h4':0.01,
        'a3':0.01, 'b3':0.02, 'c3':0.03, 'd3':0.03, 'e3':0.03, 'f3':0.03, 'g3':0.02, 'h3':0.01,
        'a2':0.01, 'b2':0.02, 'c2':0.02, 'd2':0.02, 'e2':0.02, 'f2':0.02, 'g2':0.02, 'h2':0.01,
        'a1':0.01, 'b1':0.01, 'c1':0.01, 'd1':0.01, 'e1':0.01, 'f1':0.01, 'g1':0.01, 'h1':0.01,}

p2s2d = {(1,1):"a1",(1,2):"a2",(1,3):"a3",(1,4):"a4",(1,5):"a5",(1,6):"a6",(1,7):"a7",(1,8):"a8",
        (2,1):"b1",(2,2):"b2",(2,3):"b3",(2,4):"b4",(2,5):"b5",(2,6):"b6",(2,7):"b7",(2,8):"b8",
        (3,1):"c1",(3,2):"c2",(3,3):"c3",(3,4):"c4",(3,5):"c5",(3,6):"c6",(3,7):"c7",(3,8):"c8",
        (4,1):"d1",(4,2):"d2",(4,3):"d3",(4,4):"d4",(4,5):"d5",(4,6):"d6",(4,7):"d7",(4,8):"d8",
        (5,1):"e1",(5,2):"e2",(5,3):"e3",(5,4):"e4",(5,5):"e5",(5,6):"e6",(5,7):"e7",(5,8):"e8",
        (6,1):"f1",(6,2):"f2",(6,3):"f3",(6,4):"f4",(6,5):"f5",(6,6):"f6",(6,7):"f7",(6,8):"f8",
        (7,1):"g1",(7,2):"g2",(7,3):"g3",(7,4):"g4",(7,5):"g5",(7,6):"g6",(7,7):"g7",(7,8):"g8",
        (8,1):"h1",(8,2):"h2",(8,3):"h3",(8,4):"h4",(8,5):"h5",(8,6):"h6",(8,7):"h7",(8,8):"h8",}

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

def p2s(xy):
    try:
        return p2s2d[xy]
    except KeyError:
        return 'n/a'

def sq2pos(sq):
    x = ord(sq[0])-96
    y = int(sq[1:])
    return x,y

# build for move expansion
def pbp(xy):
        x,y=xy
        sq = p2s(xy)
        return sq
        
for sq in sqs:
    x,y = sq2pos(sq)
    x= int(x)
    y=int(y)
    sqs[sq]={}
    for p in ['wp','bp','an','ab','ar','aq','ak']: #['wp','wn','wb','wr','wq','wk','bp','bn','bb','br','bq','bk',]:
        col = p[0]
        tip = p[1]
        sqs[sq][p]={'m':[],'t':[],'m2':[],'p':[],'+':[],'e':[],'c':[],}        
        rez = []
        #white pawn:
        if col == 'w' and tip == 'p':
            disp = x,y+2
            if y==2:
                sqs[sq][p]['m2']=[p2s(disp)]
            disp = x,y+1
            if y in range(2,7):
                sqs[sq][p]['m'].append(p2s(disp))
            if y==7:
                sqs[sq][p]['p']=[ p2s(disp)+z_ for z_ in ['R','N','B','Q']]
            disp = x-1,y+1
            sqs[sq][p]['+']=[]
            sqs[sq][p]['e']=[]
            for disp in [(x-1,y+1),(x+1,y+1)]:
                if y in range(2,7):
                    sqs[sq][p]['t'].append(p2s(disp)) #'wp@(x,2<=y<=6),b*@(x+-1,y+1)': 'take(wp,x+-1,y+1)'
                if y==7:
                    sqs[sq][p]['+'].extend([ p2s(disp)+z_ for z_ in ['R','N','B','Q']])
                if y==5:
                    sqs[sq][p]['e'].append(p2s(disp))

        if col == 'b' and tip == 'p':
            disp = x,y-2
            if y==7:
                sqs[sq][p]['m2']=[p2s(disp)]
            disp = x,y-1
            if y in range(3,8):
                sqs[sq][p]['m'].append(p2s(disp))
            if y==2:
                sqs[sq][p]['p']=[p2s(disp)+z_ for z_ in ['R','N','B','Q']]
            disp = x-1,y-1
            sqs[sq][p]['+']=[]
            sqs[sq][p]['e']=[]
            for disp in [(x-1,y-1),(x+1,y-1)]:
                if y in range(3,8):
                    sqs[sq][p]['t'].append(p2s(disp)) #'wp@(x,2<=y<=6),b*@(x+-1,y+1)': 'take(wp,x+-1,y+1)'
                if y==2:
                    sqs[sq][p]['+'].extend([p2s(disp)+z_ for z_ in ['R','N','B','Q']])
                if y==4:
                    sqs[sq][p]['e'].append(p2s(disp))





        # knight
        if tip == 'n':
            for disp in[ (x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2),(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),]:
                sqs[sq][p]['m'].append(p2s(disp))
                sqs[sq][p]['t']=sqs[sq][p]['m']

        if p== 'ak':
            sqs[sq][p]['m'] = bmap[sq]['king']
            sqs[sq][p]['t']=sqs[sq][p]['m']            
                
        for dd in ['NE','SE','SW','NW']:
            if p in ['ab','aq']:
                sqs[sq][p][dd] = bmap[sq][dd][:]
            else:
                sqs[sq][p][dd] = []

        for dd in ['N','E','S','W']:
            if p in ['ar','aq']:
                sqs[sq][p][dd] = bmap[sq][dd][:]
            else:
                sqs[sq][p][dd] = []
        
        #castle
        if tip == 'k':
            if sq == 'e1': sqs[sq][p]['c'].append(p2s((x+2,y)))
            if sq == 'e8': sqs[sq][p]['c'].append(p2s((x+2,y)))
            if sq == 'e1': sqs[sq][p]['c'].append(p2s((x-2,y)))
            if sq == 'e8': sqs[sq][p]['c'].append(p2s((x-2,y)))

        rez = [ z for z in rez if z.count('n/a')==0] #excludes out of the board expansions
        if len(rez)>0:
            print sq,p,rez

for sq in sqs:
    #print '\n'
    for p in sqs[sq]:
        for act in sqs[sq][p]:
            sqs[sq][p][act]=[ z for z in sqs[sq][p][act] if z.count('n/a')==0 ]
        #print 'sqs['+sq+']['+p+']',sqs[sq][p]

    print "'"+sq+"':"+str(sqs[sq])+','

# -----------------------------------------------------------
# ===========================================================
# -----------------------------------------------------------

"""
# below is the build for checks dict
for sq in sqs:

    x,y = sq2pos(sq)
    
    #knight
    sqs[sq]={'knight':[]}
    for q in [(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),]:
        dsq = p2s2(q)
        if dsq != 'n/a':
            sqs[sq]['knight'].append(dsq)

    #pawn
    sqs[sq]['wpawn']=[]
    if p2s2((x+1,y-1)) != 'n/a':
            sqs[sq]['wpawn'].append(p2s2((x+1,y-1)))
    if p2s2((x-1,y-1)) !='n/a':
            sqs[sq]['wpawn'].append(p2s2((x-1,y-1)))
    sqs[sq]['bpawn']=[]
    if p2s2((x+1,y+1)) != 'n/a':
            sqs[sq]['bpawn'].append(p2s2((x+1,y+1)))
    if p2s2((x-1,y+1)) !='n/a':
            sqs[sq]['bpawn'].append(p2s2((x-1,y+1)))

    #king
    sqs[sq]['king']=[]
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for d in directions:
        dsq = p2s2((d[0]+x,d[1]+y))
        if dsq != 'n/a':
            sqs[sq]['king'].append(dsq)

    #NESW
    sqs[sq]['N']=[]
    sqs[sq]['E']=[]
    sqs[sq]['S']=[]
    sqs[sq]['W']=[]

    sqs[sq]['NE']=[]
    sqs[sq]['SE']=[]
    sqs[sq]['SW']=[]
    sqs[sq]['NW']=[]
    for i in range(1,9):
        nsq = p2s2((x,y+i))
        if nsq != 'n/a':
            sqs[sq]['N'].append(nsq)
        esq = p2s2((x+i,y))
        if esq != 'n/a':
            sqs[sq]['E'].append(esq)
        ssq = p2s2((x,y-i))
        if ssq != 'n/a':
            sqs[sq]['S'].append(ssq)
        wsq = p2s2((x-i,y))
        if wsq != 'n/a':
            sqs[sq]['W'].append(wsq)

        nsq = p2s2((x+i,y+i))
        if nsq != 'n/a':
            sqs[sq]['NE'].append(nsq)
        esq = p2s2((x+i,y-i))
        if esq != 'n/a':
            sqs[sq]['SE'].append(esq)
        ssq = p2s2((x-i,y-i))
        if ssq != 'n/a':
            sqs[sq]['SW'].append(ssq)
        wsq = p2s2((x-i,y+i))
        if wsq != 'n/a':
            sqs[sq]['NW'].append(wsq)
            


for sq in sqs:
    print "'"+sq+"':"+str(sqs[sq])+','


"""
