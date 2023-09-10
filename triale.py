fulldict = dict()
tempdict = dict()
name = 'Emmanuel'
id = '2012405017'
nameid = name+'_'+id

subject = 'Computer science'
assesTypelist=['Quiz','Hw','Attend','Exam']
scorelist = [40,20,20,70]

resultdict = dict(zip(assesTypelist,scorelist))
tempdict[subject] = resultdict
fulldict[nameid] =tempdict
print(fulldict)
result = numpy.prod(scorelist)