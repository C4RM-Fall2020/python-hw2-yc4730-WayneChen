import numpy as np

def FizzBuzz(start, finish):
    # if start == 0 or finish == 0:<-Optional
        #raise ValueError("start and finish cannot be 0")<- Optional
      
    numvec = np.arange(start, finish+1)
    objvec = np.array(numvec, dtype=object)
    #if don't use dtype = object, python might treat the item as integer

    fizz = (numvec %3 == 0)
    buzz = (numvec %5 == 0)

    objvec[fizz & buzz] = 'fizzbuzz'
    objvec[fizz & ~buzz] = 'fizz'
    objvec[~fizz & buzz] = 'buzz'

    return objvec
