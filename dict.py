

    
#enter = True
tempdict= dict()

    
count = 0
while count < 4:
    name = input('enter name; ')
    list = ['w','r','h']
    id = '1234'
            
    merge = name+'_'+id
            
    tempdict[merge] = list
    #print(tempdict)
    count = count + 1
    enter = False
print(tempdict)
for idname in tempdict:
    #print(tempdict)
    sp = idname.split('_')
    print(sp)
    




