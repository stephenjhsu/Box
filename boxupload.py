#credit to: http://opensource.box.com/box-python-sdk/tutorials/intro.html

# Import two classes from the boxsdk module - Client and OAuth2
from boxsdk import Client, OAuth2
from boxsdk.network.default_network import DefaultNetwork
from pprint import pformat
import sys
from mycsv import *
from csv2json import *
from csv2html import *
from csv2xml import * 

# Define client ID, client secret, and developer token. Information at: developer.box.com
CLIENT_ID = ""
CLIENT_SECRET = ""
ACCESS_TOKEN = ""

class LoggingNetwork(DefaultNetwork):
    def request(self, method, url, access_token, **kwargs):
        """ Base class override. Pretty-prints outgoing requests and incoming responses. """
        print '\x1b[36m{} {} {}\x1b[0m'.format(method, url, pformat(kwargs))
        response = super(LoggingNetwork, self).request(
            method, url, access_token, **kwargs
        )
        if response.ok:
            print '\x1b[32m{}\x1b[0m'.format(response.content)
        else:
            print '\x1b[31m{}\n{}\n{}\x1b[0m'.format(
                response.status_code,
                response.headers,
                pformat(response.content),
            )
        return response

oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)
client = Client(oauth2, LoggingNetwork())

def upload(filepath, typechange = None, headers = True, namefile = 'output'):
	"""
	upload is a function that uploads files directly from local to the Box cloud
	Inputs:
		filepath: string path to the filepath
		typechange: string such as "html", "xml" or "json" denoting the type of file to be saved as
		headers: boolean if the file has a header or not
		namefile: string of the file name to be saved as 
	"""
	if typechange == None:
		box_file = client.folder('0').upload(filepath)
	elif headers == False:
		#defaults to abc... if no headers given
		data = readcsv(getdata(filepath), headers=False)
		if typechange == 'html':
			tmpfile = "/tmp/"+ str(namefile) +"." + str(typechange)
			htmlfile = open(tmpfile, "w")
			htmlfile = htmlfile.write(htmlfunc2(data))
			box_file = client.folder('0').upload(tmpfile)
		elif typechange == 'xml':
			tmpfile = "/tmp/"+ str(namefile) +".xml"
			xmlfile = open(tmpfile, "w")
			xmlfile = xmlfile.write(xmlfunc2(data))
			box_file = client.folder('0').upload(tmpfile)
		elif typechange == 'json':
			tmpfile = "/tmp/"+ str(namefile) +".json"
			jsonfile = open("/tmp/output.json", "w")
			jsonfile = jsonfile.write(jsonfunc2(data))
			box_file = client.folder('0').upload(tmpfile)
		else:
			raise ValueError('Sorry, type change not recognized')
	else:
		header, data = readcsv(getdata(filepath))
		if typechange == 'html':
			tmpfile = "/tmp/"+ str(namefile) +"." + str(typechange)
			htmlfile = open(tmpfile, "w")
			htmlfile = htmlfile.write(htmlfunc(header, data))
			box_file = client.folder('0').upload(tmpfile)
		elif typechange == 'xml':
			tmpfile = "/tmp/"+ str(namefile) +"." + str(typechange)
			xmlfile = open(tmpfile, "w")
			xmlfile = xmlfile.write(xmlfunc(header,data))
			box_file = client.folder('0').upload(tmpfile)
		elif typechange == 'json':
			tmpfile = "/tmp/"+ str(namefile) +"." + str(typechange)
			jsonfile = open(tmpfile, "w")
			jsonfile = jsonfile.write(jsonfunc(header,data))
			box_file = client.folder('0').upload(tmpfile)
		else:
			raise ValueError('Sorry, type change not recognized')

#Example calls
#upload('/Users/shsu/Downloads/t.csv', 'html', headers = False, namefile = 'stephen')
#upload('/Users/shsu/Downloads/t.csv', 'xml', headers = False)
#upload('/Users/shsu/Downloads/t.csv', 'json', headers = False)
upload('/Users/shsu/Downloads/aapl.csv', 'html', headers = True, namefile = 'boxrules')




