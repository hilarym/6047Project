import numpy
import scipy
from scipy import stats

def createClusters(clusterFile):
    clusterFile = open(clusterFile)
    clusters = [set() for x in xrange(100)]
    #clusters = []
    for line in clusterFile:
        strippedLine = line.strip()
        lineList = strippedLine.split()
        clusters[int(lineList[1])].add(lineList[0])
        #clusters.append(set(lineList))
    clusterFile.close()

    return clusters


def hyperGeomTest(clusters1, clusters2):
    
    for cluster1 in clusters1:
        for cluster2 in clusters2:
            pvalue = 1.0-(scipy.stats.hypergeom.cdf(len(cluster1&cluster2)-1,1455,len(cluster1),len(cluster2)))
            if pvalue <= .001:
                print "cluster1: "
                print len(cluster1)
                print "cluster2: "
                print len(cluster2)
                print len(cluster1&cluster2)
                print pvalue
        
        
clusters1 = createClusters("newGeneDiseaseClusters.txt")
clusters2 = createClusters("newComorbidityClusters.txt")
hyperGeomTest(clusters1, clusters2)
print "done"
