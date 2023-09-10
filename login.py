import os
usernamedb = 'emma'
passworddb = '12345'

def Logsys(username,password):
    login_attempt = 0
    fail = 3
    
    passa = True
    
    while passa and login_attempt < 5:
       username = input('Enter username: ')
       password = input('Enter password: ')
       if username == usernamedb and password == passworddb:
           print('welcome')
           passa = False
       else:
           #while username != usernamedb and password != passworddb:
             print(f'invalid credentials. Attempt left: {fail} out of 4 \n')
             login_attempt =login_attempt + 1
             fail = fail -1
             #os.system('clear')
             #passa = False
             if login_attempt == 3:
                 print('Warning!!! you have 1 attempt left\n')
                 #os.system('clear')
             elif login_attempt == 4:
                 print('Account Lock triggered, please contact admin')
                 passa = False
                 
                 
                 
print('i now have a key board')    
       
     
          
        
           
Logsys(usernamedb,passworddb)