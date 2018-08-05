'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    #pass
    # add your code here
    l = len(text)
    a1 = text
    a2 = {}
    i = 0
    
    while i < l    
        if a1[i] in a2:
            a2[a1[i]] = a2[a1[i]] + 1
        else
            a2[a1[i]] = 1
        i++
        
    for key,value in a2.items():
        print(key,str(value))
        
def count_char_insensitive(text):
    #pass
    # add your code here
    l = len(test)
    a1 = test
    a2 = {}
    i = 0
    
    a1 = test.lower()
    
    while i < l    
        if a1[i] in a2:
            a2[a1[i]] += 1
        else
            a2[a1[i]] = 1
        i++   
        
        
    for key,value in a2.items():
        print(key,str(value))
    

# bonus task:
def count_char_ordered(text):
    pass
    # add your code here 
    

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

