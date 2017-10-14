import mycsv

def htmlfunc(header, data):
	a = '<html>' + '\n' + '<body>' + '\n' '<table>' + '\n'
	a += '<tr>'
	for item in header:
	  a += '<th>' + str(item) + '</th>'
	a += '</tr>' + '\n' 
	for i in data:
	  a += '<tr>'
	  for j in i:
	    a += '<td>' + str(j) + '</td>'
	  a += '</tr>'
	  a += '\n'
	a += '</table>'+ '\n'  '</body>'+ '\n' '</html>'
	return a

def htmlfunc2(data):
	header = list(map(chr, range(97, 97+len(data[0]))))
	a = '<html>' + '\n' + '<body>' + '\n' '<table>' + '\n'
	a += '<tr>'
	for item in header:
	  a += '<th>' + str(item) + '</th>'
	a += '</tr>' + '\n' 
	for i in data:
	  a += '<tr>'
	  for j in i:
	    a += '<td>' + str(j) + '</td>'
	  a += '</tr>'
	  a += '\n'
	a += '</table>'+ '\n'  '</body>'+ '\n' '</html>'
	return a