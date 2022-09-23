def bubble(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[i]>array[i+1]:
                temp=array[i+1]
                array[i+1]=array[i]
                array[i]=temp
    return array

print (bubble([12,23,12,54,23,34,67,86,98]))