
## comorbidity: add one for each disease a specific disease
## is connected to
def degree_comorbidity():
    nodes = {}
    file = open("trimmedComorbidity.txt")
    for line in file:
        line = line.strip()
        ## words has disease1, disease2, edge weight
        words = line.split('\t')
        disease1 = words[0]
        disease2 = words[1]
        if disease1 in nodes:
            nodes[disease1].add(disease2)
        else:
            nodes[disease1] = set([disease2])

        if disease2 in nodes:
            nodes[disease2].add(disease1)
        else:
            nodes[disease2] = set([disease1])

    nodesDegrees = {}
    for node in nodes:
        val = nodes[node]
        nodesDegrees[node] = len(val)
    degrees = sorted(nodesDegrees.items(), key=lambda x: x[1])
    print ("mins")
    print (degrees[0:6])
    print ("maxes")
    print (degrees[-5:])
 
    aveDegree = sum(nodesDegrees.values())*1.0/len(nodesDegrees)
    print ("ave degree: ", aveDegree)
        

## gene-disease with genes as the degree factor
## add one for each gene the disease is connected to
def degree_geneDisease():
    nodes = {}
    file = open("trimmedGeneDisease.txt")
    for line in file:
        line = line.strip()
        words = line.split('\t')
        disease = words[0]
        if disease in nodes:
            nodes[disease] += 1
        else:
            nodes[disease] = 1
    degrees = sorted(nodes.items(), key=lambda x: x[1])
    print ("mins")
    for (disease, degree) in degrees[0:5]:
        print (disease, ': degree of ', degree)
    print ("maxes")
    for (disease, degree) in degrees[-5:]:
        print (disease, ': degree of ', degree)
    aveDegree = sum(nodes.values())*1.0/len(nodes)
    print ("ave degree: ", aveDegree)
       
## gene-disease for disease-disease version
## add one for each disease the disease is connected to
def degree_betterGeneDisease():
    ## dictionary where each key is a node and its value is
    ## a set of genes it is connected to
    nodeGenes = {}
    file = open("trimmedGeneDisease.txt")
    for line in file:
        line = line.strip()
        words = line.split('\t')
        disease = words[0]
        if disease in nodeGenes:
            nodeGenes[disease].add(words[1])
        else:
            nodeGenes[disease] = set(words[1])
    ## dictionary where each key is a node and its value is the
    ## number of diseases it is related to
    nodes = {}
    for disease1 in nodeGenes:
        for disease2 in nodeGenes:
            if disease1 != disease2:
                genes1 = nodeGenes[disease1]
                genes2 = nodeGenes[disease2]
                degree = len(genes1 & genes2)
                if degree > 0:
                    if disease1 in nodes:
                        nodes[disease1] += 1
                    else:
                        nodes[disease1] = 1
          
    degrees = sorted(nodes.items(), key=lambda x: x[1])
    print ("mins")
    for (disease, degree) in degrees[0:5]:
        print (disease, ': degree of ', degree)
    print ("maxes")
    for (disease, degree) in degrees[-5:]:
        print (disease, ': degree of ', degree)
    aveDegree = sum(nodes.values())*1.0/len(nodes)
    print ("ave degree: ", aveDegree)
            

if __name__ == '__main__':
    #degree_comorbidity()
    degree_betterGeneDisease()
