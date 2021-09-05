import json
import os

stud_list = []                          # this will serve as list of students
choose = 'no'  
def file_upload():                               # upload the file in the program
    if os.path.exists("StudentList.txt"):                    # check if the txt is exist
        upload_file = open("StudentList.txt","r")               # read the file and use in for loop
        for student in upload_file:
            stud = json.loads(student)                           # convert each student string into dictionary
            stud_list.append({"name":stud["name"],"age":stud["age"],"grade":stud["grade"]})  # after converting to dictionary it will append to a list

file_upload()
def file_downloaded(): # write the value in the txt
    try:
        length = len(stud_list) if bool(stud_list) else null    #check the length of the list 
        download_file = open("StudentList.txt","w")             # open the txt 
        for student in stud_list:           
            download_file.write(json.dumps(student)) # convert each student dictionary in the list into strings and write it in the txt
            download_file.write("\n")   
    except:
        print("Your database is empty")            
    else:
        print("Student has been stored in database")
        download_file.close()

def view_list(): # view all the student info
    try:
        length = len(stud_list) if bool(stud_list) else null            # check if it has morethan 0 
        for student in stud_list:
            print("Name: ",student["name"]) 
            print("Age: ",student["age"])
            print("Grade: ",student["grade"])
            print()
    except:
        print("Your database is empty")  # if it has no length it is empty
    else:
        print("View All The Student ")
def delete(): # delete the student in the list
    try:
        length = len(stud_list) if bool(stud_list) else null        # check if the list is not empty
        deletion = input("Enter the Student number you want to delete: ")       
        for x in range(len(stud_list)):
            if(deletion == str(x)):  # check if the student element and deletion number is equal to each other
                del stud_list[x]
    except:
        print("Please Type Correctly")
    else:
        if len(stud_list) == length:  # check if no one is deleted meaning the deletion number is not found
             print("The Student information you want to delete is not Found")
        else:
             print("Deleted Successfully")
def check(name): # check the name and it should be unique
    for student in stud_list:
        if name in student["name"]:
           return null
    else:
        return name


def insert(): # insert a student
    try:
        check_name=input("Enter your name : ")
        name =check(check_name)                     # check the name if has the same value in the txt 
        age = int(input("Enter your age : "))
        grade = int(input("Enter your grade : "))
        stud_list.append({"name":name,"age":age,"grade":grade})   # append the student dictionary in the list
    except:
        print("Please Make sure you type correctly")
    else:
        print("Your info has been stored in the database successfully")
        print(stud_list)
def menu():
    print("1.) INSERT ")
    print("2.) DELETE ")
    print("3.) VIEW LIST")
    print("4.) Exit ")
def process(choose):
    if choose == '1':
        insert()
        return "Insert"
    elif choose == '2':
        delete()
        return "Delete"
    elif choose == '3':
        view_list()
        return "View list"
    elif choose == '4':
        return "yes"
    else:
        print("Error,Try Again")

while choose != 'yes':   # this is the start of the program
    menu()
    choose = input("Enter the process: ")
    choose = process(choose)
file_downloaded() # after the while loop it will store in the txt
