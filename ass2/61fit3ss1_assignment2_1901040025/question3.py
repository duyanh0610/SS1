
import json
import collections
from operator import itemgetter

def countFrequency (data): 
    result = dict()
    # store in dict
    for word in data:
        
        if word not in result: 
            result[word] = 1
        else: 
            result[word] += 1    
    return result   

# count all word
def countAllWord (data): 
    return len(data)


# count frequency
def countWords_3(inputFile, outputFile) :
    
    #read input file
    with open (inputFile, "r") as input:
        data= input.read()
        data =data.lower().split()
    

    sum = countAllWord(data)
    result = countFrequency(data)
    
    # calculate and round frequency
    for word in result:
        result[word] = round((result[word] / sum) *100, 2 )

   

    # sort value
    # result =dict( sorted(result.items(),key= itemgetter(1), reverse= True) )
    
    #sorted
    result =dict([(key, -value) for value, key in sorted([(-value, key) for key, value in result.items()])])
    

    # write to json file
    with open ( outputFile, "w") as output: 
       json.dump (result,output) 
    
    

#main
countWords_3('sample.txt', 'sample_output_3.json')



