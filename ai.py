# -*- coding: utf-8 -*-

## https://www.ai-class.com/course/video/quizquestion/194
# Unit 13.6
#

import re#, sys
#global max_eval_memory_size
#max_eval_memory_size = 150000
#global capture_sign
#capture_sign = 'x' # this one should become class init parameter
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
#evaluated = {}

def hashit(board_state):
    return board_state["a1"]+board_state["a2"]+board_state["a3"]+board_state["a4"]+board_state["a5"]+board_state["a6"]+board_state["a7"]+board_state["a8"]+board_state["b1"]+board_state["b2"]+board_state["b3"]+board_state["b4"]+board_state["b5"]+board_state["b6"]+board_state["b7"]+board_state["b8"]+board_state["c1"]+board_state["c2"]+board_state["c3"]+board_state["c4"]+board_state["c5"]+board_state["c6"]+board_state["c7"]+board_state["c8"]+board_state["d1"]+board_state["d2"]+board_state["d3"]+board_state["d4"]+board_state["d5"]+board_state["d6"]+board_state["d7"]+board_state["d8"]+board_state["e1"]+board_state["e2"]+board_state["e3"]+board_state["e4"]+board_state["e5"]+board_state["e6"]+board_state["e7"]+board_state["e8"]+board_state["f1"]+board_state["f2"]+board_state["f3"]+board_state["f4"]+board_state["f5"]+board_state["f6"]+board_state["f7"]+board_state["f8"]+board_state["g1"]+board_state["g2"]+board_state["g3"]+board_state["g4"]+board_state["g5"]+board_state["g6"]+board_state["g7"]+board_state["g8"]+board_state["h1"]+board_state["h2"]+board_state["h3"]+board_state["h4"]+board_state["h5"]+board_state["h6"]+board_state["h7"]+board_state["h8"]

from board import board
from board import MoveException

class AI():
    def __init__(self,logfile='d:\\temp\\delme.txt'):#self,wplayer='human',bplayer='human',clock=60*60,logfile='d:\\temp\\chesslog.txt'):
        self.evaluated = {}
        self.max_eval_memory_size = 1000000
        self.capture_sign = 'x'

        
        self.logfile=logfile#[:-4]+'_'+str(self.turn_count)+'_'+str(p)+'.txt

    def logit(self,*args):
        data=' '.join([str(x) for x in args])
        with open(self.logfile,'a') as zlog:
            zlog.write(data+'\n')

    def clean_records(self,current_count):
        to_del = [ k for k in self.evaluated.keys() if 64-k.count('  ')>current_count]
        for d in to_del:
            del self.evaluated[d]
        #this is a good spot to load from pickle records for pieces_count-5

    def AICalc(self,board_state):
        # moved the calculation to another func, to determine the effect of the cache
        val= 0.0
        for sq in board_state:
            if board_state[sq][0]=='w':
                val+=pvalues[board_state[sq][1]]#+sqvalues[sq]
            if board_state[sq][0]=='b': #this is needed to avoid evaluating the empty squares
                val-=pvalues[board_state[sq][1]]#+sqvalues[sq]
                
        #print hashstate,'     rezval',val
        val = round(val,3)
        return val
    
    def AIeval(self,board_state):
        hashstate = hashit(board_state) #''.join([ board_state[z] for z in ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'] ])
        #if hashstate in self.evaluated.keys():
        try:
            return self.evaluated[hashstate]
        except KeyError as e:
            val = self.AICalc(board_state)
            if len(self.evaluated) < self.max_eval_memory_size:
                self.evaluated[hashstate]=val
            return val
            
        '''        
        #handy = lambda sq: pvalues[board_state[sq][1]]+sqvalues[sq]
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
        for sq in board_state:
            if board_state[sq][0]=='w':
                val+=pvalues[board_state[sq][1]]#+sqvalues[sq]
            if board_state[sq][0]=='b': #this is needed to avoid evaluating the empty squares
                val-=pvalues[board_state[sq][1]]#+sqvalues[sq]
                
        #print hashstate,'     rezval',val
        val = round(val,3)
            
        if len(self.evaluated) < self.max_eval_memory_size:
            self.evaluated[hashstate]=val
        return val
        '''

    """
    def maxValue(self,boardstate,tcol,depth,original_depth,alpha,beta,expansions, path):
        if tcol=='w':
            opposite = 'b'
        else:
            opposite = 'w'
        score = -999
        best_action = {}
        for p in expansions.keys():
            for e in expansions[p]:
                new_action={}
                new_action['origin']=str(p)[-2:]
                new_action['move']=e
                #print 'max new_action path',e,e[2]
                new_action['path']=path+[e[2]]
                r=self.Value(boardstate,opposite,depth-1,original_depth,alpha,beta,new_action)
                if r>score:
                    score = r
                    best_action=new_action
                if score >= beta:
                    return [score, new_action]
                alpha = max(alpha,score)

        return [score,best_action]
    """


    def maxValue(self,boardstate,tcol,depth,original_depth,alpha,beta,expansions, path):
        if tcol=='w':
            opposite = 'b'
        else:
            opposite = 'w'
        score = -999
        best_result = {}
        for p in expansions.keys():
            for e in expansions[p]:
                new_action={}
                
                new_action['origin']=str(p)[-2:]
                new_action['move']=e
                #print 'min new_action path',e,e[2]
                new_action['path']=path+[e[2]]
                
                result = self.Value(boardstate,opposite,depth-1,original_depth,alpha,beta,new_action)
                result['path'].insert(0,e)
                result['move']=new_action
                if result['score']>score:
                    score=result['score']
                    best_result = result
                    
                if score >= beta:
                    return result
                alpha = max(alpha,score)

        return best_result

    def minValue(self,boardstate,tcol,depth,original_depth,alpha,beta,expansions, path):
        if tcol=='w':
            opposite = 'b'
        else:
            opposite = 'w'
        score = 999
        best_result = {}
        for p in expansions.keys():
            for e in expansions[p]:
                new_action={}
                
                new_action['origin']=str(p)[-2:]
                new_action['move']=e
                #print 'min new_action path',e,e[2]
                new_action['path']=path+[e[2]]
                
                result = self.Value(boardstate,opposite,depth-1,original_depth,alpha,beta,new_action)
                result['path'].insert(0,e)
                result['move']=new_action
                if result['score']<score:
                    score=result['score']
                    best_result = result
                    
                if score <= alpha:
                    return result
                beta = min(beta,score)

        return best_result

    def Value(self,boardstate,tcol,depth,original_depth,alpha,beta,action):
        depthindent=' '*(5-depth)
        result = {'move':action,'score':0,'path':[],'rem_exp':-1}

        #matecheck uses the extend anyways... so we might as well use it
        # first we need to push the move
        #print "action['origin']",action['origin']
        #print "action['move']",action['move']
        new_state = board(boardstate)
        new_state.exec_move(new_state.piece_by_sq(action['origin']),action['move'])
        
        if tcol=='w':
            pieces_set=new_state.whites[:]
            opposite = 'b'
        else:
            pieces_set=new_state.blacks[:]
            opposite = 'w'

        
        # then, check if either side is in check >>  sq_in_check(self,sq,by_col,b_state='',verbose=0):
        turn_in_check = False
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ])==0:
            print(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ])==0:
            print(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
        w_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='wk' ][0],'b',new_state.board)
        b_in_check = new_state.sq_in_check([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ][0],'w',new_state.board)
        if (w_in_check and tcol=='w') or (b_in_check and tcol=='b'):
            turn_in_check = True

        # and finaly get the expand list
        expansions = {}
        exp_count = 0
        for p in pieces_set:
            expansions[p]=new_state.valids(p)
            exp_count += len(expansions[p])
        
        # if we have reached cutoff depth and the last move has no capture or check:
        if depth <=0:# and action['move'][2].count(self.capture_sign)==0 and not w_in_check and not b_in_check:
            result['score'] = self.AIeval(new_state.board) # r = tuple of the value for whites in the deepest state, and the value for blacks in the deepest state
            result['rem_exp']=exp_count
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|action:',action,'state val',result)
            return result # result = {'move':action,'score':State evaluation,'path':[],'rem_exp': # of possible expansion }
            # this is returned only towards minV/maxV functions

        # teminal state
        if exp_count==0:
            # check if mate or stalemate
            if turn_in_check: 
                score = 99
            else:
                score = 60 # later we need to adjust this depending on whether we want remi
            #check if mate is for the white
            if tcol=='w':
                score=-score
            result['score'] = score
            result['rem_exp']=0
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|action:',action,'state val',result)
            return result # this is/(should be) returned only towards minV/maxV functions

        # maximizing state
        if tcol=='w':
            rez = self.maxValue(new_state.board,tcol,depth,original_depth,alpha,beta,expansions,action['path'][:])
        if tcol=='b':
            rez = self.minValue(new_state.board,tcol,depth,original_depth,alpha,beta,expansions,action['path'][:])
        # rez === result in terms of structure and expected values :: result = {'move':action,'score':0,'path':[],'rem_exp':-1}
        # might need to adjust path here?

        if 1==0: 
            print 'boardstate', boardstate
            print 'tcol',tcol
            print 'depth',depth
            print 'original_depth',original_depth
            print 'alpha',alpha
            print 'beta',beta
            print 'expansions',expansions
            print 'action[\'path\']',action['path']


        #print 'z rez:', rez
        return rez
        #### - Note - ###
        # The max/min doesn't depend on the self_color, because if AI is playing White, it still needs to calculate
        # the best move for the human opponent (Black), and that will still be min() since the low value of the state
        # means it's better possition for the Black!!!
        #### -------- ###
        
            
            
        
    
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
            print(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
        if len([ z for z in new_state.board.keys() if new_state.board[z]=='bk' ])==0:
            print(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'|action:',action)
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
        if depth <=0 and action['move'][2].count(self.capture_sign)==0 and not w_in_check and not b_in_check:
            rez = self.AIeval(new_state.board) # r = tuple of the value for whites in the deepest state, and the value for blacks in the deepest state
            #rez = round(r[0]-r[1],3)
            #if selfcol!='w':
            #    rez = -rez
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',w_in_check,'b+',b_in_check,'|action:',action,'state val',rez)
            return [rez,0] # [evaluation, num_of_avail_moves_on_next_level]

        self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'alpha',alpha,'beta',beta,'w+',w_in_check,'b+',b_in_check,'|action:',action)
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
                if action['move'][2].count(self.capture_sign)!=0:
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
            rez= self.AIeval(new_state.board)
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
            #print 'to be returned',thing
            pass

        return thing
