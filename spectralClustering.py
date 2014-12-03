from convertGeneDisease import convertGeneDisease_additive
import numpy as np
import scipy
from sklearn import cluster as c


def cluster(matrix, diseases, fileName, numClusters, affinityName):
    print "started clustering"
    clustering = c.SpectralClustering(n_clusters=numClusters, affinity=affinityName).fit(matrix)
    myFile = open(fileName, 'w')
    for i in xrange(len(clustering.labels_)):
        myFile.write(diseases[i] + "\t" + str(clustering.labels_[i])+"\n")
    myFile.close()
                                     

def comorbidityMatrix():
    diseaseDictionary = {}
    networkFile = open('trimmedComorbidity.txt')
    for line in networkFile:
        line = line.strip()
        lineList = line.split()
        score = abs(float(lineList[2]))
        if lineList[0] not in diseaseDictionary:
            diseaseDictionary[lineList[0]] = {}
        if lineList[1] not in diseaseDictionary:
            diseaseDictionary[lineList[1]]={}
        
        diseaseDictionary[lineList[0]][lineList[1]] = score
        diseaseDictionary[lineList[1]][lineList[0]] = score

    networkFile.close()

    mymatrix = []
    keys = diseaseDictionary.keys()
    
    for disease1 in keys:
        row = []
        for disease2 in keys:
            disease1dict = diseaseDictionary[disease1]
            if disease2 in disease1dict:
                row.append(disease1dict[disease2])
            else:
                row.append(0.0)
        mymatrix.append(row)

    return np.array(mymatrix), keys
        
        

matrix,keys = convertGeneDisease_additive()
cluster(matrix, keys, "newGeneDiseaseCluters_additive.txt", 20, "rbf")
matrix, keys = comorbidityMatrix()
cluster(matrix, keys, "newComorbidityClusters_additive.txt", 20, "precomputed")
