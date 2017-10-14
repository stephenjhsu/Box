import sys

def getdata(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data.strip()

def readcsv(data, headers = True):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    line_list = []
    data = data.splitlines()
    for x in data:
        x = x.split(",")
        line_list.append(x)
    if headers == True:
        header = line_list[0]
        data = line_list[1:]
        return header, data
    else:
        return line_list



#print(readcsv(getdata('/Users/shsu/Downloads/t.csv')))