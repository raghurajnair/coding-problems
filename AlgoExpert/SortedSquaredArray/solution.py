def sortedSquaredArray(array):
    resultSet = []
    left_pointer = 0
    right_pointer = len(array)-1
    for num in array:
        resultSet.append(0)
        
    for idx in reversed(range(len(array))):
        if abs(array[right_pointer]) > abs(array[left_pointer]):
            resultSet[idx] = array[right_pointer]*array[right_pointer]
            right_pointer -= 1
        else:
            resultSet[idx] = array[left_pointer]*array[left_pointer]
            left_pointer += 1
    
    return resultSet