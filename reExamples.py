import re

# find the word pretty
def hasPretty(inp):
    return re.search(r'pretty', inp) != None
print hasPretty('i am pretty so yeah')
print hasPretty('i am not that ahhh')
    
def whichPet(inp):
    result = re.search(r'pet (cat|dog)', inp)
    if result == None:
        return None
    return result.group(1)
print whichPet('my pet cat')
print whichPet('my pet dog was cool')
print whichPet('my pet donkey')


def getAdjs(inp):
    return re.findall(r'\w+y', inp)
    #return re.findall(r'[a-zA-Z0-9_]+y', inp) # the same thing
    #return re.findall(r'\w{1,}y', inp) # the same thing
print getAdjs('the funny book was goofy')

def isEmail(inp):
	return re.search(r'^\w+@\w+(\.\w).*?', inp) != None
print isEmail('blah@hello.com')
print isEmail('sd$sd@hello.com')

def getTxts(inp):
	return re.findall(r'\w+\.txt', inp)
print getTxts('yo.html blah.txt woah.txt')

def getNumWords(inp):
	i = 0
	awe = 0
	return re.findall(r'\w+', inp)
print getNumWords('yo.html blah.txt woah.txt')
for i in wordList:		#set a condition to check if the word is awesome
	if wordList[i] == 'awesome' or 'awes0me':
		awe += 1
percAwesomeness = (awe / len(wordList)) * 100

#def percAwesome(inp):
#	result = re.search(r'awesome|awes0me')
#	words, found, percentage = 0
#	re.''
#	if result == 1:
#		found += 1
#percentage = (found/words)*100
#print percAwesome('')
#print 'Percentage awesomeness is', percentage''