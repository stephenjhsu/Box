import mycsv

"""
csv2xml takes in a csv file and transforms it into a xml file
"""

def xmlfunc(header, data):
	"""
	xmlfunc takes in a header line and the data and converts it into xml format
	"""
	header2 = header
	xmlString = ''
	for i in range(len(header2)):
	    header2[i] = header2[i].replace(' ', '_')
	header3 = list(header2)
	for i in range(len(header3)):
		header3[i] = header3[i].replace('_', ' ')
	xmlString += '<' + '?xml version = "1.0"?' + '>' + "\n"
	xmlString += '<'+ 'file' + '>' + "\n"
	xmlString += '  <headers>' + ','.join(header3) + '</headers>' + '\n'
	xmlString += '	<data>' + "\n"
	for row in data:
	    xmlString += '      <record>' + "\n"
	    xmlString += '          ' 
	    for j in range(len(header2)):
	        xmlString += '<' + header2[j] + '>' + row[j] + '</' + header2[j] + '>'
	    xmlString += "\n" + '      </record>' + "\n"
	xmlString += '	</data>' + "\n"
	xmlString += '</'+ 'file' + '>'
	return xmlString



def xmlfunc2(data):
	"""
	xmlfunc2 takes in the data and converts it into xml format
	"""
	header2 = list(map(chr, range(97, 97+len(data[0]))))
	xmlString = ''
	for i in range(len(header2)):
	    header2[i] = header2[i].replace(' ', '_')
	header3 = list(header2)
	for i in range(len(header3)):
		header3[i] = header3[i].replace('_', ' ')
	xmlString += '<' + '?xml version = "1.0"?' + '>' + "\n"
	xmlString += '<'+ 'file' + '>' + "\n"
	xmlString += '  <headers>' + ','.join(header3) + '</headers>' + '\n'
	xmlString += '	<data>' + "\n"
	for row in data:
	    xmlString += '      <record>' + "\n"
	    xmlString += '          ' 
	    for j in range(len(header2)):
	        xmlString += '<' + header2[j] + '>' + row[j] + '</' + header2[j] + '>'
	    xmlString += "\n" + '      </record>' + "\n"
	xmlString += '	</data>' + "\n"
	xmlString += '</'+ 'file' + '>'
	return xmlString



