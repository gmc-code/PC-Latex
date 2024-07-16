from math import floor

def stemplot(data,leafdigits):
    d = []
    interval = int(10**int(leafdigits))
    for val in sorted(data):
        val = int(floor(val))
        stm, lf = divmod(val,interval)
        d.append( (int(stm), int(lf)) )
    stems, leafs = list(zip(*d))
    # print(stems, leafs)
    # stemwidth = max(len(str(x)) for x in stems)
    # leafwidth = max(len(str(x)) for x in leafs)
    laststemused = min(stems) - 1
    out = ""
    title = (f'\n\nKey:\n Stem multiplier: {interval}\n X | Y  =>  {interval}*X+Y\n')
    for s,l in d:
        #first time with new stem
        if laststemused < s:
            laststemused += 1
            out +=f'\n{s} | {l}'
        else:
            # jsut add leaf with same stem
            out +=f' {l}'

    return title, out

if __name__ == '__main__':
    print( stemplot(data0)[0], stemplot(data0)[1])