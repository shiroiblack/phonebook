studentdict = dict()
student_sub_dict = dict()


def stdentry(name , id , student_sub_dict):
    std_id = name + '_'+id
    studentdict[std_id] = student_sub_dict
    return studentdict
    
def stdsubentry(subject):
    student_sub_dict['subject'] = subject
    print(student_sub_dict)
    merge = stdentry(name , id , student_sub_dict)
    
    
name = input('enter student name: ')
id = input('enter student ID: ')
subject = input('Enter sunject: ')
subject = [subject]
stdsubentry(subject)
print(studentdict)

#studentdict = dict()

def studentsearch(id,name):
    studentlist = studentdict.keys() 
    print(studentlist)
    for KEY in studentlist:
        namepart = KEY.split('_')
        if name in namepart or id in namepart:
        	print('we found a record')
        	subject = fulldict[KEY].values()
        	print(subject.values())
studentsearch(id,name)
