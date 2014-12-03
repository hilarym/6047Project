def buildDictionary():
    myFile = open('MRCONSO.RRF')
    line = myFile.readline()
    dictionary=[{} for x in xrange(100000)]
    for line in myFile:
        myList = line.split('|')
        if myList[11]=='ICD9CM':
            if '-' not in myList[10] and myList[10][0].isalpha() == False:
                icd = int(float(myList[10])*100)
##                if dictionary[icd]==None or myList[0]==dictionary[icd]:
                dictionary[icd][myList[10]] = myList[0]


    myFile.close()
    return dictionary

def getGeneDiseases():
    umlsFile = open('all_gene_disease_associations.txt')
    geneDisease=set()
    for line in umlsFile:
        myList = line.split('\t')
        umls = myList[3][5:]
        geneDisease.add(umls)
    umlsFile.close()
    return geneDisease


def convertICD9toUMLS(dictionary, dataFile):
    phenoSet = set()
    icdFile = open(dataFile)
    for line in icdFile:
        myList = line.split('\t')
        for i in range(2):
            icd = float(myList[i])*100
            if myList[i] in dictionary[int(icd)].keys():
                phenoSet.add(dictionary[int(icd)][myList[i]])

    icdFile.close()
    print len(phenoSet)
    return phenoSet

def findIntersectionSize(set1, set2):
    intersection = set1 & set2
    length = len(intersection)
    intersectFile = open('intersectFile.txt','w')
    for i in intersection:
        intersectFile.write(i+'\n')
    intersectFile.close()
    return length


d=buildDictionary()
print "done with dictionary"
g = getGeneDiseases()
print "done with genes"
print len(g)
p = convertICD9toUMLS(d, 'AllNet5.net')
print "finally done!!!"
print findIntersectionSize(g,p)
