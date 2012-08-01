my-py-chess
===========

basic chess featuring move validation and stupid AI
###################################################

So far:
 - worked with unittest, and build good set of tests
 - basic AI in place - playable at search depth 3 (pushing it at 4 = 2 moves for each player (midgame goes to 1.5h move time))
   = uses pruning and cache for evaluated states, but no real optimisation was added i.e. could brush good deal once ready
   = AI not smart but somewhat resilient
   = subdepth search for check & capture positions -- that actually adds the vast overhead on search. Prior to adding this, depth 4 was playable
 - various tasks completed:
   added clock on AI moves
   history could be feeded as game sequence
   added disambiguation in the expand function
   fixed: error on certain returns of the verify method were returning move representation (a,(c,d,e)) instead of the new ((a,b),(c,d,e))

In this branch:
 - changed the return format to tuple of five elements, but some other methods still take old format as input
 - spit time at start of the AI move
 - changes to the AIEval caused issues
1. e4 Nf6
2. Nc3 e6
3. Bb5 c6
4. Ba4 Qb6
5. Bb3 Qxf2+
 - 

TODOs:
 - Main
*  + change the structure returned by the validation from ((a,b),(c,d,e)) to single tuple or dict
   = figure out a way to do more encapsulation on the classes
*  = review and adjust naming conventions, clean up of commented out code
   = show move count
   = add help instructions
   = undo
   = add ?stats to show mem size (&usage)
   (= prep AI vs AI mode, which will be used for (speed) testing)
   = push/pull to text -> easy way to restore last state
     ~ representation should be lib independant i.e. standard algebric notation
   = add the clock to the human player too
   + maybe rewrite the move_decode using reg ex (check with gives better speed)
*  + rewrite board class & scrap piece class. compare AI timing (currently 

 - the AI
   = add call count on the recursion calls and sub depth recursion calls
*  = fix AI logs + add option to manage detailness of the AI logs (detailed are needed only for analysis of the evaluation func)
   = add option for search cut based on time
   = verbose & time the main search tree branches
   = Improve evaluation
*    ~ pass markers on history dependant moves
     ~ hit heat pattern
   = Optimize speed
     ~ etudes and endgame by the book
     ~ AI eval to return func?
     ~ replace ifs with trys

 - Testing
   = add testing on the disambiguation after the expand
   = add basic AI tests. Just eval on predefined boardstate with couple of different depth settings for the AI
     ~ state with no check/capture, with key move on depth 4
     ~ state with check - with key move beyond depth 4
     ~ capture collision 

 - Conceptual
   = extract all log functionality to class/decorators
   = experiment with dynamic switch of classes - save game state, init new class objects, load state



---------------------------------------------------------
>>>>>>>>>> BRANCH "validation_ret_restruct": <<<<<<<<<<<<
---------------------------------------------------------
 * The validation return is restructured
 * Broke the AI, and reverting seems way back, so I re-wrote it
 * New AI is not any better in performance, but is a bit simpler in structure
 * Got "c:\Python26\python.exe -m cProfile c:\gits\my-py-chess\unitt.py" to find the time hole:
   - 179.407sec  ai.py:53(AIeval)
   - 191.796sec  board.py:277(validate_move)
       - 184.368sec  board.py:314(sq_in_check)
   - 67.379sec  {method 'keys' of 'dict' objects} due to 7 614 286 calls
 
 >>ToDo
 - board.py line 350: change the check -- apparantly too expensive as it currently is


