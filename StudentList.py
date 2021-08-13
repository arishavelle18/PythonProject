import json
import os

stud_list = []
choose = 'no'
def file_upload():
    if os.path.exists("StudentList.txt"):
        upload_file = open("StudentList.txt","r")
        for student in upload_file:
            stud = json.loads(student)
            stud_list.append({"name":stud["name"],"age":stud["age"],"grade":stud["grade"]})

file_upload()
def file_downloaded():
    try:
        length = len(stud_list) if bool(stud_list) else null
        download_file = open("StudentList.txt","w")
        for student in stud_list:
            download_file.write(json.dumps(student))
            download_file.write("\n")
    except:
        print("Your database is empty")
    else:
        print("Student has been stored in database")
        download_file.close()

def view_list():
    try:
        length = len(stud_list) if bool(stud_list) else null
        for student in stud_list:
            print("Name: ",student["name"])
            print("Age: ",student["age"])
            print("Grade: ",student["grade"])
            print()
    except:
        print("Your database is empty")
    else:
        print("View All The Student ")
def delete():
    try:
        length = len(stud_list) if bool(stud_list) else null
        deletion = input("Enter the Student number you want to delete: ")
        for x in range(len(stud_list)):
            if(deletion == str(x)):
                del stud_list[x]
    except:
        print("Please Type Correctly")
    else:
        if len(stud_list) == length:
             print("The Student information you want to delete is not Found")
        else:
             print("Deleted Successfully")
def check(name):
    for student in stud_list:
        if name in student["name"]:
           return null
    else:
        return name


def insert():
    try:
        check_name=input("Enter your name : ")
        name =check(check_name)
        age = int(input("Enter your age : "))
        grade = int(input("Enter your grade : "))
        stud_list.append({"name":name,"age":age,"grade":grade})
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

while choose != 'yes':
    menu()
    choose = input("Enter the process: ")
    choose = process(choose)
file_downloaded()