# -*- coding: utf-8 -*-
#TO DO:
# -1. write the AI
# -1.1 AI needs tweaking
# -1.1.1 Optimize speed
# -1.1.2 Better the evaluation
# 1. write the clock function - it will help tweaking the AI
# 2. create function that converts a game notation list of moves -- i.e. split()
# 3. Add disambiguation after the expand function - check for repeating notations when merging piece based expansion list - if any - add flank/row
#           not tested
# 4. 

# * maybe rewrite the move_decode using reg ex
# * after reaching some completeness, copy the board class & rewrite to use only states, or only pieces, and test AI timing
#
# DESIGN DECISION reasoning:
#  Decision = keep self.board = board_state as variable of the board class, although it can be calculated from the pieces list
#  Reason(s)= we can easily replace the variable with a function, that does the calculation and returns the same value,
#             however the majority of the time the value needs to be passed without changes i.e. we will be cycling a
#             calcualtion and getting the same result every time we pass the board_state to a method. The additional memory cost is
#             2chars per square => 2bytes*64sq  = 128bytes. Eventually once we have the recursion in place, we can modify the class
#             and test to compare the productivity of the two implementations. For now we will keep the extra variable as it makes it
#             simpler to read & write the code.

# hist
# castle relevant history + last move = {'sw': True, 'nw': True, 'ne': True, 'se': True, 'wk': True, 'bk':True, 'last': 'g5'}
#  !!! e.p. verification of the last move == 'g5' is insufficient since it might be result of g6g5 and not only g7g5 !!!
#             done, but not tested!
###################################################

global capture_sign
capture_sign = 'x'

"""
import re, sys, time

global max_eval_memory_size
max_eval_memory_size = 150000

global pvalues
pvalues = {'p':1.0,'r':5.0,'n':3.0,'b':3.0,'q':10.0,'k':0.0,' ':0.0}
global sqvalues
sqvalues = { 'a8':0.01, 'b8':0.01, 'c8':0.01, 'd8':0.01, 'e8':0.01, 'f8':0.01, 'g8':0.01, 'h8':0.01,
             'a7':0.01, 'b7':0.02, 'c7':0.02, 'd7':0.02, 'e7':0.02, 'f7':0.02, 'g7':0.02, 'h7':0.01,
             'a6':0.01, 'b6':0.02, 'c6':0.03, 'd6':0.03, 'e6':0.03, 'f6':0.03, 'g6':0.02, 'h6':0.01,
             'a5':0.01, 'b5':0.02, 'c5':0.03, 'd5':0.04, 'e5':0.04, 'f5':0.03, 'g5':0.02, 'h5':0.01,
             'a4':0.01, 'b4':0.02, 'c4':0.03, 'd4':0.04, 'e4':0.04, 'f4':0.03, 'g4':0.02, 'h4':0.01,
             'a3':0.01, 'b3':0.02, 'c3':0.03, 'd3':0.03, 'e3':0.03, 'f3':0.03, 'g3':0.02, 'h3':0.01,
             'a2':0.01, 'b2':0.02, 'c2':0.02, 'd2':0.02, 'e2':0.02, 'f2':0.02, 'g2':0.02, 'h2':0.01,
             'a1':0.01, 'b1':0.01, 'c1':0.01, 'd1':0.01, 'e1':0.01, 'f1':0.01, 'g1':0.01, 'h1':0.01,}

global evaluated
evaluated = {}

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



def sq2pos(sq):
    x = ord(sq[0])-96
    y = int(sq[1:])
    return x,y

def pos2sq(x,y):
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)
"""
def p2s(xy):
    x,y=xy
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)
"""
class MoveException(Exception):
    def __init__(self, *args):
        # *args is used to get a list of the parameters passed in
        self.args = [a for a in args]

"""
class piece():
    
    def __init__(self, col, tip, sq): # col=['w','b'] tip=['p','r','n','b','q','k'] sq = [a1..h8]
        self.col = col
        self.type = tip
        self.sq = sq
        self.x = ord(self.sq[0])-96
        self.y = int(self.sq[1])
        #self.onboard = True
        #names = {'p':'Pawn','r':'Rook','n':'Knight','b':'Bishop','q':'Queen','k':'King',' ':''}
        #values = {'p':1,'r':5,'n':3,'b':3,'q':10,'k':0,' ':0}
        #self.name = names[tip]
        #self.val = values[tip]

    def __repr__(self):
        return self.col+self.type+'@'+self.sq
        
    """
    def __repr__(self):
        if self.onboard:
            return self.col+self.type+'@'+self.sq
        else:
            return self.col+self.type+'@taken'
    
    def move(self,destination):
        if destination==None:
            self.take()
        else:
            self.sq = destination
            self.x = ord(self.sq[0])-96
            self.y = int(self.sq[1])

    def take(self):
        self.sq = ''
        self.x = -1
        self.y = -1
        self.onboard = False
    """ 

    def expand(self, board_state):
        # list possible moves based on preconditions only.
        # there are post conditions (like screws) that should be considered afterwards, as they depend expansions of the opponents pieces!
        #  - board_state - dict representation of the board state, and not the board object!!! 
        #  result is returned as notation integrated in the command representation i.e. tuple(comm,sq,notation)

        #print('expanding',self)
        

        """
        def piece_by_pos(x,y=''):
            #print('x',x,'y',y)
            if y!='':
                sq = pos2sq(x,y)
            else:
                sq = x
                x,y = sq2pos(sq)

            if x<1 or x>8 or y<1 or y>8: return 'n/a'
            return board_state[sq]
        """

        def pbp(xy):
            x,y=xy
            sq = p2s(xy)
            if sq == 'n/a':
                return sq
            else:
                return board_state[sq]

        #rezexe = [] #command sequence; possible types: move @sq, take @sq, e.p @sq, castle @sq, promo @sq, take+promo @sq => (type,sq)
        #  m=move t=take e=en passant c=castle p=promo +=take+promo
        #rezsan = [] #SAN = Simple Algebric Notation
        rez = []
        #if not self.onboard:
        #    return rez

        # result representation in triplets of (a,sq,note) where
        #   a = action[m=move t=take e=en passant c=castle p=promo +=take+promo]
        #   sq = square is param for the action
        #   note = notation*
        #     *   Notation is close to Algebraic_chess_notation http://en.wikipedia.org/wiki/Algebraic_chess_notation but
        #         the full complience will need additional steps to add disambiguation, checks and mate

        #white pawn:
        if self.col == 'w' and self.type == 'p':
            #print('self.x',self.x,'self.y',self.y)
            disp = self.x,self.y+2
            if self.y==2 and pbp((self.x,3))=='  ' and pbp((self.x,4))=='  ': rez.append(('m',p2s(disp),p2s(disp))) #'wp@(x,2),none@(x,3),none@(x,4)': 'move(0,2)'
            disp = self.x,self.y+1
            if self.y>=2 and self.y<7 and pbp(disp)=='  ': rez.append(('m',p2s(disp),p2s(disp))) #'wp@(x,2<=y<=6),none@(x,y+1)': 'move(wp,x,y+1)'
            if self.y==7 and pbp(disp)=='  ': rez.extend([ ('p',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']]) #'wp@(x,7),none@(x,8)': 'promote(q,r,n,b,x,8)'
            disp = self.x-1,self.y+1
            if self.y>=2 and self.y<7 and pbp(disp)[0]=='b': rez.append(('t',p2s(disp),self.sq[0]+capture_sign+p2s(disp))) #'wp@(x,2<=y<=6),b*@(x+-1,y+1)': 'take(wp,x+-1,y+1)'
            if self.y==7 and pbp(disp)[0]=='b': rez.extend([ ('+',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']])#'wp@(x,7),b*@(x+-1,y+1)': 'promote(q|r|n|b,x+-1,8)'
            #if self.y==5 and lastmove == chr(self.x-1+96)+'5': rez.append(('e',p2s(disp),self.sq[0]+capture_sign+p2s(disp))) #'wp@(x,5),none@(x-1,y+1),board.lastmove(bp,from(x-1,y+2),to(x-1,y))': 'anpasan(wp,x-1,y+1)'
            if self.y==5 and pbp(disp)=='  ' and pbp((self.x-1,self.y))=='bp': rez.append(('e',p2s(disp),self.sq[0]+capture_sign+p2s(disp)))
            disp = self.x+1,self.y+1
            if self.y>=2 and self.y<7 and pbp(disp)[0]=='b': rez.append(('t',p2s(disp),self.sq[0]+capture_sign+p2s(disp))) #'wp@(x,2<=y<=6),b*@(x+-1,y+1)': 'take(wp,x+-1,y+1)'
            if self.y==7 and pbp(disp)[0]=='b': rez.extend([ ('+',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']])
            if self.y==5 and pbp(disp)=='  ' and pbp((self.x+1,self.y))=='bp': rez.append(('e',p2s(disp),self.sq[0]+capture_sign+p2s(disp))) #'wp@(x,5),none@(x-1,y+1),board.lastmove(bp,from(x-1,y+2),to(x-1,y))': 'anpasan(wp,x+1,y+1)'

        if self.col == 'b' and self.type == 'p':
            disp = self.x,self.y-2
            if self.y==7 and pbp((self.x,6))=='  ' and pbp((self.x,5))=='  ': rez.append(('m',p2s(disp),p2s(disp)))
            disp = self.x,self.y-1
            if self.y<=7 and self.y>2 and pbp(disp)=='  ': rez.append(('m',p2s(disp),p2s(disp)))
            if self.y==2 and pbp(disp)=='  ': rez.extend([ ('m',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']])
            
            disp = self.x-1,self.y-1
            if self.y>=7 and self.y>2 and pbp(disp)[0]=='w': rez.append(('t',p2s(disp),self.sq[0]+capture_sign+p2s(disp)))
            if self.y==2 and pbp(disp)[0]=='w': rez.extend([ ('+',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']])
            if self.y==5 and pbp(disp)=='  ' and pbp((self.x-1,self.y))=='wp': rez.append(('e',p2s(disp),self.sq[0]+capture_sign+p2s(disp)))
            disp = self.x+1,self.y-1
            if self.y>=7 and self.y>2 and pbp(disp)[0]=='w': rez.append(('t',p2s(disp),self.sq[0]+capture_sign+p2s(disp)))
            if self.y==2 and pbp(disp)[0]=='w': rez.extend([ ('+',p2s(disp),p2s(disp)+z_) for z_ in ['R','N','B','Q']])
            if self.y==4 and pbp(disp)=='  ' and pbp((self.x+1,self.y))=='wp': rez.append(('e',p2s(disp),self.sq[0]+capture_sign+p2s(disp)))

        if self.type == 'n':
            disp = self.x+1,self.y-2
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp =self.x+1,self.y-2
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp =self.x+2,self.y-1
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp =self.x+2,self.y-1
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp = self.x+2,self.y+1
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp = self.x+2,self.y+1
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp = self.x+1,self.y+2
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp = self.x+1,self.y+2
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))

            disp =self.x-1,self.y-2
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp = self.x-1,self.y-2
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp =self.x-2,self.y-1
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp =self.x-2,self.y-1
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp =self.x-2,self.y+1
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp =self.x-2,self.y+1
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))
            disp =self.x-1,self.y+2
            if pbp(disp)=='  ': rez.append(('m',p2s(disp),'N'+p2s(disp)))
            disp =self.x-1,self.y+2
            if pbp(disp)!='  ' and pbp(disp)[0]!=self.col: rez.append(('t',p2s(disp),'Nx'+p2s(disp)))

        if self.type in ['q','k','b','r']:
            NE=SE=SW=NW=N=E=S=W=False # flags for each direction
            if self.type == 'k':
                maxrange = 2
            else:
                maxrange = 8
            for i in range(1,maxrange):
                disp = self.x+i,self.y+i
                if not NE and self.type in ['q','b','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        NE = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x+i,self.y-i
                if not SE and self.type in ['q','b','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        SE = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x-i,self.y-i
                if not SW and self.type in ['q','b','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        SW = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x-i,self.y+i
                if not NW and self.type in ['q','b','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        NW = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x,self.y+i                            
                if not N and self.type in ['q','r','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        N = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x+i,self.y
                if not E and self.type in ['q','r','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        E = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x,self.y-i
                if not S and self.type in ['q','r','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        S = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

                disp = self.x-i,self.y
                if not W and self.type in ['q','r','k']:
                    if pbp(disp)=='  ':
                        rez.append(('m',p2s(disp),self.type.upper()+p2s(disp)))
                    else:
                        W = True
                        if pbp(disp)[0]!=self.col:
                            rez.append(('t',p2s(disp),self.type.upper()+'x'+p2s(disp)))

        if self.type == 'k':
            if self.col == 'w' and self.sq == 'e1' and board_state['h1']=='wr' and board_state['f1']=='  ' and board_state['g1']=='  ': rez.append(('c',p2s((self.x+2,self.y)),'O-O'))
            if self.col == 'b' and self.sq == 'e8' and board_state['h8']=='br' and board_state['f8']=='  ' and board_state['g8']=='  ': rez.append(('c',p2s((self.x+2,self.y)),'O-O'))
            if self.col == 'w' and self.sq == 'e1' and board_state['a1']=='wr' and board_state['b1']=='  ' and board_state['c1']=='  ' and board_state['d1']=='  ': rez.append(('c',p2s((self.x-2,self.y)),'O-O-O'))
            if self.col == 'b' and self.sq == 'e8' and board_state['a8']=='br' and board_state['b8']=='  ' and board_state['c8']=='  ' and board_state['d8']=='  ': rez.append(('c',p2s((self.x-2,self.y)),'O-O-O'))

        rez = [ x for x in rez if x.count('n/a')==0] #excludes out of the board expansions
        return rez
        
