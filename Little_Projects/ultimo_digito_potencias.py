def ld(a, b):
    d = ['0','1','2486','3971','46','5','6','7431','8426','91']
    n = d[int(str(a)[-1])]
    return int(n[b%len(n)-1])

def nums(a, b):
    return int(str(a**b)[-1]) == ld(a, b)
