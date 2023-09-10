class Person():
	def __init__(self,name):
		self.name = name
		
	def talk(self):
		print(f'Hi, {self.name}')
		
		

voice = input('who are you?:')

name = Person(voice)
name.talk()

name1 = person(voice)
name1.talk()