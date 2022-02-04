import re  

text = input('Enter the sentence:')  

#text = "https://mail.google.com:1010/mail/"  

url = re.findall("^h.+",text)  
hostname = re.findall("//mail.(\w.+.com)",text)
protocol = re.findall("^(h.+?):", text) 
portnumber =re.findall("[0-9]+",text) 
host=re.findall('://([\w\-\.]+)',text)
separator=""
print("URL:", separator.join(url))  
print("Hostname:", separator.join(hostname))
print("Protocol:", separator.join(protocol))
print("Port number:", separator.join(portnumber))