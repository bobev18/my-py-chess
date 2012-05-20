# -*- coding: utf-8 -*-

import re#, sys
#global max_eval_memory_size
max_eval_memory_size = 150000
#global capture_sign
capture_sign = 'x' # this one should become class init parameter
#global pvalues
pvalues = {'p':1.0,'r':5.0,'n':3.0,'b':3.0,'q':10.0,'k':0.0,' ':0.0}
#global sqvalues
sqvalues = { 'a8':0.01, 'b8':0.01, 'c8':0.01, 'd8':0.01, 'e8':0.01, 'f8':0.01, 'g8':0.01, 'h8':0.01,
             'a7':0.01, 'b7':0.02, 'c7':0.02, 'd7':0.02, 'e7':0.02, 'f7':0.02, 'g7':0.02, 'h7':0.01,
             'a6':0.01, 'b6':0.02, 'c6':0.03, 'd6':0.03, 'e6':0.03, 'f6':0.03, 'g6':0.02, 'h6':0.01,
             'a5':0.01, 'b5':0.02, 'c5':0.03, 'd5':0.04, 'e5':0.04, 'f5':0.03, 'g5':0.02, 'h5':0.01,
             'a4':0.01, 'b4':0.02, 'c4':0.03, 'd4':0.04, 'e4':0.04, 'f4':0.03, 'g4':0.02, 'h4':0.01,
             'a3':0.01, 'b3':0.02, 'c3':0.03, 'd3':0.03, 'e3':0.03, 'f3':0.03, 'g3':0.02, 'h3':0.01,
             'a2':0.01, 'b2':0.02, 'c2':0.02, 'd2':0.02, 'e2':0.02, 'f2':0.02, 'g2':0.02, 'h2':0.01,
             'a1':0.01, 'b1':0.01, 'c1':0.01, 'd1':0.01, 'e1':0.01, 'f1':0.01, 'g1':0.01, 'h1':0.01,}

#global evaluated
evaluated = {}

def AIeval(board_state):
    hashstate = ''.join([ board_state[z] for z in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'] ])
    if hashstate in evaluated.keys():
        return evaluated[hashstate]
    
    handy = lambda sq: pvalues[board_state[sq][1]]+sqvalues[sq]
    """
    wval= 0.0
    bval= 0.0
    for sq in board_state:
        if board_state[sq][0]=='w':
            wval+=handy(sq)
        elif board_state[sq][0]=='b': #this is needed to avoid evaluating the empty squares
            bval+=handy(sq)
        else: 
            pass
    """

    val= 0.0
    for sq in board_state.keys():
        if board_state[sq][0]=='w':
            val+=handy(sq)
        elif board_state[sq][0]=='b': #this is needed to avoid evaluating the empty squares
            val-=handy(sq)
        else: 
            pass

    if len(evaluated)<max_eval_memory_size: evaluated[hashstate]=val
    return val

from board import board
from board import MoveException

class AI():
    def __init__(self,logfile='d:\\temp\\delme.txt'):#self,wplayer='human',bplayer='human',clock=60*60,logfile='d:\\temp\\chesslog.txt'):
        self.logfile=logfile#[:-4]+'_'+str(self.turn_count)+'_'+str(p)+'.txt
        with open(logfile,'w') as f:
            self.logfile = logfile #sys.stdout

    def logit(self,*args):
        data=' '.join([str(x) for x in args])
        with open(self.logfile,'a') as zlog:
            zlog.write(data+'\n')

    def clean_records(self,current_count):
        to_del = [ k for k in evaluated.keys() if 64-k.count('  ')>current_count]
        for d in to_del:
            del evaluated[d]
        #this is a good spot to load from pickle records for pieces_count-5
    """
    def AIeval(self,board_state):
        hashstate = ''.join([ board_state[z] for z in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'] ])
        if hashstate in evaluated.keys():
            return evaluated[hashstate]
        
        wval= 0.0
        bval= 0.0
        for sq in board_state:
            psq = board_state[sq]#the piece at sq
            if psq[0]=='w':
                wval+=pvalues[psq[1]]
                wval+=sqvalues[sq]
            else:# psq[0]=='b':
                bval+=pvalues[psq[1]]
                bval+=sqvalues[sq]
        if len(evaluated)<max_eval_memory_size: evaluated[hashstate]=(wval,bval)
        return (wval,bval)
    """
    
    def AIrecursion(self,boardstate,selfcol,tcol,depth,original_depth,alpha,beta,action):
        depthindent=' '*(5-depth)
        #exec_move takes piece object, which to move, and expansion in triplet 'move type', 'destination square', 'notation'
        # we have no use of the piece object, since the new board object creates new piece objects
        # we still need easy way to operate on the piece we want, so we'll use sq2exp = tuple of square of the piece, expansion
        new_state = board(boardstate)
        #if action['origin']!='':
        new_state.exec_move(new_state.piece_by_sq(action['origin']),action['move'])
        if tcol=='w':
            pieces_set=new_state.whites[:]
            opposite = 'b'
        else:
            pieces_set=new_state.blacks[:]
            opposite = 'w'

        turn_in_check = False
        # check if either side is in check >>  sq_in_check(self,sq,by_col,b_state='',verbose=0):
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ])==0:
            print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ])==0:
            print(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
        w_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ][0],'b',new_state.board)
        b_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ][0],'w',new_state.board)
        if (w_in_check and tcol=='w') or (b_in_check and tcol=='b'):
            turn_in_check = True

        ####################################################################################################################
        #                                             TERMINATION CONDITION(S)                                             #
        ####################################################################################################################
        # ignore cut at depth==0 if last turn results in check -- dig deeper
        #if depth <=0 and (sq2exp[1][2].count(capture_sign)==0 or (not w_in_check) and (not b_in_check)):
        # depth is reached or passed, last move was not capture, and no one is in check
        if depth <=0 and action['move'][2].count(capture_sign)==0 and not w_in_check and not b_in_check:
            rez = AIeval(new_state.board) # r = tuple of the value for whites in the deepest state, and the value for blacks in the deepest state
            #rez = round(r[0]-r[1],3)
            #if selfcol!='w':
            #    rez = -rez
            self.logit(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|action:',action,'state val',rez)
            return [rez,0] # [evaluation, num_of_avail_moves_on_next_level]

        self.logit(depthindent,'rec:',len(evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'w+',w_in_check,'b+',b_in_check,'|action:',action)
        moverez = []
        pruning = False
        original_length = 0
        ####################################################################################################################
        #                                                    PIECE CYCLE                                                   #
        ####################################################################################################################
        while not pruning and len(pieces_set)>0 :
            p=pieces_set.pop(0)
            expansions=new_state.valids(p)
            original_length += len(expansions)
            ###----------------------------------------------\
            ### BELOW ARE REDUCTIONS on sub-depth expansions
            if depth <=0:
                # if deepened due to capturing -> allow only further captures on the same square
                if action['move'][2].count(capture_sign)!=0:
                    expansions = [ z for z in expansions if z[0] in ['t','+','e'] and z[1]==action['move'][1] ] # i.e. check deeper only captures that take at the same sq as the last vapture
                else: # if deepened due to being check
                    reduced_expansions = []
                    for exp in expansions:
                        vboard = new_state.virt_move(p,exp)
                        if tcol =='w':
                            still_in_check = new_state.sq_in_check([ z for z in vboard.keys() if vboard[z]=='wk' ][0],'b',vboard)
                        else:
                            still_in_check = new_state.sq_in_check([ z for z in vboard.keys() if vboard[z]=='bk' ][0],'w',vboard)
                        if not still_in_check:
                            reduced_expansions.append(exp) # collects moves that escape the current check

                    #if turn_in_check and len(reduced_expansions)>0:
                    expansions = reduced_expansions

            ####################################################################################################################
            #                                                   EXPANSION CYCLE                                                #
            ####################################################################################################################
            while not pruning and len(expansions)>0:
                e = expansions.pop(0)
                #print('-- p',p,'e',e)
                #print 'sq2exp: ',sq2exp #sq2exp:  ['c7', ('m', 'c5', 'c5'), 'h4', 'h5']
                #if len(sq2exp)>2:
                #    remnant = sq2exp[2:]
                #else:
                #    remnant = []
                new_action={}
                new_action['origin']=p.sq
                new_action['move']=e
                new_action['path']=action['path']+[action['move'][2]]
                #was
                #remnant.insert(0,sq2exp[1][2])# the move destination square 
                #remnant.insert(0,e)           # the triplet defining the curent expansion
                #remnant.insert(0,p.sq)        # originating square for the move 'e'
                #print 'remnant: ',remnant # remnant:  ['f1', ('m', 'c4', 'Bc4'), 'c5', 'h4', 'h5']
                try:
                    r = self.AIrecursion(new_state.board,selfcol,opposite,depth-1,original_depth,alpha,beta,new_action)
                except MoveException as err:
                    print('********** Exception args:',str(err.args))
                    print(new_state.show())
                    print('new_state.piece_by_sq(action[origin])',new_state.piece_by_sq(action['origin']),'action[move]',action['move'])
                    print('action',action)
                    print('playin col:',selfcol)
                    print('-- p',p,'e',e)
                    #print('zr',r)
                    
                r.append(e)
                moverez.append(r)
                ###------------\\
                #    PRUNING
                if tcol==selfcol: #MAX in the cycle
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

            # --- end of expansions cycle ---------------------/

        # ---     end of the pieces cycle     ----------------/

        #next if is to cover for reduction of expasions to consequtive take squares, might get misinterpreted as mate
        # this will not be needed if we use true check for mate instead of rely on the inability to produce valid moves
        if depth<=0 and len(moverez)==0 and original_length>0:
            rez= AIeval(new_state.board)
            #rez = round(r[0]-r[1],3)
            #if selfcol!='w':
            #    rez = -rez
            #print(depthindent,'turn col:',tcol,'depth:',depth,'|sq2exe:',sq2exp[0],'mv2exe:',sq2exp[1],'state val',rez,file=self.log)
            moverez = [[rez,0]] # [evaluation, num_of_avail_moves_on_next_level]
        # ----- end of reduction <> mate disambiguation

        ####################################################################################################################
        #                                      CHOOSE BEST RESULT TO RETURN                                                #
        ####################################################################################################################
        #print(depthindent,'moverez to max/min:',moverez,file=self.log)
        if tcol==selfcol:
            if len(moverez)==0:
                thing = [-99, '#']
                #print(depthindent,'returning:',thing,file=self.log)
                self.logit(depthindent,'returning:',thing)
                if thing[0]>alpha:
                    alpha=thing[0]
            else:
                if original_depth==depth:
                    thing = sorted(moverez,key=lambda _t: _t[0])
                    #print 'thing1',thing
                else:
                    thing = max(moverez,key=lambda _t: _t[0])  # find max the score
                    somerez = [ z for z in moverez if z[0]==thing[0] ] # select all elements that have the max score
                    thing = min(somerez, key=lambda _t: _t[1]) # @_t[1] we have the number of expansions for the next turn; i.e. minimize opponents options
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
                if original_depth==depth:
                    thing = sorted(moverez,key=lambda _t: _t[0],reverse=True)
                    #print 'thing2',thing
                else:
                    thing = min(moverez,key=lambda _t: _t[0])
                    #print(depthindent,'return min moverez:',thing,file=self.log)
                self.logit(depthindent,'return min moverez:',thing)
        
            #if type(thing[0]) == list or ('m', 'h3', 'h3') in thing:
            #    print('moverez',moverez)
            #    print('thing',thing)

        if original_depth!=depth:
            thing.insert(1,len(moverez)) # number of all available moves

        #!!!! below will break as it's incompleted !!!
        if original_depth==depth:
            #thing.append(0,p.sq) # the origination sq for the _initial_ move should be returned, as its used in the validator
            #print moverez
            pass
        
        return thing
                
                
    """
    def AI_move(self,init_borad_state,lastmove,depth=5,verbose=0):
        #print('/n/n',5*'-','CALL AI_move','-'*5,file=self.log)
        self.logit('/n/n',5*'-','CALL AI_move','-'*5)
        #print('depth:',depth,file=self.log)
        self.logit('depth:',depth)
        rez = {}
        if self.turn['col']=='w':
            opposite = 'b'
        else:
            opposite = 'w'

        lm_origin=lastmove[0][0]
        #lm_piece = lastmove[0][1]
        #(filtered[0],(move_type,destination,move))
        lm_move_triplet=(lastmove[0][1],lastmove[1]) # (piece,(move_type,destination,move))
        action = {'origin':lm_origin,'move':lastmove[1],'path':[]}
        #print action
        #print 'init_borad_state',init_borad_state
        rrr = self.AIrecursion(init_borad_state,self.turn['col'],self.turn['col'],depth,depth,-999,999,action)
        #print rr #
        \"""[-0.29999999999999999, 19, 18, 0, ('m', 'h5', 'h5'), ('t', 'b5', 'Bxb5'), ('m', 'b5', 'b5')]
        [-0.26000000000000001, 30, 19, 0, ('m', 'h5', 'h5'), ('t', 'f5', 'exf5'), ('m', 'f5', 'f5')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h7', 'Rh7'), ('m', 'd4', 'd4'), ('m', 'h5', 'h5')]
        [0.68000000000000005, 30, 19, 0, ('m', 'h7', 'Rh7'), ('m', 'd4', 'd4'), ('m', 'h6', 'h6')]
        [0.68000000000000005, 31, 27, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'd5', 'd5')]
        [0.68000000000000005, 30, 27, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'd6', 'd6')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'g5', 'g5')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'g6', 'g6')]
        [0.68000000000000005, 30, 20, 0, ('m', 'g8', 'Rg8'), ('m', 'd4', 'd4'), ('m', 'h6', 'Nh6')]
        [0.68000000000000005, 30, 22, 0, ('m', 'g8', 'Rg8'), ('m', 'f3', 'Qf3'), ('m', 'f6', 'Nf6')]
        [0.68000000000000005, 30, 22, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'c5', 'c5')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'c6', 'c6')]
        [0.68000000000000005, 30, 19, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'f6', 'f6')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'b6', 'b6')]
        [0.68000000000000005, 30, 22, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'c6', 'Nc6')]
        [0.68000000000000005, 30, 20, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'a6', 'Na6')]
        [0.68000000000000005, 30, 21, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'a5', 'a5')]
        [0.68000000000000005, 30, 19, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'a6', 'a6')]
        [0.68000000000000005, 29, 29, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'e5', 'e5')]
        [0.68000000000000005, 30, 30, 0, ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'e6', 'e6')]
        \"""
        while rrr:
            rr = rrr.pop()
            print 'self.turnset()',self.turnset()
            for p in self.turnset():
                # the initial moves are the end of the queue
                movepath = [x for x in rr[1:] if isinstance(x,tuple)]
                #print movepath
                zmove= movepath[-1]
                print 'zmove',zmove
                print self.verified(p)
                if zmove in self.verified(p):
                    return [p,zmove]

        return "ERROR - no of the suggested moves is valid; unles mate - it's an error"
        
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
            #print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',x.sq
            exp_ = [z[1] for z in x.expand(board_state)]
            if verbose:
                self.logit(x,exp_)
            if destination in exp_:
                new.append((x.sq,x))
        
        filtered = new

        if len(filtered)>1:
            raise MoveException('move is ambiguous. Possible executors:'+str(filtered))
        if len(filtered)==0:
            raise MoveException('no piece expanding to the destination ('+destination+') is found in the piece set')


        if verbose >0:
            self.logit('result:',(filtered[0],(move_type,destination,move)))

        return (filtered[0],(move_type,destination,move))

    def cycle(self,testing=[],aidepth=4,verbose=1): # verbose=1 - we want to see the board by default, and occasionaly turn it off...
        old_board_state = ''
        pieces_count = 32
        previous_move = None
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
                        if mv[1] in self.verified(mv[0][1]):
                            validated_move = mv
                            previous_move = mv
                        else:
                            print('notation was correct, but move is invalid')
                            print('move',mv[1])
                            print('allowed moves',self.verified(mv[0]))
                            #print('notation was correct, but move is invalid -- move',mv[1],'allowed moves',self.verified(mv[0]),file=self.log)
                            self.logit('notation was correct, but move is invalid -- move',mv[1],'allowed moves',self.verified(mv[0]))
            else:
                start_stamp = time.clock()
                #print previous_move
                #print 'old_board_state',old_board_state
                vm = self.AI_move(old_board_state,previous_move,aidepth,verbose) #turn_color,verbose ### used to be depth,verbose
                previous_move = vm[1]
                #returns (bp@f7, [0.64000000000000001, 30, 19, 38, 0, ('m', 'f3', 'Qf3'), ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'f6', 'f6')]))
                run_time = time.clock() - start_stamp
                validated_move = [['',vm[0]],vm[1]] #?? how shall we trully validate ??
                # validated_move[0] is the piece object
                # validated_move[1] has the evaluation, and sequence of moves. the last in the list [-1] is the fisrt of the sequence
                print('AI:',vm,' completed in:',run_time)
                self.logit('AI:',vm)
                

            #if verbose>0:
            #    print('validated_move',validated_move)
            #print('validated_move',validated_move,file=self.log)

            if not eksit and len(validated_move)>0:
                #turn_time = now - stamp

                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                old_board_state = self.zboard.board.copy()
                #print 'creation',old_board_state
                #execute move
                print validated_move
                self.zboard.exec_move(validated_move[0][1],validated_move[1])

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
                #print 'prior to notation',validated_move
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
    """
