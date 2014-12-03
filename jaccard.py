## for spectral clustering

def getclusters (file):
    clusters = {}
    for line in file:
        line = line.strip()
        [disease, cluster] = line.split('\t')
        if cluster in clusters:
            clusters[cluster].add(disease)
        else:
             newcluster = set()
             newcluster.add(disease)
             clusters[cluster] = newcluster
    return clusters

def getJaccard(clusters1, clusters2):
    jaccardIndexes = {}
    biggestJaccard = {}
    maxJaccard = 0
    maxPair = ()
    for clusterName1 in clusters1:
        cluster1 = clusters1[clusterName1]
        for clusterName2 in clusters2:
            cluster2 = clusters2[clusterName2]
            intersection = cluster1 & cluster2
            union = cluster1 | cluster2
            jaccardIndex = 1.0*len(intersection)/len(union)
            jaccardIndexes[(clusterName1,clusterName2)] = jaccardIndex
            if jaccardIndex > maxJaccard:
                maxJaccard = jaccardIndex
                maxPair = (clusterName1, clusterName2)
            if len(cluster1) > 5 and len(cluster2) > 5 and jaccardIndex > 0.1:
                biggestJaccard[(clusterName1, clusterName2)] = jaccardIndex
                print ("intersection: ",len(intersection))
    return (biggestJaccard, maxPair, maxJaccard)

## for markov clustering
def listOfClustersasSets(clusteredFile):
    clustered = open(clusteredFile)
    clusters = [] ## list of clusters (represented as sets)
    
    for line in clustered:
        cluster = line.split('\t')
        currCluster = set()
        for disease in cluster:
            currCluster.add(disease)
        clusters.append(currCluster)
    clustered.close()
    return clusters


def getJaccard(clusterList1, clusterList2):
    jaccardIndexes = {}
    biggestJaccard = {}
    maxJaccard = 0
    maxPair = ()
    for cluster1 in clusterList1:
        for cluster2 in clusterList2:
            intersection = cluster1 & cluster2
            union = cluster1 | cluster2
            jaccardIndex = len(intersection)/len(union)
            jaccardIndexes[(cluster1,cluster2)] = jaccardIndex
            if jaccardIndex > maxJaccard:
                maxJaccard = jaccardIndex
                maxPair = (cluster1, cluster2)
            if len(cluster1) > 5 and len(cluster2) > 5 and jaccardIndex > 0.1:
                biggestJaccard[(cluster1, cluster2)] = jaccardIndex
    return (biggestJaccard, maxJaccard, maxPair)


##if __name__ == '__main__':
##    print 
##    comorbidityclusters = open("newComorbidityClusters.txt")
##    genediseaseclusters = open("newGeneDiseaseClusters.txt")
##    clusters1 = getclusters(comorbidityclusters)
##    clusters2 = getclusters(genediseaseclusters)
##    comorbidityclusters.close()
##    genediseaseclusters.close()
##    (biggestJaccard, maxPair, maxJaccard) = getJaccard(clusters1, clusters2)
##    print ("max pair is: "+ str(maxPair) + " with a score of: "+ str(maxJaccard))
##   ##  print ("check: "+ str(jaccardIndexes[maxPair]))
##    (cluster1, cluster2) = maxPair
##    print ("max pair is actually: "+ str(clusters1[cluster1]) + " , "+ str(clusters2[cluster2]))
##    print (len(biggestJaccard))
##    for pair in biggestJaccard:
##        (cName1, cName2) = pair
##        bigCluster1 = clusters1[cName1]
##        bigCluster2 = clusters2[cName2]
## ##       print ("pair is: "+ str(bigCluster1) + " , "+str(bigCluster2) + " with a score of: " + str(biggestJaccard[pair]))
##        print ("\n ")
##        print ("first cluster has: ",str(len(bigCluster1))+"diseases, and second cluster has: ", len(bigCluster2))
##        print ("score for this one is: ",biggestJaccard[pair])
