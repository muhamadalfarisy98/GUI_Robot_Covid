#https://www.decalage.info/en/python/print_list

#test
#for comma seperated string
list_int=[80,443,8080,8081]
a=str(list_int).strip('[]')
print(a)


# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
        
        
# Driver code     
s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s))  


# Python program to convert a list 
# to string using join() function 
    
# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
        
        
# Driver code     
s = ['Geeks', 'for', 'Geeks'] 
print(listToString(s))  
w=''

print(w)


s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in s]) 

print(type(listToStr))
print(listToStr)  
my_list= listToStr.split()
print(my_list)
