from urllib.request import urlopen
import re #regex or regular expression

urls = ["http://google.com", "http://nytimes.com", "http://www.csueastbay.edu"]

regex = '<title>?(.+?)</title>' # get whatever in between <title>

pattern = re.compile(regex) #Compile a regular expression pattern into a regular expression object

for url in urls:
    htmlfile = urlopen(url) 
    htmltext = htmlfile.read()
    text = htmltext.decode(encoding="utf8", errors='ignore')
    title = re.findall(pattern, text) # in the file htmltext, find all that fits the pattern
    print (title)