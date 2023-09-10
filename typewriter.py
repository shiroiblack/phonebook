import sys,time,os


hmm = 'You are the best in the world\n'

for char in hmm:
	sys.stdout.write(char)
	sys.stdout.flush()
	
	if char == '\n':
		time.sleep(0.1)
		
	else:
		time.sleep(0.1)