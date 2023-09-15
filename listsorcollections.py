#qn.change 80 to 89 and add a new item to the list. 
    # the item value will be 55.(append 55)
    #find the size of the list having appended 55
    #write a prog to sum all items in the list
    #write a python function that take two lists and returns true if they have atlest one common member.
students_marks=[60,70,80,]
#to covert 80 to 89
students_marks[2]=89
print(students_marks)

#to add a value to the list, we append.
students_marks.append(55)
print(students_marks)

#to find how many items are in the set, we use the len function.
#print(len(students_marks))
new_student_mark=[60, 70, 80 ]
students_marks=[60, 70, 89, 55 ]

students_marks=(input("enter items in list1"));
new_student_mark=(input("enter list items in list2"));

#to add the two lists
sum=(students_marks + new_student_mark)
print(sum)
common_elements =["i for i in new_student_mark if i in students_marks"]
if len(common_elements) >= 1:
     print("True")
else:
     print("False")
     print(common_elements)