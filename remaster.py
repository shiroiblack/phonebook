#chooseoption():
print('STUDENT DBASE')
print('Enter (1) To Enter New Student')
print('Enter (2) To Search student Record')
control = int(input('Enter:'))
query = control
	#return query
#chooseoption()

def studbase():
	fulldict = dict()
	resultdict = dict()
	numStud = int(input('Enter number of student: '))
	a = input('Enter Subject1:')
	b = input('Enter Subject2:')
	c = input('Enter Subject3:')
	for i in range(numStud):
		name = input('Enter Student Name: ')
		id = input('Enter Student ID No.:')
		nameid = name+'_' + id
		asstype = ['Hw','Quiz','Atd','Exam']
		print(f'               {a}       ')
		print('Enter Student scores  separated with (,)')
		print('Hw, Quiz, Attd, Exam')
		score = input('Enter Score: ')
		scoresplit = score.split(',')
		result = dict(zip(asstype,scoresplit))
		resultdict[a] = result
		
		print(f'               {b}       ')
		print('Enter Student scores  separated with (,)')
		print('Hw, Quiz, Attd, Exam')
		scor1e = input('Enter Score: ')
		scoresplit = score.split(',')
		result = dict(zip(asstype,scoresplit))
		resultdict[a] = result
		fulldict[nameid] = resultdict
		print(fulldict)
	
#studbase()
def controp(query):
	#chooseoption()
	print(query)	
	if query == 1:
		studbase()
		
controp(query)
		