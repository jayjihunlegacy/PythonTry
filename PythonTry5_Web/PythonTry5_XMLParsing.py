from xml.dom.minidom import parse, parseString, Document
from xml.etree import ElementTree

# the xml must me saved using "ANSI" encoding.


loopFlag = 1
xmlFD = -1
BooksDoc = None

fileName = "C:/pythonplay/book.xml"

def LoadXMLFromFile():
    global fileName, xmlFD

    try:
        xmlFD = open(fileName)
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print("loading fail!")
        else:
            print("XML Document loading complete")
            return dom
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()
 
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True

def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())

def PrintBookList(tag):
    global BooksDoc
    if not checkDocument():
        return None

    booklist=BooksDoc.childNodes[0].childNodes
    for item in booklist:
        if item.nodeName == "book":
            subitems = item.childNodes

            for atom in subitems:
                if atom.nodeName in tag:
                    print("title=", atom.firstChild.nodeValue) #firstChild of title is the title text.


def AddBook(bookdata):
    global BooksDoc
    if not checkDocument():
        return None

    #new Book!
    newBook = BooksDoc.createElement('book') #BooksDoc here is meaningless.
    newBook.setAttrubute('ISBN', bookdata['ISBN'])

    #new Title!
    titleEle = BooksDoc.createElement('title')





depth = 0
def Print(node):
    global depth
    
    print("-"*2*depth,node.nodeName, node.nodeValue)#(node.nodeValue if node.nodeName!="#text" else ""))
    depth+=1
    for child in node.childNodes:
        Print(child)
    depth-=1

BooksDoc = LoadXMLFromFile()
PrintDOMtoXML()
print("================================================")
dummy = Document()
newBook = dummy.createElement('book')
newBook.setAttribute('ISBN', "111")
BooksDoc.firstChild.appendChild(newBook)

PrintDOMtoXML()

print(type(BooksDoc))
PrintBookList(["title",])

#Print(BooksDoc.childNodes[0])

BooksFree()
    



