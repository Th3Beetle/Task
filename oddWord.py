MIN_VALUE = 1
MAX_VALUE = 200000

def solution(stringLength):
    '''
    function that, given an integer N, returns 
    a string consisting of N lowercase letters 
    such that each letter occurs an odd number of times.
    '''
    if not isinstance(stringLength, int):
        raise ValueError('parameter must be integer')
    if stringLength < MIN_VALUE or stringLength > MAX_VALUE:
        raise ValueError('parameter must be between {} and {}'.format(MIN_VALUE, MAX_VALUE))

    return ('a' * stringLength) if (stringLength % 2) != 0 else ('a' * (stringLength - 1) + 'b')