# -*- coding: utf-8 -*-
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

#const
plainboardinit = {'a8':'br', 'b8':'bn', 'c8':'bb', 'd8':'bq', 'e8':'bk', 'f8':'bb', 'g8':'bn', 'h8':'br',
                 'a7':'bp', 'b7':'bp', 'c7':'bp', 'd7':'bp', 'e7':'bp', 'f7':'bp', 'g7':'bp', 'h7':'bp',
                 'a6':'  ', 'b6':'  ', 'c6':'  ', 'd6':'  ', 'e6':'  ', 'f6':'  ', 'g6':'  ', 'h6':'  ',
                 'a5':'  ', 'b5':'  ', 'c5':'  ', 'd5':'  ', 'e5':'  ', 'f5':'  ', 'g5':'  ', 'h5':'  ',
                 'a4':'  ', 'b4':'  ', 'c4':'  ', 'd4':'  ', 'e4':'  ', 'f4':'  ', 'g4':'  ', 'h4':'  ',
                 'a3':'  ', 'b3':'  ', 'c3':'  ', 'd3':'  ', 'e3':'  ', 'f3':'  ', 'g3':'  ', 'h3':'  ',
                 'a2':'wp', 'b2':'wp', 'c2':'wp', 'd2':'wp', 'e2':'wp', 'f2':'wp', 'g2':'wp', 'h2':'wp',
                 'a1':'wr', 'b1':'wn', 'c1':'wb', 'd1':'wq', 'e1':'wk', 'f1':'wb', 'g1':'wn', 'h1':'wr',}

"""
def sq2pos(sq):
    x = ord(sq[0])-96
    y = int(sq[1:])
    return x,y

def pos2sq(x,y):
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)

def p2s(xy):
    x,y=xy
    if x<1 or x>8 or y<1 or y>8: return 'n/a'
    return chr(96+x)+str(y)

"""
#from piece import piece
from board import board
from board import MoveException

class game():
    def __init__(self,wplayer='human',bplayer='human',clock=60*60,logfile='d:\\temp\\chesslog.txt'):
        self.zboard = board(plainboardinit)
        self.white = {'col':'w', 'player':wplayer, 'time':clock, 'hist': [], 'is_in_check':False}
        self.black = {'col':'b', 'player':bplayer, 'time':clock, 'hist': [], 'is_in_check':False}
        self.turn = self.white
        self.turn_count = 1
        self.full_notation = '' # quite as the values in hist, but with the count and # + ? !
        self.logfile = logfile #sys.stdout
        #self.log = open(logfile,'w')

        #initiate the game cycle
        #self.cycle()
    
    def logit(self,*args):
        #if self.log == None:
        #    self.startlog()
        data = ''
        for arg in args:
            data+=str(arg)+' ; '
        with open(self.logfile,'a') as zlog:
            zlog.write(data)

    def turnset(self):
        if self.turn['col']=='w':
            return self.zboard.whites
        else:
            return self.zboard.blacks

    def show(self):
        # shows the state of the game
        rez = self.zboard.show()+'\n'
        rez += 'on turn: '+self.turn['col']+' || remaining time: '+str(self.turn['time']) +'\n'
        if self.turn['is_in_check']:
            rez += 'player is in check. possible moves:\n'+str(self.verified([ z for z in self.turnset() if z.type=='k' ][0])) +'\n'
        else:
            rez += 'pieces at disposal:\n'+str(self.turnset()) +'\n'
        return rez
        
    def prompt_human_move(self):
        self.show()
        mv = None
        while mv==None:
            inp = raw_input('enter your move: ')
            if inp[0] != '?':
                try:
                    mv = self.decode_move(inp,self.turnset())
                except MoveException as err:
                    print('erroneous move',err.args)
            else:
                mv = inp[1:]

        return mv #returns move or command

    def AIeval(self,board_state):
        hashstate = ''.join([ board_state[z] for z in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'] ])
        if hashstate in evaluated.keys():
            return evaluated[hashstate]
        
        wval=bval= 0.0
        for sq in board_state:
            psq = board_state[sq]
            if psq[0]=='w':
                wval+=pvalues[psq[1]]
                wval+=sqvalues[sq]
            else:
                bval+=pvalues[psq[1]]
                bval+=sqvalues[sq]

        if len(evaluated)<max_eval_memory_size: evaluated[hashstate]=(wval,bval)
        return (wval,bval)

    def AIrecursion(self,boardstate,col,tcol,depth,alpha,beta,sq2exp):
        depthindent=' '*(5-depth)
        #print('/n/n',depthindent,5*'-','CALL AIrecursion','-'*5,file=self.log)
        #print(depthindent,'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1],end=' ',file=self.log)
        #print(depthindent,'boardstate:',boardstate,file=self.log)
        new_state = board(boardstate)
        #exec_move takes piece object, which to move, and expansion in triplet 'move type', 'destination square', 'notation'
        # we have no use of the piece object, since the new board object creates new piece objects
        # we still need easy way to operate on the piece we want, so we'll use sq2exp = tuple of square of the piece, expansion
        new_state.exec_move(new_state.piece_by_sq(sq2exp[0]),sq2exp[1])
        #print('-'*30)
        #print(new_state.show())
        #print('new_state.piece_by_sq(sq2exp[0])',new_state.piece_by_sq(sq2exp[0]),'sq2exp[1]',sq2exp[1])
        #print('sq2exp',sq2exp)
        #print('playin col:',col)
                
        if tcol=='w':
            pieces_set=new_state.whites[:]
            opposite = 'b'
        else:
            pieces_set=new_state.blacks[:]
            opposite = 'w'

        turn_in_check = False
        # check if either side is in check >>  sq_in_check(self,sq,by_col,b_state='',verbose=0):
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ])==0: print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:])
        w_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ][0],'b',new_state.board)
        if w_in_check and tcol=='w': turn_in_check = True
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ])==0: print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:])
        b_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ][0],'w',new_state.board)
        if b_in_check and tcol=='b': turn_in_check = True

        # ignore cut at depth==0 if last turn results in check -- dig deeper
        if depth <=0 and (sq2exp[1][2].count(capture_sign)==0 or (not w_in_check) and (not b_in_check)):
            #
            #
            # !!! adding sq2exp[1][2].count(capture_sign)==0: got 1000731 rows for in_check expansion!!!
            #
            #
            r= self.AIeval(new_state.board)
            #print('r',r)
            # r = tuple of the value for whites in the deepest state, and the value for blacks in the deepest state
            rez = round(r[0]-r[1],3)
            if col!='w':
                rez = -rez
                
            #print(depthindent,'state value for black',rez,file=self.log)
            #print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:],'state val',rez,file=self.log)
            self.logit(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:],'state val',rez)
            return [rez,0]

        #print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'w+',w_in_check,'b+',b_in_check,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:],file=self.log)
        self.logit(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'w+',w_in_check,'b+',b_in_check,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1:])
        #print(depthindent,'new_state full set:',new_state.fullset(),file=self.log)
        
        moverez = []
        pruning = False
        original_length = 0
        while not pruning and len(pieces_set)>0 :
            p=pieces_set.pop(0)
            #
            # !!!
            # !!!!!! we cant use verified method as it's dependat on the game object
            # !!! the first move will be validated against history, but the recursions wont be able to cover it
            # unless, we pass history events from the game and keep internal track...
            #

            """
            if str(p)=='bp@e6' and sq2exp[1:]==[('t', 'g6', 'Qxg6'), 'Rg8']: # : state {'h8': '  ', 'h2': 'wp', 'h3': '  ', 'h1': '  ', 'h6': '  ', 'h7': 'bn', 'h4': '  ', 'h5': '  ', 'd8': '  ', 'a8': 'br', 'd6': '  ', 'd7': '  ', 'd4': '  ', 'd5': '  ', 'd2': '  ', 'd3': '  ', 'd1': '  ', 'g7': 'wr', 'g6': 'wq', 'g5': '  ', 'g4': '  ', 'g3': '  ', 'g2': 'wp', 'g1': 'wk', 'g8': 'br', 'c8': '  ', 'c3': '  ', 'c2': 'bq', 'c1': '  ', 'c7': '  ', 'c6': '  ', 'c5': '  ', 'c4': '  ', 'f1': 'wr', 'f2': 'wp', 'f3': 'wn', 'f4': '  ', 'f5': '  ', 'f6': 'bp', 'f7': '  ', 'f8': '  ', 'b4': '  ', 'b5': '  ', 'b6': 'bp', 'b7': '  ', 'b1': '  ', 'b2': '  ', 'b3': '  ', 'b8': '  ', 'a1': '  ', 'a3': 'wp', 'a2': '  ', 'a5': 'bp', 'e8': 'bk', 'a7': '  ', 'a6': '  ', 'e5': '  ', 'e4': 'wp', 'e7': '  ', 'e6': 'bp', 'e1': '  ', 'e3': 'wb', 'e2': '  ', 'a4': '  '} [('m', 'e5', 'e5')]
                #print('new_state:',new_state)
                #print('new_state full set:',new_state.fullset())
                expansions=new_state.valids(p,1)
            else:
                expansions=new_state.valids(p)
            """
            expansions=new_state.valids(p)
            #print(new_state.show(),file=self.log)
            #print(depthindent,'valids4',p,':',expansions,'     state',new_state.board,file=self.log)
            if depth <=0 and sq2exp[1][2].count(capture_sign)!=0:
                original_length += len(expansions)
                expansions = [ z for z in expansions if z[0] in ['t','+','e'] and z[1]==sq2exp[1][1] ]
                # i.e. check deeper only captures that take at the same sq as the last vapture

            if depth <=0 and sq2exp[1][2].count(capture_sign)==0: #not deeper due to capturing
                reduced_expansions = []
                original_length += len(expansions)
                for exp in expansions:
                    vboard = new_state.virt_move(p,exp)
                    if tcol =='w':
                        still_in_check = new_state.sq_in_check([ z for z in vboard.keys() if vboard[z]=='wk' ][0],'b',vboard)
                    else:
                        still_in_check = new_state.sq_in_check([ z for z in vboard.keys() if vboard[z]=='bk' ][0],'w',vboard)
                    if not still_in_check:
                        reduced_expansions.append(exp)

                #expansions = reduced_expansions
                # i.e. check deeper only non captures so that only ceck moves will persist in depth
                ##
                #
                #the concept currently fails because at depth 0 we end up with state that can only be resolved by capturing
                # we have to expand only non capture moves, but that mandates that the next state will also have the check from the previous one.
                #
                ##
                if turn_in_check and len(reduced_expansions)>0:
                    expansions = reduced_expansions
                # the check above will cause sub depth limit expansions, that initially occured due to the last checked move was resulting in check, to
                #   go deeper using a capture move as long as there are no other alternatives to escape the check
            
            while not pruning and len(expansions)>0:
                e = expansions.pop(0)
                #print('-- p',p,'e',e)
                if len(sq2exp)>2:
                    remnant = sq2exp[2:]
                else:
                    remnant = []
                remnant.insert(0,sq2exp[1][2])
                remnant.insert(0,e)
                remnant.insert(0,p.sq)
                try:
                    r = self.AIrecursion(new_state.board,col,opposite,depth-1,alpha,beta,remnant)
                except MoveException as err:
                    print('********** Exception args:',str(err.args))
                    print(new_state.show())
                    print('new_state.piece_by_sq(sq2exp[0])',new_state.piece_by_sq(sq2exp[0]),'sq2exp[1]',sq2exp[1])
                    print('sq2exp',sq2exp)
                    print('playin col:',col)
                    print('-- p',p,'e',e)
                    #print('zr',r)
                    
                r.append(e)
                moverez.append(r)
                
                #pruning
                if tcol==col: #MAX in the cycle
                    if r[0]>beta:
                        pruning = True
                        #print(depthindent,'pruned r[0]>beta',r[0],'>',beta,'| skipping:',expansions,'+',pieces_set,file=self.log)
                        self.logit(depthindent,'pruned r[0]>beta',r[0],'>',beta,'| skipping:',expansions,'+',pieces_set)
                    if r[0]>alpha:
                        alpha=r[0]
                else:
                    if r[0]<alpha:
                        pruning = True
                        #print(depthindent,'pruned r[0]<alpha',r[0],'<',alpha,'| skipping:',expansions,'+',pieces_set,file=self.log)
                        self.logit(depthindent,'pruned r[0]<alpha',r[0],'<',alpha,'| skipping:',expansions,'+',pieces_set)
                    if r[0]<beta:
                        beta = r[0]

        #next if is to cover for reduction of expasions to consequtive take squares, might get misinterpreted as mate
        if depth<=0 and len(moverez)==0 and original_length>0:
            r= self.AIeval(new_state.board)
            rez = round(r[0]-r[1],3)
            if col!='w':
                rez = -rez
            #print(depthindent,'turn col:',tcol,'depth:',depth,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1],'state val',rez,file=self.log)
            moverez = [[rez,0]]

        #print(depthindent,'moverez to max/min:',moverez,file=self.log)
        if tcol==col:
            if len(moverez)==0:
                thing = [-99, '#']
                #print(depthindent,'returning:',thing,file=self.log)
                self.logit(depthindent,'returning:',thing)
                if thing[0]>alpha:
                    alpha=thing[0]
            else:
                thing = max(moverez,key=lambda _t: _t[0])
                
                somerez = [ z for z in moverez if z[0]==thing[0] ]
                thing = min(somerez, key=lambda _t: _t[1])

                #print(depthindent,'return max moverez:',thing,file=self.log) 
                self.logit(depthindent,'return max moverez:',thing)
        else:
            if len(moverez)==0:
                thing = [99, '#']
                #print(depthindent,'returning:',thing,file=self.log)
                self.logit(depthindent,'returning:',thing)
                if thing[0]<beta:
                    beta=thing[0]
            else:
                thing = min(moverez,key=lambda _t: _t[0])
                #print(depthindent,'return min moverez:',thing,file=self.log)
                self.logit(depthindent,'return min moverez:',thing)
        
            #if type(thing[0]) == list or ('m', 'h3', 'h3') in thing:
            #    print('moverez',moverez)
            #    print('thing',thing)

        thing.insert(1,len(moverez)) # number of all available moves
        
        return thing
                
                

    def AI_move(self,depth=5,verbose=0):
        #print('/n/n',5*'-','CALL AI_move','-'*5,file=self.log)
        self.logit('/n/n',5*'-','CALL AI_move','-'*5)
        #print('depth:',depth,file=self.log)
        self.logit('depth:',depth)
        rez = {}
        if self.turn['col']=='w':
            opposite = 'b'
        else:
            opposite = 'w'

        #set separate log file for each AI move, beacuse otherwise the log gets 0.5GB big
        templog = self.log
        alpha=-999
        beta=999
        pieces_set = self.turnset()[:]
        pruning = False
        while not pruning and len(pieces_set)>0 :
            p = pieces_set.pop(0)
            local_rez = []
            possible_moves = self.verified(p)
            if len(possible_moves)>0:
                with open(self.logfile[:-4]+'_'+str(self.turn_count)+'_'+str(p)+'.txt','w') as f: # this will also close the turn specific log file
                    while not pruning and len(possible_moves)>0:
                        e=possible_moves.pop(0)
                        self.log = f #switch log
                        rr = self.AIrecursion(self.zboard.board,self.turn['col'],opposite,depth,alpha,beta,(p.sq,e))
                        rr.append(e)
                        local_rez.append(rr)
                        #pruning
                        if rr[0]>beta:
                            pruning = True
                            #print('pruned r[0]>beta',rr[0],'>',beta,'| skipping:',possible_moves,'+',pieces_set,file=self.log)
                            self.logit('pruned r[0]>beta',rr[0],'>',beta,'| skipping:',possible_moves,'+',pieces_set)
                            if verbose>0:
                                print('pruned r[0]>beta',rr[0],'>',beta,'| skipping:',possible_moves,'+',pieces_set)
                        if rr[0]>alpha:
                            alpha=rr[0]

            self.log = templog # return to the main log file
            if verbose>0:
                print('p:',p,'     -> ',local_rez)
            #print('p:',p,'     -> ',local_rez,file=self.log)
            self.logit('p:',p,'     -> ',local_rez)

            if len(local_rez)>0:
                rez[p]=max(local_rez,key=lambda _t: _t[0])

        maxrezkey = max(rez,key=lambda _t: rez[_t][0])
        if verbose>0:
            #print('rez:',rez)
            print('decided:',(maxrezkey,rez[maxrezkey]))
        #print('decided:',(maxrezkey,rez[maxrezkey]),file=self.log)
        self.logit('decided:',(maxrezkey,rez[maxrezkey]))
        return (maxrezkey,rez[maxrezkey])
            
    def verified(self,piece):
        #print('/n/n',5*'-','CALL verified','-'*5,'n\piece=',piece,file=self.log)
        self.logit('/n/n',5*'-','CALL verified','-'*5,'n\piece=',piece)
        expansions = self.zboard.valids(piece)
        #print('expansions',expansions,file=self.log)
        self.logit('expansions',expansions)
        reductions = []
        # check for hist dependant moves
        if 'c' in [ z[0] for z in expansions]: #verify for O-O
            if piece.col=='w':
                if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Ke1','Kxe1'] ]): #king moved
                    reductions.append([ z for z in expansions if z[2].count('O-O')>0 ][0] )
                else:
                    if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Rh1','Rxh1'] ]): #king's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==2 ][0] )
                    if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Ra1','Rxa1'] ]): #queen's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==3 ][0] )
            else:
                if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Ke8','Kxe8'] ]): #king moved
                    reductions.append([ z for z in expansions if z[2].count('O-O')>0 ][0] )
                else:
                    if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Rh8','Rxh8'] ]): #king's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==2 ][0] )
                    if any([ mov in [ z[2] for z in self.white['hist'] ] for mov in ['Ra8','Rxa8'] ]): #queen's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==3 ][0] )
        if 'e' in [ z[0] for z in expansions]: # verify for en passan
            for e in [ z for z in expansions if z[0]=='e' ]:
                if piece.col=='w':
                    #print(self.black['hist'][-1][2])
                    #print(e[1][0]+'5')
                    #print(e[1][0]+'6')
                    #print(self.black['hist'])
                    #print([ z[2] for z in self.black['hist'] ])
                    if self.black['hist'][-1][2]!=e[1][0]+'5' or e[1][0]+'6' in [ z[2] for z in self.black['hist'] ]:
                        #e[1][0] = the file for the destination sq in the e.p. move
                        # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'
                        reductions.append(e)
                else:
                    #print(self.white['hist'][-1][2])
                    #print(e[1][0]+'4')
                    #print(e[1][0]+'3')
                    #print(self.white['hist'])
                    #print([ z[2] for z in self.white['hist'] ])
                    if self.white['hist'][-1][2]!=e[1][0]+'4' or e[1][0]+'3' in [ z[2] for z in self.white['hist'] ]:
                        #e[1][0] = the file for the destination sq in the e.p. move
                        # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'
                        reductions.append(e)

        #print('reductions:',reductions,file=self.log)
        self.logit('reductions:',reductions)
        reduced = [ z for z in expansions if z not in reductions ]

        # add disambiguations based on other pieces of the same type being able to get to the same spot
        if piece.col == 'w':
            set_to_check = self.zboard.whites
        else:
            set_to_check = self.zboard.blacks
        disambiguations = []
        set_to_check = [ z for z in set_to_check if z.type == piece.type and z.sq != piece.sq and z.type in ['r','n','b','q'] ] # we can have multiple Q after promotion
        #print('set to check for disambiguations:',set_to_check,file=self.log)
        self.logit('set to check for disambiguations:',set_to_check)
        if len(set_to_check)>0:
            for p2c in set_to_check:
                check_exp = self.zboard.valids(p2c)
                
                for e in check_exp:
                    ambiguity = ''
                    if e in reduced:
                        ambiguity = e

                    if ambiguity != '':
                        reduced.remove(ambiguity)
                        if p2c.sq[0]==piece.sq[0]: #if both are on the same file => disambuguate by rank
                            reduced.append((ambiguity[0],ambiguity[1],ambiguity[2][0]+piece.sq[1]+ambiguity[2][1:]))
                        else: # on same rank, or at opossite corners of a rectangle => disambiguate by file
                            reduced.append((ambiguity[0],ambiguity[1],ambiguity[2][0]+piece.sq[0]+ambiguity[2][1:]))

                        #print('removed ambiguous',ambiguity,'and added disambiguated',reduced[-1],file=self.log)
                        self.logit('removed ambiguous',ambiguity,'and added disambiguated',reduced[-1])

        # print('final list to return:',reduced,file=self.log)
        return reduced

    def mate(self):
        rez=[]
        for p in self.turnset():
            rez.extend(self.verified(p))

        if len(rez)==0:
            if self.turn['is_in_check']:
                return 'mate'
            else:
                return 'stalemate'
        else:
            return ''
        
    def decode_move(self, move_notation, piece_set):
        verbose = 1
        if verbose>0:
            #print('/n/n',5*'-','CALL decode_move','-'*5,file=self.log)
            #print('decoding move:',move_notation,file=self.log)
            #print('operating piece set:',piece_set,file=self.log)
            self.logit('/n/n',5*'-','CALL decode_move','-'*5)
            self.logit('decoding move:',move_notation)
            self.logit('operating piece set:',piece_set)
        board_state = self.zboard.board
        # capture turn count if included in notation
        #p = re.compile(r'\d\.')
        move_num = re.search(r'\d\.{1,3}\s?', move_notation)
        if move_num == None:
            if verbose >0:
                #print('notation does not include turn count',file=self.log)
                self.logit('notation does not include turn count')
            zmove = move_notation
        else:
            if verbose >0:
                #print(move_num.span(),file=self.log)
                self.logit(move_num.span())
            zmove = move_notation[move_num.end():]

        #clean punctuation
        if zmove.count('?')>0:
            zmove = zmove[:zmove.find('?')]
        if zmove.count('!')>0:
            zmove = zmove[:zmove.find('!')]

        #clean/process end chars
        if zmove.count('+')>0:
            zmove = zmove[:zmove.find('+')] # check & double check
        if zmove.count('#')>0:
            zmove = zmove[:zmove.find('#')] # mate

        move = zmove # this is the value for the notation we track in the hist
        
        promo = '' #promoting a pawn i.e. e8Q
        for pz in ['R','N','B','Q']:
            if zmove[-1] == pz:
                promo = pz
        #clean the promo char, not to tip off the piece operator
        if promo != '':
            zmove=zmove[:-1]
       
        #casteling
        if zmove.count('O') == 2 or zmove.count('0') == 2:
            #king side castle
            kp = [ z for z in piece_set if z.type == 'k' ][0]
            destination = 'g'+kp.sq[1] #kp.sq[1] - the rank of king
            return (kp,('c',destination,move))

        if zmove.count('O') == 3 or zmove.count('0') == 3:
            #queen side castle
            kp = [ z for z in piece_set if z.type == 'k' ][0]
            destination = 'c'+kp.sq[1] #kp.sq[1] - the rank of king
            return (kp,('c',destination,move))

        
        #find piece type
        piece_type = 'p'
        for pz in ['R','N','B','Q','K']:
           if zmove.count(pz)>0:
               piece_type = pz
        
        #filtered = [x for x in piece_set if x.type == piece_type.lower()]
        filtered = [x for x in piece_set if x.type == piece_type.lower()]

        if len(filtered)==0:
            raise MoveException('no piece of the needed type ('+piece_type.lower()+') is found in the piece set')
        
        enpassan = False
        #find whether the move is capturing
        if zmove.count(capture_sign)>0:
            capturing = True
            destination = zmove[zmove.find(capture_sign)+1:]
            if destination not in board_state.keys():
                raise MoveException('capture sign detected in move, but destination ('+destination+') is not on the board')
            if  board_state[destination] == '  ':
                if verbose>0:
                    #print('capturing on empty sq with',destination[1],' in [3,6]',file=self.log)
                    self.logit('capturing on empty sq with',destination[1],' in [3,6]')
                if piece_type == 'p' and destination[1] in ['3','6']:
                    enpassan = True
                    if verbose>0:
                        #print('possibility of en passan detected',file=self.log)
                        self.logit('possibility of en passan detected')
                else:
                    raise MoveException(self.zboard.show(board_state)+'\ntaking empty spot '+destination+' by non pawn '+ piece_type)
        else:
            capturing = False
            if zmove.count(piece_type)>0:
                destination = zmove[zmove.find(piece_type)+1:]
            else:
                destination = zmove

        move_type = 'm'
        if capturing:
            move_type='t'
            if verbose>0:
                self.logit('enpassan',enpassan)
            if enpassan :
                move_type='e'
        if promo != '':
            move_type='p'
        if capturing and promo != '':
            move_type='+'
        
        if verbose>0:
            self.logit('move_type',move_type)
        if len(filtered)==1:
            return (filtered[0],(move_type,destination,move))

        #find if the move has disambiguation
        disambiguation = ''
        if capturing:
            if zmove[zmove.find(capture_sign)-1]!=piece_type:
                disambiguation = zmove[zmove.find(capture_sign)-1]
                #if piece_type != 'p':
                #   ambiguous = zmove[0]+zmove[zmove.find(capture_sign)]
                #else:
                #   ambiguous = zmove
        else:
            if len(destination)>2:
                disambiguation = destination[0]
                destination = destination[1:]
                #ambiguous = piece_type+destination

        if verbose >0:
            self.logit('disambigument:',disambiguation)
            self.logit('destination:',destination)
                
        if disambiguation != '':
            if disambiguation in [chr(x) for x in range(97,105)]: #disambiguation by column
                filtered = [ x for x in filtered if disambiguation == x.sq[0]]
            else: #disambiguation by rank
                filtered = [ x for x in filtered if disambiguation == x.sq[1]]

            if len(filtered)==0:
                raise MoveException('no piece matching the disambiguation ('+disambiguation+') is found in the piece set')
            if len(filtered)==1:
                return (filtered[0],(move_type,destination,move))
            
        #filter by destination
        #verbose=1 #debug
        new = []
        for x in filtered:
            exp_ = [z[1] for z in x.expand(board_state)]
            if verbose:
                self.logit(x,exp_)
            if destination in exp_:
                new.append(x)
        
        filtered = new

        if len(filtered)>1:
            raise MoveException('move is ambiguous. Possible executors:'+str(filtered))
        if len(filtered)==0:
            raise MoveException('no piece expanding to the destination ('+destination+') is found in the piece set')


        if verbose >0:
            self.logit('result:',(filtered[0],(move_type,destination,move)))

        return (filtered[0],(move_type,destination,move))

    def cycle(self,testing=[],aidepth=4,verbose=1): # verbose=1 - we want to see the board by default, and occasionaly turn it off...
        pieces_count = 32
        
        if testing != []:
            testing.append('exit')
            human_function = lambda : self.decode_move(testing.pop(0),self.turnset())
        else:
            human_function = self.prompt_human_move
        mate = self.mate()
        eksit = False
        while not eksit and mate=='':
            if verbose>0:
                print(self.show())
            
            if self.turn['player']=='human':
                #take_time_stamp
                validated_move = None
                while validated_move == None:
                    mv = human_function()
                    #print('>'+str(mv)+'<')
                    if mv == 'exit':
                        eksit = True
                        validated_move = 'exit'
                    elif mv == '':
                        validated_move = ''
                    elif mv == 'hist':
                        print(self.full_notation)
                        validated_move = ''
                    elif mv == 'export':
                        print(self.zboard.board)
                        validated_move = ''
                    elif mv == 'verbose':
                        if verbose == 0:
                            verbose=1
                        else:
                            verbose=0
                        validated_move = ''
                    else:
                        #print('mv',mv)
                        #print(' in',self.verified(mv[0]))
                        if mv[1] in self.verified(mv[0]):
                            validated_move = mv
                        else:
                            print('notation was correct, but move is invalid')
                            print('move',mv[1])
                            print('allowed moves',self.verified(mv[0]))
                            #print('notation was correct, but move is invalid -- move',mv[1],'allowed moves',self.verified(mv[0]),file=self.log)
                            self.logit('notation was correct, but move is invalid -- move',mv[1],'allowed moves',self.verified(mv[0]))
            else:
                start_stamp = time.clock()
                vm = self.AI_move(self.turn['col'],verbose) #turn_color,verbose ### used to be depth,verbose
                run_time = time.clock() - start_stamp
                validated_move = (vm[0],vm[1][-1])
                # validated_move[0] is the piece object
                # validated_move[1] has the evaluation, and sequence of moves. the last in the list [-1] is the fisrt of the sequence
                print('AI:',validated_move,' completed in:',run_time)
                self.logit('AI:',validated_move)

            #if verbose>0:
            #    print('validated_move',validated_move)
            #print('validated_move',validated_move,file=self.log)

            if not eksit and len(validated_move)>0:
                #turn_time = now - stamp
                #execute move
                self.zboard.exec_move(validated_move[0],validated_move[1])

                #memory reuse
                re_count = 64 - ''.join(self.zboard.board.values()).count('  ')
                if pieces_count != re_count:
                    pieces_count = re_count
                    to_del = [ k for k in evaluated.keys() if 64-k.count('  ')>re_count]
                    for d in to_del:
                        del evaluated[d]
                    #this is a good spot to load from pickle records for pieces_count-5
                
                self.turn['hist'].append(validated_move[1])  #  add move to hist
                #self.turn['time'] -= turn_time #  remaining time = remaining time - turn time
                #add move to full notation
                if self.turn['col'] == 'w':
                    opposite_col = self.zboard.blacks
                else:
                    opposite_col = self.zboard.whites
                kp = [ z for z in opposite_col if z.type=='k' ][0]
                
                #sq_in_check(self,sq,by_col,b_state='',verbose=0):
                check = self.zboard.sq_in_check(kp.sq,self.turn['col'])
                add_notation = validated_move[1][2]
                if check:
                    add_notation += '+'
                    
                #switch turn & #complete the move notation (disambiguation notation should be in the AI move section)
                if self.turn['col'] == 'w':
                    self.turn = self.black
                    self.full_notation += str(self.turn_count)+'. '+add_notation+' ' #move separator
                    self.turn_count +=1
                else:
                    self.turn = self.white
                    self.full_notation += add_notation+'\n'

                #  including the 'in_check' value
                self.turn['is_in_check'] = check
                #check if mate or stalemate
                mate = self.mate()

            
            
        # --------- end of while
        if verbose>0:
            print(self.full_notation)
        if mate == 'stalemate':
            self.full_notation = self.full_notation[:-2]+'\n1/2-1/2'
            return '1/2-1/2'
        if mate == 'mate':
            self.full_notation = self.full_notation[:-2]+'#\n'
            if self.turn['col']=='w':
                self.full_notation+='0-1'
                return '0-1'
            else:
                self.full_notation+='1-0'
                return '1-0'

        return 'exit'
