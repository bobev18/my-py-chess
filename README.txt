my-py-chess
===========

basic chess featuring move validation and stupid AI
###################################################

Usage:
   1. Import the main module
     import chesslib

   2. Initialize game - 
     # by default both players are human
     # mygame = chesslib.game()
     
     # for AI playing black 
     mygame = chesslib.game(bplayer='ai',logfile='test.txt') 
     
     # you can set both players to AI
     # mygame  = chesslib.game(wplayer='ai',bplayer='ai',logfile='ai_vs_ai_test.txt')

  3. Start the game
     mygame.cycle(aidepth=3,verbose=0)
     # default verbose is 1, and show bunch of info on the AI move evaluation

  4. enter '?' to see ingame commands
  
  As per version 0.8, at depth 4, which is the default value, the AI will take average about 2 min to move
  AI vs AI game at aidepth=5 did 33 moves for total of 2h

  5. you can preset position by dict of the following kind
    mygame.zboard.piecefy({'h8': 'bk', 'h2': '  ', 'h3': '  ', 'h1': '  ', 'h6': '  ', 'h7': '  ', 'h4': '  ', 'h5': '  ', 'd8': '  ', 'a8': '  ', 'd6': '  ', 'd7': '  ', 'd4': '  ', 'd5': '  ', 'd2': '  ', 'd3': '  ', 'd1': '  ', 'g7': '  ', 'g6': '  ', 'g5': '  ', 'g4': '  ', 'g3': '  ', 'g2': '  ', 'g1': '  ', 'g8': '  ', 'c8': '  ', 'c3': '  ', 'c2': '  ', 'c1': '  ', 'c7': '  ', 'c6': '  ', 'c5': '  ', 'c4': '  ', 'f1': '  ', 'f2': '  ', 'f3': '  ', 'f4': '  ', 'f5': '  ', 'f6': '  ', 'f7': '  ', 'f8': '  ', 'b4': '  ', 'b5': '  ', 'b6': '  ', 'b7': '  ', 'b1': '  ', 'b2': '  ', 'b3': '  ', 'b8': '  ', 'a1': '  ', 'a3': '  ', 'a2': '  ', 'a5': '  ', 'e8': '  ', 'a7': '  ', 'a6': '  ', 'e5': 'bq', 'e4': '  ', 'e7': '  ', 'e6': '  ', 'e1': 'wk', 'e3': '  ', 'e2': 'wq', 'a4': '  '})

  Use command ?export to print the current game board in such dict
  
  6. You can feed sequence like so:
    mygame.cycle(testing=['1.e4','b6','2.d4','Bb7','3.Bd3','f5','4.exf5','Bxg2','5.Qh5+','g6','6.fxg6','Nf6','7.gxh7+','Nxh5'])
  
  Unless you add 'exit' at the end of the move sequence, the game will be handed to the players as initialized.
  The result of the command ?hist could be adjusted to be used as feed sequence

So far:
 - worked with unittest, and build some tests
 - basic AI in place - playable at search depth 4
   = uses pruning and cache for evaluated states, did some optimisation on validations
   = Disabled sub-depth evaluation of critical positions to optimise speed. AI wasn't smart but somewhat resilient when it was enabled
   = Disabled subdepth search for check & capture positions -- that actually added the vast overhead on search. 
 - various tasks completed:
   AI moves show the time they took in seconds
   history could be feeded as game sequence
   added disambiguation in the expand function
 - show timestamp at start of the AI move
 - help menu for the in game commands
 - Undo -- undoes 1 move per each player == undoes a whole turn

TODOs:
 - Main
   = add ?resign and ?draw commands
   = figure out a way to do more encapsulation on the classes
*  = review and adjust naming conventions, clean up of commented out code
   = add ?stats to show mem size (&usage)
   = Savegame. push/pull to text -> easy way to restore last state
     ~ representation should be lib independant i.e. standard algebric notation
   = add the clocks
   + make threades, and add option for AI thinking during opponent's time
   + maybe rewrite the move_decode using reg ex (check with gives better speed)
   + rewrite board class & scrap piece class. compare AI timing

 - the AI
   = add call counter on the recursion calls and sub depth recursion calls
*  = fix AI logs + add option to manage detailness of the AI logs (detailed are needed only for analysis of the evaluation func)
   = add option for search cut, based on time
   = verbose & time the main search tree branches
*  = record entire tree, not just evaluation result of the state
   = Improve evaluation
     ~ hit heat pattern
   = Optimize speed
!!!   ~ reuse branches where the opponent's move is calculated, but not evaluated as optimal, thus expanding only one level at the leaf nodes
       ~~ it's the propagation of the values of the new leafs that determines the optimal path/move, so the comparisons at each node are still needed
       ~~ there is still much sense in the concept, as currently we decide posible moves anew at every branch, and we have already done so for all except the end nodes
       ?? consider using http://networkx.lanl.gov/index.html for the game tree
     ~ etudes and endgame by the book
     ~ AI eval to return func? Have evaluation that will determine the best evaluation function ???
     ~ replace ifs with trys

 - Testing
   = add basic AI tests. Just eval on predefined boardstate with couple of different depth settings for the AI
     ~ state with no check/capture, with key move on depth 4
     ~ state with check - with key move beyond depth 4
     ~ capture collision (whether to initiate exchange or no)
   = add tests for draws by "imposible to mate" i.e. king and knight vs king

 - Conceptual
   = extract all log functionality to class/decorators
   = experiment with dynamic switch of classes - save game state, init new class objects, load state

 - Bugs
   = Currently catches only king vs king, and should catch draws of King+light vs king & etc
   = Vertical disambiguation of moves is not generated in the expansions list, causing such moves not to be accepted by the prompt
   = AI fails to prefer mate in 1 move compared to mate in 4 moves
