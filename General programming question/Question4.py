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

# Write a function that takes a string as parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers, whose sum is 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers then your program should return false 
# as well.
# Example1: input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb" output = False (the two numbers do not sum to 10)
# Example2: input = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb" output = True (the two numbers sum to 10)
# weight = 8

def question_mark(example1):
    sum=0
    sum_of_number=0
    list1=[]
    list2=[]
    for i in example1:
        for j in range(0,10): #本文里面的数字属于String
            if i==str(j):    
                sum+=1
                sum_of_number+=int(i)
    print(sum)
    print(sum_of_number)
    if sum !=2 and sum_of_number != 10:
        return False 
    else:
        for i in range(len(example1)):
            for j in range(0,10):
                if example1[i]==str(j):
                    list1.append(i)
            
        for i in example1[list1[0]:list1[-1]+1]:
            list2.append(i)
        print(list2)
    a="?"
    sum_of_Question_mark=0

    for i in list2:
        if i == a:
            sum_of_Question_mark+=1
    
    if sum_of_Question_mark==3 and sum_of_number==10:

        return True
    else:
        return False
    




input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfk" 
input2 = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb"
print(question_mark(input2))
