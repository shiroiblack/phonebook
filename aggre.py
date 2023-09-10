def scoreaggregrator(name, id, subject, assessTypeList,scorelist):
	tempdict = dict()
	
	conver = dict(zip(assessTypeList,scorelist))
	tempdict(subject) = conver
	print(tempdict)