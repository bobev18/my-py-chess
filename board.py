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

from piece import piece

"""
import re, sys, time

global max_eval_memory_size
max_eval_memory_size = 150000
global capture_sign
capture_sign = 'x'
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
"""
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
"""
def pos2sq(x,y):
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)
"""
def p2s(xy):
    x,y=xy
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)

class MoveException(Exception):
    def __init__(self, *args):
        # *args is used to get a list of the parameters passed in
        self.args = [a for a in args]

class board():
    def __init__(self,board_state=''):
        if board_state == '':
            self.board = emptyboardinit.copy()
            self.whites = []
            self.blacks = []
        else:
            self.piecefy(board_state)

    def initialset(self):
        self.piecefy(plainboardinit)
    
    def piecefy(self,board_state):
        self.board = board_state.copy()
        self.whites = []
        self.blacks = []
        for sq in self.board.keys():
            if self.board[sq]!='  ':
                if self.board[sq][0]=='w':
                    self.whites.append(piece(self.board[sq][0],self.board[sq][1],sq))
                else:
                    self.blacks.append(piece(self.board[sq][0],self.board[sq][1],sq))

    def fullset(self):
        return self.whites+self.blacks

    """# no longer used
    def boardify(self):
        #fills the board based on list of pieces
        self.board = self.emptyboardinit.copy()
        for p in self.fullset():
            self.board[p.sq]=p.col+p.type
    """

    def show(self,board_state=''):
        # direct print
        #for i in range(8,0,-1):
        #    print('|',sep='',end='')
        #    for j in range(97,105):
        #        print(self.board[chr(j)+str(i)],sep='',end='|')
        #    print()

        # return string
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
            raise MoveException(msg)

        if piece == None:
            msg = 'Trying to move the air at '+piece_or_sq
            raise MoveException(msg)

        if verbose>0:
            print('>>> board',self)
            print('>>> piece',piece)
            print('>>> orriginal_sq',orriginal_sq)
            

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
            raise MoveException(msg)

        #the following code covers for the boardify:
        self.board[piece.sq]='  '
        
        if piece.col == 'w':
            self.whites.remove(piece)
        else:
            self.blacks.remove(piece)

        del(piece) #? needed?

    def add(self,col,tip='',sq=''):
        if tip=='' and sq=='':
            sq = col[-2:]
            tip = col[1]
            col = col[0]

        if self.piece_by_sq(sq) != None:
            msg = 'Are you blind - there is another piece at that spot: '+repr(self.piece_by_sq(tosq))
            raise MoveException(msg)

        #print(col,tip,sq)
        p = piece(col,tip,sq)
        if col == 'w':
            self.whites.append(p)
        else:
            self.blacks.append(p)

        #the following code covers for the boardify:
        self.board[p.sq]=p.col+p.type

    def exec_move(self,piece,exp,verbose=0):#,virtual=False):
        # the function that applies given expansion EXP to the piece set (and thus the board)
        if type(piece) == int :
            verbose=1
        if verbose>0:
            print(')))',piece,exp)
        if exp[0]=='m':
            self.relocate(piece,exp[1],verbose)
        elif exp[0]=='t':
            self.take(exp[1]) # take the piece at the destiantion position 
            self.relocate(piece,exp[1]) # move to the destination position
        elif exp[0]=='e':
            self.take(exp[1][0]+piece.sq[1]) #exp[1][0] is the file of the pawn being taken, piece.sq[1] is the rank of the pawn executing the e.p. before the move
            self.relocate(piece,exp[1])
        elif exp[0]=='p':
            self.add(piece.col,exp[2][-1].lower(),exp[1])
            self.take(piece)
        elif exp[0]=='+':
            self.take(exp[1]) # take the piece at the destination
            self.add(piece.col,exp[2][-1].lower(),exp[1]) #add the prmo
            self.take(piece) # remove the pawn
        elif exp[0]=='c':
            if exp[2]=='O-O':
                self.relocate('h'+piece.sq[1], 'f'+piece.sq[1]) # move the rook
                self.relocate(piece,exp[1]) # move the king
            else: #O-O-O
                self.relocate('a'+piece.sq[1], 'd'+piece.sq[1]) # move the rook
                self.relocate(piece,exp[1]) # move the king


    def virt_move(self,piece,exp,verbose=0):#,virtual=False):
        # the function returns board state with applied given expansion EXP to the board
        
        if verbose>0:
            print(']]]',piece,exp)
        new_state=self.board.copy()

        if (new_state[exp[1]]=='  ' and exp[0] in ['t','+']) or (new_state[exp[1]]!='  ' and exp[0] in ['m','e','p','c']):
            raise MoveException('virtual move invalid ','piece',piece,'target sq:',new_state[exp[1]],'exp'+str(exp),'newstate \n',str(new_state))
        
        if exp[0]=='m':
            #new_state = mv(new_state,piece.sq,exp[1])
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='t':
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='e':
            new_state[exp[1][0]+piece.sq[1]]= '  '  #exp[1][0] is the file of the pawn being taken, piece.sq[1] is the rank of the pawn executing the e.p. before the move
            new_state[exp[1]] = piece.col+piece.type
            new_state[piece.sq] = '  '
        elif exp[0]=='p':
            new_state[exp[1]] = piece.col+exp[2][-1].lower()
            new_state[piece.sq] = '  '
        elif exp[0]=='+':
            new_state[exp[1]] = piece.col+exp[2][-1].lower()
            new_state[piece.sq] = '  '
        elif exp[0]=='c':
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

        return new_state

    def validate_move(self,piece,move,verbose=0):
        # only validates against position, cannot reject moves based on history conditions
        #verbose =1
        if piece.col == 'w':
            oposite_col = 'b'
            castle_row = '1'
        else:
            oposite_col = 'w'
            castle_row = '8'

        #find king sq
        if piece.type == 'k':
            ksq = [move[1]]
            if move[2].count('O')==2:
                ksq.extend([piece.sq,'f'+castle_row])
            if move[2].count('O')==3:
                ksq.extend([piece.sq,'d'+castle_row])
            #piece.sq -- The king is not currently in check
            #'f'+castle_row -- The king does not pass through a square that is under attack by enemy pieces
            #move[1] -- The king does not end up in check
        else:
            if verbose>0:
                print('search for te king in:',self.fullset())
            ksq = [ z.sq for z in self.fullset() if z.type=='k' and z.col==piece.col ]

        check_state = self.virt_move(piece,move,verbose)
        if verbose > 0:
            print('checking check against',ksq)
            #print(check_state)
            
        #return not self.sq_in_check(ksq,oposite_col,self.virt_move(piece,move))
        is_in_check = [ self.sq_in_check(z,oposite_col,check_state,verbose) for z in ksq ]
        if verbose>0:
            print('is_in_check',is_in_check)

        return not any(is_in_check) # if ANY of the possitions is in check, we should return False to indicate the move as invalid
        
    def sq_in_check(self,sq,by_col,b_state='',verbose=0):
        # checks if a square sq is in check/hit by player with by_col
        #  the idea is to "reverse-expand" the square -- it will be cheeper than expanding all enemy moves and finding the sq in "('t',sq,*)"
        #     very side note: if we are to expand the enemy anyway for AI analysis, we might evaluate the moves with the above principle!

        if b_state=='':
            board_state = self.board
        else:
            board_state = b_state
        
        x,y = sq2pos(sq)
        disp = [(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),]
        dispsq = [ p2s(z) for z in disp if p2s(z)!='n/a']
        for dsq in dispsq:
            if board_state[dsq] == by_col+'n': return True

        #pawns
        disp = [(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),]
        dispsq = [ p2s(z) for z in disp if p2s(z)!='n/a']
        if by_col == 'w' and ((p2s((x+1,y-1)) != 'n/a' and board_state[p2s((x+1,y-1))] == 'wp') or (p2s((x-1,y-1)) !='n/a' and board_state[p2s((x-1,y-1))] == 'wp')): return True
        if by_col == 'b' and ((p2s((x+1,y+1)) != 'n/a' and board_state[p2s((x+1,y+1))] == 'bp') or (p2s((x-1,y+1)) !='n/a' and board_state[p2s((x-1,y+1))] == 'bp')): return True
        
        """
        if board_state[pos2sq(x-1,y+2)] == by_col+'n': return True
        if board_state[pos2sq(x-2,y+1)] == by_col+'n': return True
        if board_state[pos2sq(x-2,y-1)] == by_col+'n': return True
        if board_state[pos2sq(x-1,y-2)] == by_col+'n': return True
        if board_state[pos2sq(x+1,y+2)] == by_col+'n': return True
        if board_state[pos2sq(x+2,y+1)] == by_col+'n': return True
        if board_state[pos2sq(x+2,y-1)] == by_col+'n': return True
        if board_state[pos2sq(x+1,y-2)] == by_col+'n': return True
        """

        #NE=SE=SW=NW=N=E=S=W=False # flags for each direction
        directions = {'N':False,'NE':False,'E':False,'SE':False,'S':False,'SW':False,'W':False,'NW':False}
        for i in range(1,8):
            disp = {(x,y+i):['N',['q','r']],(x+i,y+i):['NE',['q','b']],
                    (x+i,y):['E',['q','r']],(x+i,y-i):['SE',['q','b']],
                    (x,y-i):['S',['q','r']],(x-i,y-i):['SW',['q','b']],
                    (x-i,y):['W',['q','r']],(x-i,y+i):['NW',['q','b']],}
            for d in disp.keys():
                if not directions[disp[d][0]]:
                    sqdisp = p2s(d) # state of the displaced square # it can be own piece, enemy or empty
                    if verbose>0 : print('i',i,'disp key',d,'disp[key]',disp[d],'disp sq',sqdisp)
                    if sqdisp != 'n/a':
                        if verbose>0 : print('board[sq] >',board_state[sqdisp],'<')#,sep='')
                        if board_state[sqdisp][0] == by_col: # at the displacement square there is an enemy piece
                            if i == 1 and board_state[sqdisp][1] =='k': return True  # king at distance 1
                            if board_state[sqdisp][1] in disp[d][1]: return True # relevant displacement operator at distance i
                            directions[disp[d][0]]=True # the direction is blocked if an enemy piece doesnt operate in that direction IRRELEVANT displacement operator at distance i
                        else:
                            if board_state[sqdisp] != '  ': # not an empty field, which leaves the option of it having a piece of own color
                                if verbose>0 : print('*'*3)
                                directions[disp[d][0]]=True # the direction is blocked

       

        return False

    def valids(self,piece, debug=0):
        # return list of hist independant valid moves for given piece
        reductions = [] # list of the moves which will be excluded form the expansions, due to opening check
        expansions = piece.expand(self.board)
        if debug>0:
            print(self.show())
            print('unreduced expansions:',expansions)
        for e in expansions:
            if not self.validate_move(piece,e,debug):
                reductions.append(e)

        if debug>0:
            print('reductions:',reductions)
        return [ z for z in expansions if z not in reductions ]
