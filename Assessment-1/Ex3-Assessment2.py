import re 

def isvalidURL(str):
    regex = ("((http|https)://)(www.)?"+
             "[a-zA-Z0-9@:%._\\+-#?&//=]"+
             "{2,256}\\.[a-z]"+
             "{2,6}\\b([-a-zA-Z0-9@:%"+
             "._\\+~#?&//=]*)")

p = re.compile(regex)
if (str==None):
    return False
    
if (re.search(p,str)):
    return True
    else:
        return False
    
url=input("Enter the URL:")
if(isvalidURL(url)== True):
    print("yes")
    print("Explanation:URL validation passed.")
else:
    print("No")
    print("Explanation:URL validation failed.")

