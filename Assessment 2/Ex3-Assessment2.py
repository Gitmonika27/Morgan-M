import re

def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

url = input("Enter the URL:")

if(isValidURL(url) == True):
    print("Yes")
    print("Explanation:URL Validation Passed.")
else:
    print("No")
    print("Explanation:Url Validation failed")