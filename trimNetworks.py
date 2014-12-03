from findIntersection.py import buildDictionary()


def readIntersection():
    intersectionFile = open('intersectFile.txt')
    intersectSet = set()
    for line in intersectionFile:
        intersectSet.add(line.strip())
    intersectionFile.close()
    return intersectSet


def TrimComorbidityNetwork(dictionary,intersectSet):
    count=0
    trimmedFile = open("trimmedComorbidity.txt", 'w')
    icdFile = open('AllNet5.net')
    for line in icdFile:
        myList = line.split('\t')
        add=True
        for i in range(2):
            icd = float(myList[i])*100
            if (myList[i] not in dictionary[int(icd)].keys()) or (dictionary[int(icd)][myList[i]] not in intersectSet):
                add=False
        if add==True:
            icd1 = dictionary[int(float(myList[0])*100)][myList[0]]
            icd2 = dictionary[int(float(myList[1])*100)][myList[1]]
            trimmedFile.write(icd1 + '\t' + icd2 + '\t' + myList[8] + '\n')
            count+=1
    print count
    icdFile.close()
    trimmedFile.close()
                


## trim gene disease association network so only has diseases
## that overlap with our other one (in our intersection)
def trimGeneDisease(networkData, intersection):
    icdFile = open(networkData)
    trimFile = open('trimmedGeneDisease.txt', 'w')

    ## use a set to contain the trimmed data (won't allow for copying
    ## twice)
    setDiseaseGenes = set()
    for line in icdFile:
        lineData = line.split('\t')
        umlsCode = lineData[3][5:]
        if umlsCode in intersection:
            geneName = lineData[2]
            score = lineData[5]
            lineToAdd = umlsCode+'\t'+geneName+'\t'+score+'\n'
            setDiseaseGenes.add(lineToAdd)
    for line in setDiseaseGenes:
        trimFile.write(line)
    trimFile.close()
    icdFile.close()        

dictionary = buildDictionary()
intersection = readIntersection()
TrimComorbidityNetwork(dictionary, intersection)
trimGeneDisease('all_gene_disease_associations.txt', intersection)
