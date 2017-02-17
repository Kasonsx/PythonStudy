import xmlrpc.client
xmlrpc = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(xmlrpc.phone('evil'))