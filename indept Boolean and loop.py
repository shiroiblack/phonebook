command = ""
started = False


while True:
	command = input ('>')
	if command == 'start':
		if started:
			print('Car has already been started')
			
		else:
			print('Car started')
			started = True 
			
	elif command == 'stop':
		if started:
			print('Car stopped')
			started = False
		else:
			print('Car has already stopped ')
			started = False
	elif command == 'help':
		print("""
Start - To start car
Stop - To stop car 
Help - help	
		""")
		
	else:
		print("I don't understand what you meant by  " + command + ' Try help' )