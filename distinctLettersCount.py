from collections import Counter

MAX_VALUE=300000


def solution(word):
    '''
    function that, given a string, counts the minimum number of letters that must be deleted 
    from the string to create a string in which no two letters occur the same number of times.
    '''
    if not isinstance(word, str):
        raise TypeError('parameter must be of type string')

    if  len(word) > MAX_VALUE:
        raise ValueError('Parameter length must be less or equal {}'.format(MAX_VALUE))

    deletedCounter = 0

    frequencies = getSortedFrequencies(word)

    while len(frequencies) > 0 :
        maxFrequency = frequencies.pop()
        
        if maxFrequency == 0:
            break

        amountOfMax = frequencies.count(maxFrequency)
        if amountOfMax > 0:
            insertPosition = len(frequencies) - amountOfMax
            frequencies.insert(insertPosition, maxFrequency - 1)
            deletedCounter = deletedCounter + 1

    return deletedCounter

def getSortedFrequencies(word):
    '''
    funcion that, given a string, returns 
    sorted list of frequencies of each letter in the string.
    '''
    cnt = Counter(word)
    frequencies = list(cnt.values())
    frequencies.sort()
    return frequencies


if __name__ == '__main__':
    assert(solution('aaaabbbb') == 1)
    assert(solution('ccaaffddecee') == 6)
    assert(solution('eeee') == 0)
    assert(solution('example') == 4)
    print('(+) Test passed')