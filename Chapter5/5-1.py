def insertionSort(seq = None, operator = lambda lhs, rhs: lhs < rhs):
    seq = [] if seq == None else seq
    for i in range(len(seq)):
        for j in range(i,0,-1):
            if not(operator(seq[j-1], seq[j])):
                temp = seq[j-1]
                seq[j-1]=seq[j]
                seq[j]=temp
            else:
                break
    return seq
