'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).




'''

# Write a function that returns the largest value that is also an even value in the
# input dictionary whose values are all whole numbers (values, not keys).
# # weight = 5 

def value_greatest_even(dictionary1):
    list1=[]
    
    for i in dictionary1.values():
        if i % 2==0:
            list1.append(i)
    print(list1)
    
    
 
    '''for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            a=list1[i]
            list1[i]=list1[i+1]
            list1[i+1]=a'''
    
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                a=list1[i]
                list1[i]=list1[j]
                list1[j]=a
    print(list1)
            
    

    


dict={"number":1,"number2":8,"number3":2,"number4":10,"number5":4}
print(value_greatest_even(dict))