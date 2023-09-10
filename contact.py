import sys,time


contact = {}

print("PhoneBook")
while True:
	print("""Contact List Menu:
	1. Add Contact
	2. Delete Contact
	3. Search Contact
	4. Quit""")
	action = int(input("Enter your choice:"))
	if action == 1:
		for i in range(1):
			name = input("Enter name:")
			phone_number = int(input("Enter phone number: "))
			contact[name] = phone_number 

			print("Contact added successfully!")



	elif action == 2:
		if contact == {}:
			print("You dont have a contact")

		elif contact != {}:

			print(f"Current contact {contact}")
			print("Please choose a contact to delete by entering the name")
			dele = input("Enter name >")
			er = contact.pop(dele)
			print(f"You have successfully deleted{dele} ")

	elif action == 3:
		while True:
			print("Search contacts")
			usr_in = input("Enter name to search>")
			if usr_in in contact:
				print(f"Phone number: {contact[usr_in]}")
				conti = input("would like to continue?>")
				if conti == "yes":
					continue
				elif conti == "no":
					break
				else:
					print("you input isnt recorgnized")
			elif usr_in != contact:
				print("Name not found")
				conti = input("would like to continue?>")
				if conti == "yes":
					continue
				elif conti == "no":
					break
				else:
					print("you input isnt recorgnized")


			
	elif action == 4:
		message = "Exiting phonebook..\n"
		for char in message:
			sys.stdout.write(char)
			sys.stdout.flush()
			if char == "\n":
				time.sleep(0.9)
			else:
				time.sleep(0.1)
		exit()

	
		













