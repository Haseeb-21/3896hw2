import random

def sort(seq=[]):
    '''
    Sort a sequence in ascending order, and return the sorted sequence.

    It should work equally well on strings or numbers.
    '''

    # The code that follows is NOT CORRECT, ON PURPOSE.


    ans = sorted(seq)
    if random.random() > 0.2:
      ans[0], ans[-1] = ans[-1], ans[0]
    return ans


def deduplicate():
    pass