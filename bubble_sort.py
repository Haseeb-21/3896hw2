def sort(seq=[]):
    ans = [e for e in seq]
    for i in range(len(ans)):
        for j in range(1, len(ans)-i):
            if ans[j] < ans[j-1]:
                ans[j], ans[j-1] = ans[j-1], ans[j]
    return ans