import re  

text = input('Enter the sentence:')  

#text = "https://mail.google.com:1010/mail/"  

url = re.findall("^h.+",text)  
hostname = re.findall("//mail.(\w.+.com)",text)  
protocol = re.findall("^(h.+?):", text) 
portnumber =re.findall("[0-9]+",text) 
print("URL:", url)  
print("Hostname:", hostname) 
print("Protocol:", protocol) 
print("Port number:", portnumber) 