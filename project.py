#pylint:disable=E0001
#pylint:disable=E0001
fulldict = dict()
	
	
def studsubEntry(name,id,subject):
	temdict = dict()
	temdict['Subject'] = subject
	nameid = name +'_'+ id
	fulldict[nameid] = temdict
	print(fulldict)
	return fulldict
	
name = input('enter name: ')
id = input('enter id: ')
subject = ['python','c+']
subject = [subject]	
studsubEntry(name,id,subject)
print(fulldict)

def studentsubSearch(name, id):
	studentlist = fulldict.keys()
	for key in studentlist:
		namepart = key.split('_')
		print(namepart)
		
		if name in namepart or id in namepart:
			print('Record Found!')
			subject = fulldict[key]
			print(subject)
			#print(subject.values())
			subtaken=(f'A record was found for {name} with the id {id}. subjects taken are {subject} ')
			return subtaken
studentsubSearch(name, id)
print(subtaken)