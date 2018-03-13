"""
csv2json takes in a csv file and transforms it into a json file
"""

import mycsv

def jsonfunc(header, data):
	"""
	jsonfunc takes in a header line and the data and converts it into json format
	"""
	jsonString = '{' + "\n" + '	"headers": [' + "\n"
	header2 = ','.join(header)
	for i in range(len(header)-1):
		jsonString += '		"' + header[i] + '"' + ',' + "\n"
	jsonString += '		"' + header[len(header)-1] + '"'
	jsonString += "\n"+ '	],' + "\n"

	jsonString += '	"data": [' + "\n" 
	for row in range(len(data)):
		if row != len(data)-1:
			jsonString += "		{" + "\n"
			for j in range(len(header)-1):
				jsonString += '			"'+ header[j] +'": ' + '"' + data[row][j] + '",' + "\n"
			jsonString += '			"'+ header[len(header)-1] +'": ' + '"' + data[row][len(header)-1] + '"'
			jsonString += "\n" + "		}"+ ',' + '\n'
		else:
			jsonString += "		{" + "\n"
			for j in range(len(header)-1):
				jsonString += '			"'+ header[j] +'": ' + '"' + data[row][j] + '",' + "\n"
			jsonString += '			"'+ header[len(header)-1] +'": ' + '"' + data[row][len(header)-1] + '"'
			jsonString += "\n" + "		}"+ '\n'

	jsonString += '	]' + "\n"
	jsonString += '}'
	return jsonString


def jsonfunc2(data):
	"""
	jsonfunc2 takes in the data and converts it into json format
	"""
	jsonString = '{' + "\n" + '	"headers": [' + "\n"
	header = list(map(chr, range(97, 97+len(data[0]))))
	header2 = ','.join(header)
	for i in range(len(header)-1):
		jsonString += '		"' + header[i] + '"' + ',' + "\n"
	jsonString += '		"' + header[len(header)-1] + '"'
	jsonString += "\n"+ '	],' + "\n"

	jsonString += '	"data": [' + "\n" 
	for row in range(len(data)):
		if row != len(data)-1:
			jsonString += "		{" + "\n"
			for j in range(len(header)-1):
				jsonString += '			"'+ header[j] +'": ' + '"' + data[row][j] + '",' + "\n"
			jsonString += '			"'+ header[len(header)-1] +'": ' + '"' + data[row][len(header)-1] + '"'
			jsonString += "\n" + "		}"+ ',' + '\n'
		else:
			jsonString += "		{" + "\n"
			for j in range(len(header)-1):
				jsonString += '			"'+ header[j] +'": ' + '"' + data[row][j] + '",' + "\n"
			jsonString += '			"'+ header[len(header)-1] +'": ' + '"' + data[row][len(header)-1] + '"'
			jsonString += "\n" + "		}"+ '\n'

	jsonString += '	]' + "\n"
	jsonString += '}'
	return jsonString

