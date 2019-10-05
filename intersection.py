#intersection.py

def intersection(arrOne, arrTwo):
    if arrOne == None or arrTwo == None or min(len(arrOne), len(arrTwo)) == 0:
         return []

    # If the given arrays are sorted, we can use a different
    # strategy where we progressively remove from 

    retArr = []
    arrOneIndex = 0
    arrTwoIndex = 0
    while arrOneIndex < len(arrOne) and arrTwoIndex < len(arrTwo):
        if arrOne[arrOneIndex] == arrTwo[arrTwoIndex]:
            retArr.append(arrOne[arrOneIndex])
            arrOneIndex += 1
            arrTwoIndex += 1
        elif arrOne[0] > arrTwo[0]:
            # This means arrTwo is too small and needs larger values
            arrTwoIndex += 1
        else:
            # This means arrOne is too small and needs larger values
            arrOneIndex += 1
    return retArr


print(intersection(None, []))
