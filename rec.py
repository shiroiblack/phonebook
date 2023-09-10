
fulldict = dict()
resultdict = dict()
def studentrec():
    Entry = True
    while Entry:
        print('STUDENT RECORD')
        print('Select (1) to search for a student record')
        print('Select (2) to Enter result')
        print('1. Search Student')
        print('2. Enter Result')
        action =int(input('Select: '))
        if action == 2:
            rec = True
            while rec:
                a =  input('Enter first subject: ')
                #a.upper()
                b = input('Enter second subject: ')
                c = input('Enter third subject: ')
                
                
                numStud = int(input('Enter number of students: '))
                for i in range(numStud):
                    name1 = input('Enter Student name: ')
                    id1 = input(f'Enter id({name1}): ')
                    nameid1 = name1 + '_' + id1
                    asstype = ['Hw', 'Quiz', 'Atte', 'Exam']
                    print(f'{a}')
                    #print('ENTER SCORES SEPERATED BY (,)')
                    
                    print('ENTER SCORES SEPERATED BY (,)')
                    print('ENTER SCORES FOR {a}')
                    print("HW',|'QUIZ',|'ATTEND',|'EXAM")
                    sub = input('\n')
                    subsplit = sub.split(',')
                    result= dict(zip(asstype,subsplit))
                    fulldict[a] = result
                    
                    #name2 = input('Enter Student name: ')
                  #  id2 = input(f'Enter id({name2}): ')
                    #nameid2 = name2 + '_' + id2
                    asstype = ['Hw', 'Quiz', 'Atte', 'Exam']
                    print(f'{b}')
                    print('ENTER SCORES SEPERATED BY (,)')
                    print('HW',   'QUIZ',    'ATTEND',   'EXAM')
                    sub2 = input(f'Enter score for {b}: ')
                    subsplit2 = sub2.split(',')
                    result2= dict(zip(asstype,subsplit2))
                    fulldict[b]= result2
                    
                    resultdict[nameid1]= fulldict
                    
                    return resultdict
                    
            print('Number of students reached')
               
                
        elif action == 1:
                
                #def studsearch(name1,id1):
                 stulist = resultdict.keys()
                 print(stulist)
                 name1 = input('Enter name: ')
                 id1 = input('Enter id: ')
                 #nameid = name+'_'+ id
                 #splitit = nameid.split('_')
              
                 for name1 in stulist or id1 in stulist:
                     print('user found')
                 
                
                
                 print(resultdict)
studentrec()
  
        
        
#def stdsubsearch(name,id):
    #nameid = resultdict.keys()
#stdsubsearch(name,id)