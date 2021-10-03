

def sort(seq=[]):
    '''
    Sort a sequence in ascending order, and return the sorted sequence.

    It should work equally well on strings or numbers.
    '''

    # The code that follows is a very lazy and non-performant sort, but I believe that it works.
    
    ans = []
    src = [e for e in seq]
    while len(src) > 0:
        m = min(src)
        ans.append(m)
        src.remove(m)
    return ans


def deduplicate():
    pass