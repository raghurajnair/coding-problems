def isValidSubsequence(array, sequence):
    array_pointer = 0
    sequence_pointer = 0
    while array_pointer < len(array):
        if array[array_pointer] == sequence[sequence_pointer]:
            array_pointer += 1
            sequence_pointer += 1
            if sequence_pointer == len(sequence):
                return True
        else:
            array_pointer += 1

    if sequence_pointer == len(sequence):
        return True
    else:
        return False