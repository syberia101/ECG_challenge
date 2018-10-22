import fitz #fitz is the module MuPyPDF.
import re
import probablepeople
from StringMatcher import cleanString


def extract(fileName):
    if (fileName.endswith(".pdf")):
        next
    else:
        fileName += ".pdf"

    doc = fitz.open(fileName)
    pages = len(doc)
    pdfText = ""
    for page in doc:
        pdfText += page.getText()

    #pdfText = pdfText.replace('\r', '').replace('\n',
    print(pdfText)
    return pdfText

def extractRef(text):
    """I need to search for 'References' backwards and search the text bottom up
    to find the last instance of the word. This will isolate the references section
    of the text. It would not work searching forwards after testing."""
    #secnerefer
    reg = re.compile("(secnerefeR|SECNEREFER)") #This is disgusting and I hate it but it works
    refStart = reg.search(text[::-1])
    if refStart != None:
        refStart = len(text) - refStart.start()
        refText = text[refStart:]
    else:
        return None

    #This will search the references section based on the presence of numbers within square brackets.
    #If the pattern is present, it will use this method to extract numbered references.
    #This assumes that a paper will have at least 3 references.
    refOne = refText.find("[1]")
    refTwo = refText.find("[2]")
    refThree = refText.find("[3]")
    if refOne < refTwo and refTwo < refThree:
        refs = findRefsList(refText,"SquareBrackets")
        return refs

    #this will search using the pattern of numbers followed by fullstops.
    refOne = refText.find("1.")
    refTwo = refText.find("2.")
    refThree = refText.find("3.")
    if refOne < refTwo and refTwo < refThree:
        refs = findRefsList(refText,"NumberFullstop")
        return refs

    #This searches for the pattern of references that are plainly numbered.
    refOne = refText.find(" 1 ")
    refTwo = refText.find(" 2 ")
    refThree = refText.find(" 3 ")
    refFour = refText.find(" 4 ")
    if refOne < refTwo and refTwo < refThree and refThree < refFour:
        refs = findRefsList(refText,"Numbered")
        return refs

    newLines = [m.start() for m in re.finditer('\n', refText)]
    if newLines[2] - newLines[1] < 4 and newLines[3] - newLines[2] < 4:
        print("Cannot find by NewLine or brackets.")
        return refText

    refs = findRefsList(refText,"NewLine")
    print(refs, ' refs')
    return refs

    return refText

def findRefsList(text, method="NewLine"):
    """This will search the text given using a given method to try and extract
    references.
    Accepted parameters for method are SquareBrackets, Numbered, NumberFullstop and NewLine."""
    refs = []
    fail = 0
    start = 0
    end = 1
    i = 1

    if method == "SquareBrackets" or method == "Numbered" or method == "NumberFullstop":
        #this if statement removes the need to repeat the condition twice with different
        #substrings. It will run with either " i " or "[i]"
        if method == "SquareBrackets":
            delimS = "["
            delimE = "]"
        elif method == "Numbered":
            delimS = " "
            delimE = " "
        else:
            delimS = ""
            delimE = "."
        while True:
            #The fail variable will count how many times the item could not be found.
            #This is necessary as sometimes the program can fail to find the next reference
            #but still not have reached the end.
            if fail > 2:
                break
            if text.find(delimS+str(i)+delimE) == -1:
                fail += 1
                continue
            start = (text.find(delimS+str(i)+delimE))+2+len(str(i))
            end = text.find(delimS+str(i+1)+delimE)
            refs.append(text[start:end])
            i += 1

    #Newline method is simplest but least reliable. This is as the PDF to text
    #utilities will often insert extra newline characters in the middle of text.
    elif method == "NewLine":
        print("Newline Split")
        refs = text.split("\n")

    else:
        print("Not an appropriate parameter. Accepted parameters are \"SquareBrackets\", \"Numbered\" and \"NewLine\".")

    finalRefs = []
    for i in refs:
        if len(i) > 3:
            finalRefs.append(i)

    for i in finalRefs:
        i = i.replace('\r', '').replace('\n', '')
    return finalRefs

#once the lines have been extracted, the reference metadata can be extracted from each.
def findReferences(refString):
    metadata = {}
    metadata['authors'] = findNames(refString)
    metadata['title'] = findTitle(refString, metadata['authors'])
    return metadata

#This will find the title of the paper inside of the reference string.
def findTitle(refString, names):
    title = ""
    if names != None:
        #Different characters can indicate the end of a paper title in a reference.
        #comma and fullstop are commonly used. However commas are often in paper titles.
        delim = re.compile("(,|\.|\(\d\d\d\d\)\.)")
        titleStart = refString.find(names[-1]) + len(names[-1]) + 2
        print(titleStart, " TITLELLELELELEL")
        try:
            titleEnd = delim.search(refString[titleStart:]).start() + len(refString[:titleStart])
        except:
            return None
        title = cleanString(refString[titleStart:titleEnd], True)
        print("title in find title "+title)

    return title

#names can be extracted from the beginning of the reference string.
def findNames(refString):
    refList = refString.split()
    #initials will be a list of all of the indexes in the string that are single letters.
    initials = []
    fail = 0
    singleInitial = re.compile("^[A-Z]$")
    doubleInitial = re.compile("^[A-Z]\.[A-Z]\.$")
    tripleInitial = re.compile("^[A-Z]\.[A-Z]\.[A-Z]\.$") #I found names with 3 initials at once so here it is
    capitalLetter = re.compile("^\ ?[A-Z]")
    #Go through string and find Initials that would indicate a name.
    for i in range(len(refList)):
        if fail > 2:
            break

        #checks if words from the string match a pattern for an initial.
        #matches one single capital letter.
        if singleInitial.match(cleanString(refList[i], False)) != None:
            fail = 0
            try:
                if capitalLetter.match(cleanString(refList[i+1], False)) != None:
                    initials.append(i)
            except IndexError:
                fail += 1

        #matches the form for double initials "J.J."
        elif doubleInitial.match(refList[i]) != None:
            fail = 0
            try:
                if capitalLetter.match(cleanString(refList[i+1], False)) != None:
                    initials.append(i)
            except IndexError:
                fail += 1
        elif tripleInitial.match(refList[i]) != None:
            fail = 0
            try:
                if capitalLetter.match(cleanString(refList[i+1], False)) != None:
                    initials.append(i)
            except IndexError:
                fail += 1
        else:
            fail += 1

    """This should now create a list of names by taking the words in between each initial.
    first case is if names are in the format "M. Rea," second case is if the names are in the format "Rea, M."
    commas are used to separate names."""
    if len(initials) == 0:
        print("No names could be found.")
    else:
        names = []

        if initials[0] == 0: #This means names are formatted M. Rea, with initial first.
            for i in range(len(initials)):
                name = ""
                if i == len(initials)-1: #clause that catches the last name. Will just add the initial and the next word.
                    name += refList[initials[i]] +" "+ refList[initials[i]+1] + " "
                    names.append(name)
                    continue
                try:

                    if initials[i+1] - initials[i] == 1: #clause to catch names with two initials eg M. W. Rea,
                        for j in range(initials[i], initials[i+2]): #Find every word between the two relevant initials
                            if cleanString(refList[j]) == "and":
                                continue
                            name += refList[j] + " " #record each word found as part of one name.
                        i += 1 # needed to skip out the double initial

                    else:
                        for j in range(initials[i], initials[i+1]): #Find every word between the two relevant initials.
                            if cleanString(refList[j]) == "and":
                                continue
                            name += refList[j] + " " # record each word found as part of one name.

                    names.append(name)
                except IndexError:
                    continue

        elif initials[0] >= 1:
            for i in range(len(initials)):
                name = ""
                if i == 0: #clause to cath the first name. Works similarily to the clause for the last name.
                    for j in range(0, initials[0]):
                        name += refList[initials[i]]+" "
                    names.append(name)
                    continue
                try:

                    if initials[i+1] - initials[i] == 1: #clause to catch names with two initials eg M. W. Rea,
                        for j in range(initials[i]+1, initials[i+2]+1):
                            if cleanString(refList[j]) == "and":
                                continue
                            name += refList[j] + " "
                        i += 1 # needed to skip out the double initial

                    else:
                        for j in range(initials[i]+1, initials[i+1]+1):
                            if cleanString(refList[j]) == "and":
                                continue
                            name += refList[j] + " "

                    names.append(name)
                except IndexError:
                    if len(name) > 0:
                        names.append(name)
                    continue

        if len(names) < 1:
            return None


        #strip trailing commas from names.
        for i in range(len(names)):
            if names[i].endswith(", ") or names[i].endswith(","):
                comma = names[i].find(",")
                names[i] = names[i][:comma - len(names[i])]

        return names

#Function to run and collect references from either a pdf file or text.
def returnRefList(data):
    #If the string has less than 3 words in it, it will be a local file.
    if len(data.split()) < 3:
        refStrings = extractRef(extract(data))
    #otherwise it will be a fulltext document.
    else:
        refStrings = extractRef(data)
    references = []
    for i in refStrings:
        print('reference in i '+i)
        references.append(findReferences(i))

    finalRefs = []
    for i in references:
        metadata = {}
        if i != None:
            metadata['metadata'] = i
            finalRefs.append(metadata)
            print('metadata in return ',metadata)
    return finalRefs

#text1 = input("Input filename: ")
#refList = extractRef(extract(text1))
#for i in refList:
#    print(i+"\nNext Reference\n")
