

def sort(seq=[]):
    '''
    Sort a sequence in ascending order, and return the sorted sequence.

    It should work equally well on strings or numbers.
    '''

    # The code that follows is a very lazy and non-performant sort, but I believe that it works.
    
    ans = [e for e in seq]
    src = [e for e in seq]
    for i in range(len(src)):
        m = min(src)
        ans[i] = m
        src.remove(m)
    return ans


def deduplicate():
    pass