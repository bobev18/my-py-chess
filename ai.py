# -*- coding: utf-8 -*-

## https://www.ai-class.com/course/video/quizquestion/194
# Unit 13.6
#

import re
import copy
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

from board import board
from board import MoveException

class AI():
    def __init__(self,logfile='d:\\temp\\delme.txt'):
        self.evaluated = {}
        self.max_eval_memory_size = 1000000
        self.capture_sign = 'x'
        self.undo_stack = []
        self.game_hist = {'w':[],'b':[]}
        self.logfile=logfile#[:-4]+'_'+str(self.turn_count)+'_'+str(p)+'.txt
    
    def logit(self,*args):
        pass
        """
        data=' '.join([str(x) for x in args])
        with open(self.logfile,'a') as zlog:
            zlog.write(data+'\n')
        """

    def clean_records(self,current_count):
        to_del = [ k for k in self.evaluated.keys() if 64-k.count('  ')>current_count]
        for d in to_del:
            del self.evaluated[d]

    def AICalc(self,board_state):
        # moved the calculation to another func, to determine the effect of the cache
        val= 0.0
        for sq in board_state:
            if board_state[sq][0]=='w':
                val+=pvalues[board_state[sq][1]]+sqvalues[sq]
            if board_state[sq][0]=='b': #this is needed to avoid evaluating the empty squares
                val-=pvalues[board_state[sq][1]]+sqvalues[sq]
                
        val = round(val,3)
        return val

    def AI_move(self,init_borad_state,lastmove,turn_col,w_game_hist,b_game_hist,depth=5,verbose=0):
        self.logit('/n/n',5*'-','CALL AI_move','-'*5)
        self.logit('depth:',depth,'init_borad_state',init_borad_state,'lastmove',lastmove)

        self.game_hist['w']=w_game_hist
        self.game_hist['b']=b_game_hist
        if lastmove != None:
            lm_move_triplet=(lastmove[2],lastmove[3],lastmove[4])
            action = {'origin':lastmove[1],'move':lm_move_triplet,'path':[]}
        else:
            action = {'origin':'','move':'','path':[]}
        ai_board = board(init_borad_state)
        rrr = self.Value(ai_board,turn_col,depth,depth,-999,999,action)
        if verbose>0:
            print rrr
            print '\n'.join([str(x)+':'+str(rrr[x]) for x in rrr])
            print '-'*10
        return rrr['move']
        return "ERROR - no of the suggested moves is valid; unles mate - it's an error"
    
    def AIeval(self,board_state,hashstate):
        try:
            return self.evaluated[hashstate]
        except KeyError as e:
            val = self.AICalc(board_state)
            if len(self.evaluated) < self.max_eval_memory_size:
                self.evaluated[hashstate]=val
            return val
    
    def verified(self,tcol,action,verbose=0):
        # check for validity of history dependant moves
        whiset = self.game_hist['w'] + action['path']
        bhiset = self.game_hist['b'] + action['path']
        
        if action['move'][0] == 'c': #verify for O-O
            #print 'exp',expansions
            #print 'debug hist', self.white['hist'], self.black['hist']
            if tcol=='w':
                if 'Ke1' in whiset or 'Kxe1' in whiset:
                    return False #king moved
                if action['move'][2] == 'O-O':
                    if 'Rh1' in whiset or 'Rxh1' in whiset:
                        return False #h rook moved
                else: #O-O-O
                    if 'Ra1' in whiset or 'Rxa1' in whiset:
                        return False #a rook moved
            else:
                if 'Ke8' in bhiset or 'Kxe8' in bhiset:
                    return False #king moved
                if action['move'][2] == 'O-O':
                    if 'Rh8' in bhiset or 'Rxh8' in bhiset:
                        return False #h rook moved
                else: #O-O-O
                    if 'Ra8' in bhiset or 'Rxa8' in bhiset:
                        return False #a rook moved

        if action['move'][0]=='e': # verify for en passan
            if tcol=='w':
                if bhiset[-1]!=action['move'][1][0]+'5' or action['move'][1][0]+'6' in bhiset:
                    return False
                    #action['move'][1][0] = the file for the destination sq in the e.p. move
                    # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'

            else:
                if whiset[-1]!=action['move'][1][0]+'4' or action['move'][1][0]+'3' in whiset:
                    return False

        return True

    def maxValue(self,ai_board,tcol,depth,original_depth,alpha,beta,expansions, path):
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
                
                result = self.Value(ai_board,opposite,depth-1,original_depth,alpha,beta,new_action)
                if result != 'invalid':
                    try:
                        result['path'].insert(0,e)
                    except KeyError as ee:
                        print 'received emty dict, because '
                        print 'EVERYTHING'
                        print ai_board.show()
                        print "action['origin']",new_action['origin']
                        print "action['move']",new_action['move']
                        print "action['path']",new_action['path']
                        print result
                        print ee
                    result['move']=new_action
                    if result['score']>score:
                        score=result['score']
                        best_result = result
                        
                    if score >= beta:
                        return result
                    alpha = max(alpha,score)

        return best_result

    def minValue(self,ai_board,tcol,depth,original_depth,alpha,beta,expansions, path):
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
                
                result = self.Value(ai_board,opposite,depth-1,original_depth,alpha,beta,new_action)
                if result != 'invalid':
                    result['path'].insert(0,e)
                    result['move']=new_action
                    if result['score']<score:
                        score=result['score']
                        best_result = result
                        
                    if score <= alpha:
                        return result
                    beta = min(beta,score)

        return best_result

    def Value(self,ai_board,tcol,depth,original_depth,alpha,beta,action):
        depthindent=' '*(5-depth)
        result = {'move':action,'score':0,'path':[],'rem_exp':-1}
        
        if action['origin'] != '': #no origin, means no previous move exists
            if (action['move'][0]=='c' or action['move'][0]=='e') and not self.verified(tcol,action,verbose=0):
                return 'invalid'

            try:
                process_move = ai_board.exec_move(ai_board.piece_by_sq(action['origin']),action['move'],verbose=0)
            except MoveException as ee:
                print '<><>',action,'col', tcol,'bk pos', ai_board.bk
                print 'something went wrong ',ee
                print ai_board.show()
                print "action['origin']",action['origin']
                print "action['move']",action['move']
                print "action['path']",action['path']
                print 'retrying'
                process_move = ai_board.exec_move(ai_board.piece_by_sq(action['origin']),action['move'],verbose=1)

            if process_move != None:
                self.undo_stack.append(process_move)
            else:
                return 'invalid'
        else:
             ai_board.backtrack.append('')
             self.undo_stack.append([['data', ai_board.wk, ai_board.bk, ai_board.winch, ai_board.binch]])
        
        if tcol=='w':
            pieces_set=ai_board.whites[:] #[:] because we pop 'em during cycling
            opposite = 'b'
        else:
            pieces_set=ai_board.blacks[:]
            opposite = 'w'

        if (ai_board.winch and tcol=='w') or (ai_board.binch and tcol=='b'):
            turn_in_check = True
        else:
            turn_in_check = False            

        # and finaly get the expand list
        expansions = {}
        exp_count = 0
        for p in pieces_set:
            expansions[p] = p.expand(ai_board.board)
            exp_count += len(expansions[p])

        # if we have reached cutoff depth and the last move has no capture or check:
        if depth <=0:# and action['move'][2].count(self.capture_sign)==0 and not w_in_check and not b_in_check:
            result['score'] = self.AIeval(ai_board.board,ai_board.hashit())
            result['rem_exp']=exp_count
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',ai_board.winch,'b+',ai_board.binch,'|action:',action,'state val',result)
            popped = self.undo_stack.pop()
            try:
                ai_board.undo_move(popped)
            except MoveException as ee:
                print '<.>',action,'col', tcol,'bk pos', ai_board.bk
                print 'something went wrong during undo@cutoff ',ee
                print 'popped',popped
                print ai_board.show()
                print "action['origin']",action['origin']
                print "action['move']",action['move']
                print "action['path']",action['path']
                print 'retrying'
                ai_board.undo_move(popped,verbose=1)
            
            return result # result = {'move':action,'score':State evaluation,'path':[],'rem_exp': # of possible expansion }
            # this is returned only towards minV/maxV functions

        # teminal state
        if exp_count==0:
            # check if mate or stalemate
            if turn_in_check: 
                score = 99
            else:
                score = 60 # later we need to adjust this depending on whether we want draw
            #check if mate is for the white
            if tcol=='w':
                score=-score
            result['score'] = score
            result['rem_exp']=0
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',ai_board.winch,'b+',ai_board.binch,'|action:',action,'state val',result)
            try:
                ai_board.undo_move(self.undo_stack.pop())
            except MoveException as ee:
                print '<:>',action,'col', tcol,'bk pos', ai_board.bk
                print 'something went wrong during undo@old terminal state ',ee
                print ai_board.show()
                print "action['origin']",action['origin']
                print "action['move']",action['move']
                print "action['path']",action['path']
                print 'retrying'
                ai_board.undo_move(self.undo_stack.pop(),verbose=1)
            return result # this should return only towards minV/maxV functions; if it returns to main, it means mate check failed

        # maximizing state
        if tcol=='w':
            rez = self.maxValue(ai_board,tcol,depth,original_depth,alpha,beta,expansions,action['path'][:])
        if tcol=='b':
            rez = self.minValue(ai_board,tcol,depth,original_depth,alpha,beta,expansions,action['path'][:])
        
        # new terminal condition is having rez=={} (not using prevalidation for expansions, so it had invalid moves in the initial expands)
        if rez == {}:
            # check if mate or stalemate
            if turn_in_check: 
                score = 99
            else:
                score = 60 # later we need to adjust this depending on whether we want draw
            #check if mate is for the white
            if tcol=='w':
                score=-score
            result['score'] = score
            result['rem_exp']=0
            self.logit(depthindent,'rec:',len(self.evaluated),'turn col:',tcol,'depth:',depth,'w+',ai_board.winch,'b+',ai_board.binch,'|action:',action,'state val',result)
            try:
                ai_board.undo_move(self.undo_stack.pop())
            except MoveException as ee:
                print '<!>',action,'col', tcol,'bk pos', ai_board.bk
                print 'something went wrong during undo@new terminal state ',ee
                print ai_board.show()
                print "action['origin']",action['origin']
                print "action['move']",action['move']
                print "action['path']",action['path']
                print 'retrying'
                ai_board.undo_move(self.undo_stack.pop(),verbose=1)
            return result # this should return only towards minV/maxV functions, otherwise mate check failed

        if len(self.undo_stack)>0:
            try:
                ai_board.undo_move(self.undo_stack.pop())
            except MoveException as ee:
                print '<><>',action,'col', tcol,'bk pos', ai_board.bk
                print 'something went wrong during undo@recursion exit ',ee
                print ai_board.show()
                print "self.undo_stack",self.undo_stack
                print "action['origin']",action['origin']
                print "action['move']",action['move']
                print "action['path']",action['path']
                print 'retrying'
                ai_board.undo_move(self.undo_stack.pop())

        return rez
        #### - Note - ###
        # The max/min doesn't depend on the self_color, because if AI is playing White, it still needs to calculate
        # the best move for the human opponent (Black), and that will still be min() since smaller state evaluation result
        # means it's better possition for Black!!!
        #### -------- ###
    
