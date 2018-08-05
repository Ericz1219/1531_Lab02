def find_reverse(numbers):
    #TODO: find the reverse of the list
    numbers.reverse()
    return numbers
    pass

def find_max(numbers):
    #TODO: find the maximum of the list
    
    return max(numbers)
    pass

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)
    pass

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list

    return sum(numbers)
    pass

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    
    return sum(numbers)/len(numbers)
    pass

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    numbers.sort().reverse()
    #numbers = numbers[::-1]
    return numbers
    pass

def second_smallest(numbers):
    #TODO: find the second smallest
    numbers.sort()
    
    for i in numbers
        if i==0
            i++
        elif(numbers[i]>numbers[i-1])
            return numbers[i]
    pass


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    numbers.sort()
    for i in numbers
        if(i==0) i++
        elif(k==i+1)
        return numbers[i]
        i++
        
    pass
