import sys,time




logged_out = True
print("Login")
username = "jachike"
password = "snakes199323"


while logged_out:
	owner = "anelo"
	usrname = input("Enter username> ")
	passwrd = input("Enter password> ")
	print("i am here ")

	if usrname == username and passwrd == password:

		log_msg = "Welcome you credentials are correct. \n if i may as, how did you get the credentials?"

		for char in log_msg:
			sys.stdout.write(char)
			sys.stdout.flush()
			if char == "\n":
				time.sleep(0.9)

			else:
				time.sleep(0.1)
		while True:
			ans = input("How?")
			split_answer = ans.split()
			
			if owner in split_answer:
				print("You are a Admin permission, there for you will be given root access!")
				break
			else:
				print(f"Sorry i don't recorgnize that, try entering the full name")
	elif usrname == username and passwrd != password:
		print("invalid password try again")
	elif usrname != username and passwrd == password:
		print("invalid username")
	
	elif usrname != username and passwrd != password:
		print("invalid credentials")




