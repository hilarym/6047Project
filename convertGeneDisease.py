import numpy as np
import scipy

def convertGeneDisease_euclidean():
    ## create a dictionary with the keys as diseases and the value a list
    ## of the genes related to that disease --> list of tuples with the
    ## gene and the score

    diseaseDictionary = {}
    networkFile = open('trimmedGeneDisease.txt')
    for line in networkFile:
        line = line.strip("\n")
        lineList = line.split("\t")
        score = lineList[2]

        if lineList[0] not in diseaseDictionary:
            diseaseDictionary[lineList[0]] = {}
        diseaseDictionary[lineList[0]][lineList[1]] = float(score)

    networkFile.close()

    mymatrix = []
    keys = diseaseDictionary.keys()
    onlyDiseaseNetwork = open("onlyDiseaseNetwork.txt", 'w')
    
    for disease1 in keys:
        row = []
        for disease2 in keys:
            euclidean_distance = 0.0
            disease1dict = diseaseDictionary[disease1]
            disease2dict = diseaseDictionary[disease2]

            disease1set = set(disease1dict.keys())
            disease2set = set(disease2dict.keys())
            both = disease1set & disease2set
            just1 = disease1set-disease2set
            just2 = disease2set-disease1set

            for i in both:
                euclidean_distance += (disease1dict[i]-disease2dict[i])**2
            for j in just1:
                euclidean_distance += (disease1dict[j])**2
            for k in just2:
                euclidean_distance += (disease2dict[k])**2

            euclidean_distance = (euclidean_distance)**.5
            onlyDiseaseNetwork.write(disease1 + "\t"+ disease2 + '\t' + str(euclidean_distance) + '\n')
            row.append(euclidean_distance)
        mymatrix.append(row)
        
    return np.matrix(mymatrix), keys

def convertGeneDisease_additive():
    ## create a dictionary with the keys as diseases and the value a list
    ## of the genes related to that disease --> list of tuples with the
    ## gene and the score

    diseaseDictionary = {}
    networkFile = open('trimmedGeneDisease.txt')
    for line in networkFile:
        line = line.strip("\n")
        lineList = line.split("\t")
        score = lineList[2]

        if lineList[0] not in diseaseDictionary:
            diseaseDictionary[lineList[0]] = {}
        diseaseDictionary[lineList[0]][lineList[1]] = float(score)

    networkFile.close()

    mymatrix = []
    keys = diseaseDictionary.keys()
    onlyDiseaseNetwork = open("onlyDiseaseNetwork_additive.txt", 'w')
    
    for disease1 in keys:
        row = []
        for disease2 in keys:
            distance = 0.0
            disease1dict = diseaseDictionary[disease1]
            disease2dict = diseaseDictionary[disease2]

            disease1set = set(disease1dict.keys())
            disease2set = set(disease2dict.keys())
            both = disease1set & disease2set

            for i in both:
                distance += (disease1dict[i]+disease2dict[i])

            onlyDiseaseNetwork.write(disease1 + "\t"+ disease2 + '\t' + str(distance) + '\n')
            row.append(distance)
        mymatrix.append(row)
        
    return np.matrix(mymatrix), keys

