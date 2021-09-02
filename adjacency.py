# Check If Adjacent Cells Contain Consecutive Numbers
# var0 is checked with all the variables in argv
# argv may contain non-fixed number of variables
def adjacency(var0, *argv):
    passed = False
    
    for var in argv:
        passed = passed or abs(var0 - var) == 1
        if passed: break

    return passed