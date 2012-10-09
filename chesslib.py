# -*- coding: utf-8 -*-
import re, sys, time

#global max_eval_memory_size
#max_eval_memory_size = 150000
global capture_sign
capture_sign = 'x'
"""
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
"""
#global evaluated
#evaluated = {}

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
from ai import AI

class game():
    def __init__(self,wplayer='human',bplayer='human',clock=60*60,logfile='d:\\temp\\chesslog.txt'):
        self.zboard = board(plainboardinit)
        self.white = {'col':'w', 'player':wplayer, 'time':clock, 'hist': [], 'is_in_check':False}
        self.black = {'col':'b', 'player':bplayer, 'time':clock, 'hist': [], 'is_in_check':False}
        self.turn = self.white
        self.turn_count = 1
        self.ai = AI()
        self.full_notation = '' # quite as the values in hist, but with the count and # + ? !
        with open(logfile,'w') as f:
            self.logfile = logfile #sys.stdout
         
        #self.log = open(logfile,'w')
        #initiate the game cycle
        #self.cycle()
    
    def logit(self,*args):
        data=' '.join([str(x) for x in args])
        with open(self.logfile,'a') as zlog:
            zlog.write(data+'\n')

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

    def AI_move(self,init_borad_state,lastmove,depth=5,verbose=0):
        self.logit('/n/n',5*'-','CALL AI_move','-'*5)
        self.logit('depth:',depth,'init_borad_state',init_borad_state,'lastmove',lastmove)
        lm_move_triplet=(lastmove[2],lastmove[3],lastmove[4])
        action = {'origin':lastmove[1],'move':lm_move_triplet,'path':[]}
        #print 'action',action,'init_borad_state',init_borad_state
        #rrr = self.ai.AIrecursion(init_borad_state,self.turn['col'],self.turn['col'],depth,depth,-999,999,action)
        rrr = self.ai.Value(init_borad_state,self.turn['col'],depth,depth,-999,999,action)
        print '\n'.join([str(x)+':'+str(rrr[x]) for x in rrr])
        print '-'*10
        ######
        ## getting all the moves is needed in order to validate the history related moves (self.verified uses self.black['hist'])
        ## TODO: pass parameter in to keep track of that validation (self.verified) ((could be func))
        #print rr #
        """[-0.29999999999999999, 19, 18, 0, ('m', 'h5', 'h5'), ('t', 'b5', 'Bxb5'), ('m', 'b5', 'b5')]
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
        """
        """
        zmax=min(rrr,key=lambda z: z[0])
        tmp = [x for x in rrr if x[0]==zmax[0]] # if there are many results with the same value ...
        if len(tmp)>1:
            rrr = sorted(tmp,key=lambda _t: _t[1],reverse=True) # ... choose the one that leaves the least options for the opponent
        print '\n'.join([str(x) for x in rrr])
        print '-'*10
        while rrr:
            rr = rrr.pop()
            for p in self.turnset():
                # the initial moves are the end of the queue
                movepath = [x for x in rr[1:] if isinstance(x,tuple)]
                zmove= movepath[-1]
                #print self.verified(p)
                if zmove in self.verified(p):
                    print movepath
                    print 'piece',p,'    zmove',zmove
                    return [p,zmove]
        """
        return rrr['move']
        return "ERROR - no of the suggested moves is valid; unles mate - it's an error"
        """
        #set separate log file for each AI move, beacuse otherwise the log gets 0.5GB big
        templog = self.logfile
        alpha=-999
        beta=999
        pieces_set = self.turnset()[:]
        pruning = False
        while not pruning and len(pieces_set)>0 :
            p = pieces_set.pop(0)
            local_rez = []
            possible_moves = self.verified(p)
            if len(possible_moves)>0:
                mv_fname = self.logfile[:-4]+'_'+str(self.turn_count)+'_'+str(p)+'.txt'
                with open(mv_fname,'w') as f: # this will also close the turn specific log file 
                    pass # this is just to overwritre the previous log.
                while not pruning and len(possible_moves)>0:
                    e=possible_moves.pop(0)
                    self.log = mv_fname #switch log
                    rr = self.AIrecursion(self.zboard.board,self.turn['col'],opposite,depth,alpha,beta,{'origin':p.sq,'move':e,'path':[]})
                    rr.append(e)
                    local_rez.append(rr)
                    #pruning
                    if rr[0]>beta:
                        pruning = True
                        #print('pruned r[0]>beta',rr[0],'>',beta,'| skipping:',possible_moves,'+',pieces_set,file=self.log)
                        f.write('pruned r[0]>beta',rr[0],'>',beta,'| skipping:',possible_moves,'+',pieces_set)
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
        """
        
            
    def verified(self,piece,verbose=0):
        #print('/n/n',5*'-','CALL verified','-'*5,'n\piece=',piece,file=self.log)
        self.logit('/n/n',5*'-','CALL verified','-'*5,'n\piece=',piece)
        expansions = self.zboard.valids(piece,verbose)
        #print('expansions',expansions,file=self.log)
        self.logit('expansions',expansions)
        reductions = []
        # check for hist dependant moves
        if 'c' in [ z[0] for z in expansions]: #verify for O-O
            #print 'exp',expansions
            #print 'debug hist', self.white['hist'], self.black['hist']
            if piece.col=='w':
                if any([ mov in [ z for z in self.white['hist'] ] for mov in ['Ke1','Kxe1'] ]): #king moved
                    reductions.append([ z for z in expansions if z[2].count('O-O')>0 ][0] )
                else:
                    if any([ mov in [ z for z in self.white['hist'] ] for mov in ['Rh1','Rxh1'] ]): #king's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==2 ][0] )
                    if any([ mov in [ z for z in self.white['hist'] ] for mov in ['Ra1','Rxa1'] ]): #queen's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==3 ][0] )
            else:
                if any([ mov in [ z for z in self.black['hist'] ] for mov in ['Ke8','Kxe8'] ]): #king moved
                    reductions.append([ z for z in expansions if z[2].count('O-O')>0 ][0] )
                else:
                    if any([ mov in [ z for z in self.black['hist'] ] for mov in ['Rh8','Rxh8'] ]): #king's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==2 ][0] )
                    if any([ mov in [ z for z in self.black['hist'] ] for mov in ['Ra8','Rxa8'] ]): #queen's rook moved
                        reductions.append([ z for z in expansions if z[2].count('O')==3 ][0] )
        if 'e' in [ z[0] for z in expansions]: # verify for en passan
            for e in [ z for z in expansions if z[0]=='e' ]:
                if piece.col=='w':
                    if self.black['hist'][-1][2]!=e[1][0]+'5' or e[1][0]+'6' in [ z[2] for z in self.black['hist'] ]:
                        #e[1][0] = the file for the destination sq in the e.p. move
                        # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'
                        reductions.append(e)
                else:
                    if self.white['hist'][-1][2]!=e[1][0]+'4' or e[1][0]+'3' in [ z[2] for z in self.white['hist'] ]:
                        #e[1][0] = the file for the destination sq in the e.p. move
                        # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'
                        reductions.append(e)

        self.logit('reductions:',reductions)
        #if piece.sq=='e8' and piece.type=='k':
        #    print 'exp',expansions,'red', reductions
        reduced = [ z for z in expansions if z not in reductions ]

        # add disambiguations based on other pieces of the same type being able to get to the same spot
        if piece.col == 'w':
            set_to_disambiguate = self.zboard.whites
        else:
            set_to_disambiguate = self.zboard.blacks
        #disambiguations = []
        set_to_disambiguate = [ z for z in set_to_disambiguate if z.type == piece.type and z.sq != piece.sq and z.type in ['r','n','b','q'] ] # we can have multiple Q after promotion
        self.logit('set to check for disambiguations:',set_to_disambiguate)
        if len(set_to_disambiguate)>0:
            for p2c in set_to_disambiguate:
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

        return reduced

    def mate(self, verbose=0):
        rez=[]
        for p in self.turnset():
            temp_rez=self.verified(p,verbose)
            rez.extend(temp_rez)
            if verbose>0:
                print 'p',p,'rez',temp_rez

        if verbose>1:
            print 'mate rez (all avail moves for the pl in turn):', rez
        if verbose>0:
            print 'len avail moves:', len(rez)
            

        if len(rez)==0:
            if verbose>0:
                print 'player on turn is ',self.turn['col'],' and check against him is :',self.turn['is_in_check']
            if self.turn['is_in_check']:
                return 'mate'
            else:
                return 'stalemate'
        else:
            # repeated moves
            if len(self.zboard.backtrack)>=6 and self.zboard.backtrack[-1]==self.zboard.backtrack[-3] and self.zboard.backtrack[-1]==self.zboard.backtrack[-5] and self.zboard.backtrack[-2]==self.zboard.backtrack[-4] and self.zboard.backtrack[-2]==self.zboard.backtrack[-6]:
                print 'backtrack',self.zboard.backtrack
                return 'stalemate'
            
            return ''
        
    def decode_move(self, move_notation, piece_set):
        # format of the return is tuple of 5 elements: (piece, source_qs,move_type,destination_sq,notation)
        # first element is of class piece, and the rest are str
        verbose = 1
        if verbose>0:
            self.logit('/n/n',5*'-','CALL decode_move','-'*5)
            self.logit('decoding move:',move_notation)
            self.logit('operating piece set:',piece_set)
        board_state = self.zboard.board # {'h8': 'br', 'h2': 'wp', 'h3': '  ', 'h1': 'wr', 'h6': '  ', 'h7': 'bp', 'h4': '  ', 'h5': '  ', 'd8': 'bq', 'a8': 'br', 'd6': '  ', 'd7': 'bp', 'd4': 'bn', 'd5': '  ', 'd2': '  ', 'd3': 'wp', 'd1': 'wq', 'g7': 'bp', 'g6': '  ', 'g5': 'wb', 'g4': '  ', 'g3': '  ', 'g2': 'wp', 'g1': '  ', 'g8': '  ', 'c8': 'bb', 'c3': 'wn', 'c2': 'wp', 'c1': '  ', 'c7': 'bp', 'c6': '  ', 'c5': '  ', 'c4': 'wb', 'f1': '  ', 'f2': 'wp', 'f3': '  ', 'f4': '  ', 'f5': '  ', 'f6': 'bn', 'f7': 'bp', 'f8': '  ', 'b4': '  ', 'b5': '  ', 'b6': '  ', 'b7': 'bp', 'b1': '  ', 'b2': 'wp', 'b3': '  ', 'b8': '  ', 'a1': 'wr', 'a3': 'wp', 'a2': '  ', 'a5': '  ', 'e8': '  ', 'a7': 'bp', 'a6': '  ', 'e5': 'bp', 'e4': 'wp', 'e7': 'bk', 'e6': '  ', 'e1': 'wk', 'e3': '  ', 'e2': '  ', 'a4': '  '}
        
        # capture turn count if included in notation
        move_num = re.search(r'\d\.{1,3}\s?', move_notation)
        if move_num == None:
            zmove = move_notation
            if verbose >0: self.logit('notation does not include turn count')
        else:
            zmove = move_notation[move_num.end():]
            if verbose >0: self.logit('move number',move_num.span())

        #clean punctuation, #clean/process end chars
        if zmove.count('?')>0:
            zmove = zmove[:zmove.find('?')]
        if zmove.count('!')>0:
            zmove = zmove[:zmove.find('!')]
        if zmove.count('+')>0:
            zmove = zmove[:zmove.find('+')] # check & double check
        if zmove.count('#')>0:
            zmove = zmove[:zmove.find('#')] # mate

        move = zmove.strip() # this is the format for the notation we track in the hist
        promo = '' #promoting a pawn i.e. e8Q
        for pz in ['R','N','B','Q']:
            if zmove[-1] == pz:
                promo = pz
        if promo != '': 
            zmove=zmove[:-1] #clean the promo char, not to tip off the piece dicovery
       
        #casteling
        if zmove.count('O') == 2 or zmove.count('0') == 2: #king side castle
            kp = [ z for z in piece_set if z.type == 'k' ][0]
            destination = 'g'+kp.sq[1] #kp.sq[1] - the rank of king
            return (kp,kp.sq,'c',destination,move)

        if zmove.count('O') == 3 or zmove.count('0') == 3: #queen side castle
            kp = [ z for z in piece_set if z.type == 'k' ][0]
            destination = 'c'+kp.sq[1]
            return (kp,kp.sq,'c',destination,move)
        
        #find piece type
        piece_type = 'p'
        for pz in ['R','N','B','Q','K']:
            if zmove.count(pz)>0:
                piece_type = pz
            elif zmove.count(pz)>1:
                raise MoveException('more than one reference to piece type '+pz+' is found in the notation'+move_notation)

        #list pieces matching the found type
        filtered = [x for x in piece_set if x.type == piece_type.lower()]
        if len(filtered)==0:
            raise MoveException('no piece of the needed type ('+piece_type.lower()+') is found in the piece set')

        move_type = ''
        enpassan = False
        #find whether the move is capturing
        if zmove.count(capture_sign)>0:
            capturing = True
            move_type='t'
            destination = zmove[zmove.find(capture_sign)+1:]
            if destination not in board_state.keys():
                raise MoveException('capture sign detected in move, but destination (',destination,') is not on the board')
            if  board_state[destination] == '  ':
                if verbose>0: self.logit('capturing on empty sq with',destination[1],' in [3,6]')
                if piece_type == 'p' and destination[1] in ['3','6']:
                    enpassan = True #possibility yet -- will get verified through matching expansion
                    move_type='e'
                    if verbose>0: self.logit('possibility of en passan detected')
                else:
                    raise MoveException(self.zboard.show(board_state)+'\ntaking empty spot '+destination+' by non pawn '+ piece_type)
        else:
            capturing = False
            if zmove.count(piece_type)>0:
                destination = zmove[zmove.find(piece_type)+1:]
            else:
                destination = zmove

        if promo != '':
            move_type='p'
            if capturing:
                move_type='+'
        if move_type=='':
            move_type = 'm'
        
        if verbose>0: self.logit('move_type',move_type)
        if len(filtered)==1:
            return (filtered[0],filtered[0].sq,move_type,destination,move)

        #find if the move has disambiguation
        disambiguation = ''
        if capturing:
            if zmove[zmove.find(capture_sign)-1]!=piece_type: #true for pawn capture moves
                disambiguation = zmove[:zmove.find(capture_sign)-1] # the pawn file "cxd5"
            else:
                disambiguation = zmove[1:zmove.find(capture_sign)-1] # the pawn file "cxd5"
            if len(disambiguation)>2:
                raise MoveException('\n erroneous disambiguation '+disambiguation)
        else:
            if len(destination)==3: # Rac1 = Rook from file "A" to "C1" ; N7g5 = Knight from rank "7" to "G5" 
                disambiguation = destination[0]
                destination = destination[1:]
            elif len(destination)==4: # Nf7g5 differ from both Nh7 and Nf3 - you can have 3 pieces of same type after promotions
                disambiguation = destination[:2]
                if disambiguation not in board_state.keys():
                    raise MoveException('disambiguation detected ('+disambiguation+'), but it is not on the board')
                destination = destination[2:]
                if destination not in board_state.keys():
                    raise MoveException('destination detected as ('+destination+'), but it is not on the board')
            elif len(destination)>4:
                raise MoveException('\n erroneous destination '+destination)
            else:
                pass

        if verbose >0:
            self.logit('disambigument:',disambiguation)
            self.logit('destination:',destination)

        #filter by disambiguation        
        if len(disambiguation)>0:
            if len(disambiguation)==1:
                if disambiguation in [chr(x) for x in range(97,105)]: 
                    filtered = [ x for x in filtered if disambiguation == x.sq[0]] #disambiguation by file
                else: 
                    filtered = [ x for x in filtered if disambiguation == x.sq[1]] #disambiguation by rank
            else:
                filtered = [ x for x in filtered if disambiguation == x.sq] #disambiguation by origination square
                
            if len(filtered)==0:
                raise MoveException('no piece matching the disambiguation ('+disambiguation+') is found in the piece set')
            if len(filtered)==1:
                return (filtered[0],filtered[0].sq,move_type,destination,move)
            
        #filter by destination
        new = []
        for x in filtered:
            exp_ = [z[1] for z in x.expand(board_state)]
            if verbose: self.logit(x,exp_)
            if destination in exp_:
                new.append(x)
        filtered = new

        if len(filtered)>1:
            raise MoveException('move is ambiguous. Possible executors:'+str(filtered))
        if len(filtered)==0:
            raise MoveException('no piece expanding to the destination ('+destination+') is found in the piece set')
        if verbose >0:  self.logit('result:',(filtered[0],(move_type,destination,move)))
        return (filtered[0],filtered[0].sq,move_type,destination,move)

    def cycle(self,testing=[],aidepth=4,verbose=1): # verbose=1 - we want to see the board by default, and occasionaly turn it off...
        old_board_state = ''
        validated_move = None
        #pieces_count = 32
        #previous_move = None
        if testing != []:
            testing.append('exit')
            human_function = lambda : self.decode_move(testing.pop(0),self.turnset())
        else:
            human_function = self.prompt_human_move
        mate = self.mate()
        eksit = False
        while not eksit and mate=='':
            if verbose>0:
                print self.show()
            
            if self.turn['player']=='human':
                #take_time_stamp
                validated_move = None
                while validated_move == None:
                    mv = human_function()
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
                        verified_moves = self.verified(mv[0])
                        if (mv[2],mv[3],mv[4]) in verified_moves:
                            validated_move = mv
                            #previous_move = mv
                        else:
                            if verbose>0:
                                print('notation was correct, but move is invalid')
                                print('move',mv)
                                print('allowed moves',verified_moves)
                            self.logit('notation was correct, but move is invalid -- move',mv,'allowed moves',verified_moves)
            else:
                start_stamp = time.clock()
                if verbose>0:
                    print 'AI ('+self.turn['col']+') starts at time:',time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())

                if validated_move==None:
                    validated_move=(self.zboard.piece_by_sq('g8'), '', 'm', 'g8', 'Ng8') #(wp@e4, 'e2', 'm', 'e4', 'e4')
                    old_board_state = self.zboard.board.copy()
                    
                #print 'validated_move format',validated_move
                
                vm = self.AI_move(old_board_state,validated_move,aidepth,verbose) #turn_color,verbose ### used to be depth,verbose
                #vm = self.AI_move(self.zboard.board.copy(),validated_move,aidepth,verbose) #turn_color,verbose ### used to be depth,verbose
                # note: validated_move was previous_move, but since it has the same value...
                
                #previous_move = vm[1]
                #returns (bp@f7, [0.64000000000000001, 30, 19, 38, 0, ('m', 'f3', 'Qf3'), ('m', 'h5', 'h5'), ('m', 'd4', 'd4'), ('m', 'f6', 'f6')]))
                run_time = time.clock() - start_stamp
                #validated_move = (vm[0],'',vm[1][0],vm[1][1],vm[1][2]) #?? how shall we trully validate ??
                # validated_move[0] is the piece object
                # validated_move[1] has the evaluation, and sequence of moves. the last in the list [-1] is the fisrt of the sequence

                validated_move = (self.zboard.piece_by_sq(vm['origin']),vm['origin'],vm['move'][0],vm['move'][1],vm['move'][2])
                ## ~~ self.zboard.exec_move(validated_move[0],(validated_move[2],validated_move[3],validated_move[4]))
                # def exec_move(self,piece,exp,verbose=0):#,virtual=False):
                
                if verbose >0:
                    print('AI:',vm,' completed in:',run_time)
                self.logit('AI:',vm)
                
            if not eksit and len(validated_move)>0:
                #turn_time = now - stamp

                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                old_board_state = self.zboard.board.copy()
                
                #execute move
                if verbose >0: print validated_move
                self.zboard.exec_move(validated_move[0],(validated_move[2],validated_move[3],validated_move[4]))
                if verbose>1:
                    print 'self.zboard.winch & binch:',self.zboard.winch,self.zboard.binch
                    print 'self.turn["col"] ',self.turn['col'] 

                #print self.show()

                #memory reuse
                if validated_move[2] == 't':
                    self.ai.clean_records(64 - self.zboard.board.values().count('  '))

                #add history record
                self.turn['hist'].append(validated_move[4])  #  add move to hist
                #self.turn['time'] -= turn_time #  remaining time = remaining time - turn time

                #add move to full notation
                if self.turn['col'] == 'w':
                    #opposite_col = self.zboard.blacks
                    kp = self.zboard.bk
                else:
                    #opposite_col = self.zboard.whites
                    kp = self.zboard.wk

                
                #kp = [ z for z in opposite_col if z.type=='k' ][0]
                
                check = self.zboard.sq_in_check(kp,self.turn['col'],verbose=0)
                #print 'cycle in_check check',check


                #:run breaks on the line below because formatting returned by the AI differes from the one returned by the decode_move !!!
                add_notation = validated_move[4]
                
                if check:
                    add_notation += '+'
                    
                #switch turn & complete the move notation (disambiguation notation should be in the AI move section)
                if self.turn['col'] == 'w':
                    self.turn = self.black
                    self.full_notation += str(self.turn_count)+'. '+add_notation+' ' #move separator
                    self.turn_count +=1
                else:
                    self.turn = self.white
                    self.full_notation += add_notation+'\n'

                #calculating the 'in_check' value
                self.turn['is_in_check'] = check
                #check if mate or stalemate
                mate = self.mate(verbose=0)
                if verbose>1:
                    print 'self.zboard.winch & binch:',self.zboard.winch,self.zboard.binch
                    print 'self.turn["col"] ',self.turn['col'] 
                    print 'self.turn["is_in_check"] ',self.turn['is_in_check'] 
                    print 'mate detected as',mate
        
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
