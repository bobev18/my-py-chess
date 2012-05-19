my-py-chess
===========

basic chess featuring move validation and stupid AI

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
