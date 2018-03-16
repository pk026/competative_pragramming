def return_missing_and_repeating(array, size):
    for i in range(size):
        if array[abs(array[i])-1] > 0:
            array[abs(array[i])-1] = -array[abs(array[i])-1]
        else:
            print "The repeating element is", abs(array[i])
    for i in range(size):
        if array[i] > 0:
            print "and the missing element is",i+1