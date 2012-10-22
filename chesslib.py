# -*- coding: utf-8 -*-
import re, sys, time

global capture_sign
capture_sign = 'x'

plainboardinit = {'a8':'br', 'b8':'bn', 'c8':'bb', 'd8':'bq', 'e8':'bk', 'f8':'bb', 'g8':'bn', 'h8':'br',
                 'a7':'bp', 'b7':'bp', 'c7':'bp', 'd7':'bp', 'e7':'bp', 'f7':'bp', 'g7':'bp', 'h7':'bp',
                 'a6':'  ', 'b6':'  ', 'c6':'  ', 'd6':'  ', 'e6':'  ', 'f6':'  ', 'g6':'  ', 'h6':'  ',
                 'a5':'  ', 'b5':'  ', 'c5':'  ', 'd5':'  ', 'e5':'  ', 'f5':'  ', 'g5':'  ', 'h5':'  ',
                 'a4':'  ', 'b4':'  ', 'c4':'  ', 'd4':'  ', 'e4':'  ', 'f4':'  ', 'g4':'  ', 'h4':'  ',
                 'a3':'  ', 'b3':'  ', 'c3':'  ', 'd3':'  ', 'e3':'  ', 'f3':'  ', 'g3':'  ', 'h3':'  ',
                 'a2':'wp', 'b2':'wp', 'c2':'wp', 'd2':'wp', 'e2':'wp', 'f2':'wp', 'g2':'wp', 'h2':'wp',
                 'a1':'wr', 'b1':'wn', 'c1':'wb', 'd1':'wq', 'e1':'wk', 'f1':'wb', 'g1':'wn', 'h1':'wr',}

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
        self.undo_stack = []
        self.ai = AI()
        self.full_notation = '' # quite as the values in hist, but with the count and # + ? !
        with open(logfile,'w') as f:
            self.logfile = logfile #sys.stdout
    
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
            if len(inp)>0 and inp[0] != '?':
                try:
                    mv = self.decode_move(inp,self.turnset())
                except MoveException as err:
                    print 'erroneous move',err.args
                    print 'enter "?" to view commands'
            elif inp[0] == '?':
                if inp == '?' or inp == '?help':
                    print 'commands:\n?hist - show game notation\n?export - print position as dict\n?verbose - tongle verbose on and off\n?undo - revert full turn\n?exit - exit the game'
                    print 'advanced: ?eval(...) ; ?preval(...) - the second executes in the game cycle(for better scope)'
                    inp = None
                elif inp.count('?eval')>0:
                    print eval(inp[6:-1])
                    inp = None
                elif inp.count('?preval')>0:
                    mv = inp[3:]
                else:
                    mv = inp[1:]
            else:
                pass
        
        return mv #returns move or command
            
    def verified(self,piece,verbose=0):
        # uses prevalidate of checks and verifies any history dependent moves
        self.logit('/n/n',5*'-','CALL verified','-'*5,'n\piece=',piece)
        expansions = self.zboard.valids(piece,verbose)
        #print('expansions',expansions,file=self.log)
        self.logit('expansions:',expansions)
        reduced = []
        if piece.col == 'w':
            castle_row = '1'
            hist = self.white['hist']
        else:
            castle_row = '8'
            hist = self.black['hist']

        for expansion in expansions:
            reduced.append(expansion)
            if expansion[2]=='O-O' and ('Ke'+castle_row in hist or 'Kxe'+castle_row in hist or 'Rh'+castle_row in hist or 'Rxh'+castle_row in hist): #king's rook moved
                    reduced.pop()
            if expansion[2]=='O-O-O' and ('Ke'+castle_row in hist or 'Kxe'+castle_row in hist or 'Ra'+castle_row in hist or 'Rxa'+castle_row in hist): #queen's rook moved
                    reduced.pop()
                   
            if expansion[0]=='e': # verify for en passan
                if piece.col=='w':
                    if self.black['hist'][-1].count(expansion[1][0]+'5')==0 or expansion[1][0]+'6' in self.black['hist']:
                        #e[1][0] = the file for the destination sq in the e.p. move
                        # to reduce the e.p move, we want last move to be different from 'f5', or for hist to has move 'f6'
                        reduced.pop()
                else:
                    if self.white['hist'][-1].count(expansion[1][0]+'5')==0 or expansion[1][0]+'6' in self.white['hist']:
                        reduced.pop()

        self.logit('reduced:',reduced)

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
        # draw - no one could possibly mate
        if len(self.zboard.whites)+len(self.zboard.blacks)==2:
            return 'stalemate'

        # reduced ability to move
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
            if len(self.zboard.backtrack)>0 and self.zboard.backtrack.count(self.zboard.backtrack[-1])>=3:
                if verbose>0:
                    print 'backtrack',self.zboard.backtrack
                return 'stalemate'
            
            return ''
        
    def decode_move(self, move_notation, piece_set,verbose=0):
        # format of the return is tuple of 5 elements: (piece, source_qs,move_type,destination_sq,notation)
        # first element is of class piece, and the rest are str
        if move_notation=='exit' or move_notation.count('eval(')>0 or move_notation.count('undo')>0:
            return move_notation
        if verbose >1:
            print 'move_notation', move_notation
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
            msg = 'no piece of the needed type ('+piece_type.lower()+') is found in the piece set'
            raise MoveException(msg)

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

    def turnundo(self, verbose=0):
        #undoes whole turn i.e. it's white to move, they make undo, which reverses both black's last move, and whites last move
        #once
        if verbose>0:
            print 'self.undo_stack',self.undo_stack
        last = self.undo_stack.pop()
        if verbose>0: 
            print last
        self.zboard.undo_move(last)
        self.white['hist'].pop()  #  erase move from hist
        #twice
        if verbose>0:
            print 'self.undo_stack',self.undo_stack
        last = self.undo_stack.pop()
        if verbose>0: 
            print last
        self.zboard.undo_move(last)
        self.black['hist'].pop()  #  erase move from hist

        #self.zboard.ak below are handled by the 'data' record on the board.undo, so they will be valid
        if self.turn['col'] == 'w':
            self.turn['is_in_check'] = self.zboard.sq_in_check(self.zboard.wk,'b',verbose=0)
        else:
            self.turn['is_in_check'] = self.zboard.sq_in_check(self.zboard.bk,'w',verbose=0)

        self.turn_count -=1 # regardless of current color, we are reversing entire turn, so no conditions...

    def cycle(self,testing=[],aidepth=4,verbose=1): # verbose=1 - we want to see the board by default, and occasionaly turn it off...
        old_board_state = self.zboard.board.copy()
        validated_move = None
        mate = self.mate()
        eksit = False
        while not eksit and mate=='':
            if verbose>0:
                print self.show()
                print 'turn:',self.turn_count
            
            if self.turn['player']=='human':
                #take_time_stamp
                validated_move = None
                while validated_move == None:
                    if testing != []:
                        mv = self.decode_move(testing.pop(0),self.turnset(),verbose=0)
                    else:
                        mv = self.prompt_human_move()

                    if mv == 'exit':
                        eksit = True
                        validated_move = 'exit'
                    elif mv == '':
                        validated_move = ''
                    elif mv == 'hist':
                        print '\n'.join([ str(i+1)+'. '+self.white['hist'][i]+' '+self.black['hist'][i] for i in range(len(self.black['hist']))]), \
                              ('\n'+str(len(self.white['hist']))+'. '+self.white['hist'][-1])*(len(self.black['hist'])<len(self.white['hist']))
                        validated_move = ''
                    elif mv == 'export':
                        print self.zboard.board
                        validated_move = ''
                    elif mv == 'undo':
                        self.turnundo(verbose)
                        validated_move = ''
                    elif mv.count('eval')>0:
                        print 'mv',mv,'mv command', mv[5:-1]
                        eval(mv[5:-1])
                        validated_move = ''
                    elif mv == 'verbose':
                        if verbose == 0:
                            verbose=1
                        else:
                            verbose=0
                        validated_move = ''
                    else:
                        verified_moves = self.verified(mv[0]) #mv[0] is the piece
                        if (mv[2],mv[3]) in [(z[0],z[1]) for z in verified_moves]: # move type, destination sq, notation 
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
                
                vm = self.ai.AI_move(old_board_state,validated_move,self.turn['col'],self.white['hist'],self.black['hist'],aidepth,verbose) #turn_color,verbose ### used to be depth,verbose
                run_time = time.clock() - start_stamp
                validated_move = (self.zboard.piece_by_sq(vm['origin']),vm['origin'],vm['move'][0],vm['move'][1],vm['move'][2])
                if verbose >0:
                    print('AI:',vm,' completed in:',run_time)
                self.logit('AI:',vm)
                
            if not eksit and len(validated_move)>0:
                #turn_time = now - stamp
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                old_board_state = self.zboard.board.copy() # used to create ai_board
                
                #execute move
                if verbose >0:
                    print validated_move
                self.undo_stack.append(self.zboard.exec_move(validated_move[0],(validated_move[2],validated_move[3],validated_move[4])))
                if verbose>1:
                    print 'self.zboard.winch & binch:',self.zboard.winch,self.zboard.binch
                    print 'self.turn["col"] ',self.turn['col'] 

                #memory reuse
                if validated_move[2] == 't':
                    self.ai.clean_records(64 - self.zboard.board.values().count('  '))

                #switch turn & and check if the new player is in check
                if self.turn['col'] == 'w':
                    self.turn_count +=1
                    self.turn = self.black
                    self.turn['is_in_check'] = self.zboard.sq_in_check(self.zboard.bk,'w',verbose=0)
                    self.white['hist'].append(validated_move[4]+'+'*self.turn['is_in_check'])
                else:
                    self.turn = self.white
                    self.turn['is_in_check'] = self.zboard.sq_in_check(self.zboard.wk,'b',verbose=0)
                    self.black['hist'].append(validated_move[4]+'+'*self.turn['is_in_check'])
               
                #check if mate or stalemate
                mate = self.mate(verbose=0)
                if verbose>1:
                    print 'self.zboard.winch & binch:',self.zboard.winch,self.zboard.binch
                    print self.white['hist']+'\n'+self.black['hist']
                    print 'self.turn["is_in_check"] ',self.turn['is_in_check'] 
                    print 'mate detected as',mate
        
        # --------- end of while not eksit and mate=='':
        if verbose>0:
            print self.show()
            print self.white['hist']
            print self.black['hist']
            self.full_notation = '\n'.join([ str(i+1)+'. '+self.white['hist'][i]+' '+self.black['hist'][i] for i in range(len(self.black['hist']))])+ \
                                 ('\n'+str(len(self.white['hist']))+'. '+self.white['hist'][-1])*(len(self.black['hist'])<len(self.white['hist']))

        result = 'exit'
        if mate == 'stalemate':
            self.full_notation += '\n1/2-1/2'
            result = '1/2-1/2'
        if mate == 'mate':
            if self.turn['col']=='w':
                result = '0-1'
            else:
                result = '1-0'
            self.full_notation = self.full_notation[:-1]+'#\n'+result

        if verbose>0:
            print self.full_notation
        
        return result
