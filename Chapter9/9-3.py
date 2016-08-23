def generate(start, end = None, step=1):
    if step == 0:
        raise ValueError("step of generate must not be 0")
    elif step > 0:
        predicate = lambda lhs, rhs: lhs < rhs
    else:
        predicate = lambda lhs, rhs: lhs > rhs
    
    current = start
    exit = end
    if end == None:
        current = 0
        exit = start
    
    while predicate(current, exit):
        yield current
        current += step

if __name__ == "__main__":
    import pdb
    pdb.set_trace()
