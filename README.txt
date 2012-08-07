my-py-chess
===========

basic chess featuring move validation and stupid AI
###################################################

So far:
 - worked with unittest, and build acceptable set of tests
 - basic AI in place - playable at search depth 4 (pushing it at 4 = 2 moves for each player (midgame averages 3min per move with max at 6min))
   = uses pruning and cache for evaluated states, did some optimisation on validations
   = Disabled sub-depth evaluation of critical positions to optimise speed. AI wasn't smart but somewhat resilient when it was enabled
   = Disabled subdepth search for check & capture positions -- that actually added the vast overhead on search. 
 - various tasks completed:
   added clock on AI moves
   history could be feeded as game sequence
   added disambiguation in the expand function
 - changed the return format to tuple of five elements
 - spit time at start of the AI move

TODOs:
 - Main
   = figure out a way to do more encapsulation on the classes
*  = review and adjust naming conventions, clean up of commented out code
   = show move count
   = add help instructions
   = undo
   = add ?stats to show mem size (&usage)
   = prep AI vs AI mode, which will be used for (speed) testing
   = Savegame. push/pull to text -> easy way to restore last state
     ~ representation should be lib independant i.e. standard algebric notation
   = add the clock to the human player too
   + maybe rewrite the move_decode using reg ex (check with gives better speed)
   ? rewrite board class & scrap piece class. compare AI timing

 - the AI
   = add call count on the recursion calls and sub depth recursion calls
*  = fix AI logs + add option to manage detailness of the AI logs (detailed are needed only for analysis of the evaluation func)
   = add option for search cut based on time
   = verbose & time the main search tree branches
   = Improve evaluation
*    ~ pass markers on history dependant moves (i.e. use the path from previous move to eval the new state
     ~ hit heat pattern
   = Optimize speed
     ~ etudes and endgame by the book
     ~ AI eval to return func? Have evaluation that will determine the best evaluation function ???
     ~ replace ifs with trys

 - Testing
   = add basic AI tests. Just eval on predefined boardstate with couple of different depth settings for the AI
     ~ state with no check/capture, with key move on depth 4
     ~ state with check - with key move beyond depth 4
     ~ capture collision (whether to initiate exchange or no)

 - Conceptual
   = extract all log functionality to class/decorators
   = experiment with dynamic switch of classes - save game state, init new class objects, load state




