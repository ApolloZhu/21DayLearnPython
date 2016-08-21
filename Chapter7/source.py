import pdb
#import math

def grade(sum):
    """
    >>> grade(100)
    'A'
    >>> grade(80)
    'B'
    >>> grade(65)
    'C'
    >>> grade(10)
    'F'
    """
    if sum > 90:
        return 'A'
    elif sum > 80:
        return 'B'
    elif sum > 60:
        return 'C'
    else:
        return 'F'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    
    pdb.runcall(grade, 30)
    pdb.run("""for i in range(5):
        grade(i * 20)
    """)
