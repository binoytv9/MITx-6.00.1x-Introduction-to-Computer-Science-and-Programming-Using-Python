def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    i = 0
    new = tuple()
    while i < len(aTup):
        new += (aTup[i],)
        i += 2
    return new

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
