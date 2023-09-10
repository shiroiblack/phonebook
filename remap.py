studRecdict = dict()


def studdataEntry():
	name = input('Enter name: ')
	id  = input('Enter id: ')
	nameid = name +'_'+id
	
	chemquiz = int(input('Enter Chemquiz: '))
	bioquiz = int(input('Enter bioquiz: '))
	mathsquiz = int(input('Enter maths quiz: '))
	
	chemHw =int(input('Entet chem Hw: '))
	bioHw =int( input('Enter bio Hw: '))
	mathsHw = int(input('Enter maths Hw: '))
	
	chemExam = int(input('Enter chem exam: '))
	bioExam = int(input('Enter bio exam : '))
	mathsHW = int(input('Enter math Hw: '))
	
	Sum_for_chem = (chemquiz + chemHw + chemExam)
	print(Sum_for_chem)
	Chemavg = (Sum_for_chem) /3
	print(Chemavg)
	
studdataEntry()