class  Point:
	def kill(self):#methods
		input('what?')
		print('process killed')
		
	def revive(self):
		print('process Revived')
		
		
		
point1 = Point()#assigns to a variable
point1.x = 10
point1.y = 20

print(point1.x,point1.y) 

point2 = Point()
print(point2.x)