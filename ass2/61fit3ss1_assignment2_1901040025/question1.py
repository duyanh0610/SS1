
import json


# count 
def countFrequency (data): 
    result = dict()
    # store in dict
    for word in data:
        if word not in result: 
            result[word] = 1
        else: 
            result[word] += 1    

    return result   

# count frequency
def countWords_1(inputFile, outputFile) :
    #read input file
    with open (inputFile, "r") as input:
        data= input.read()
        data =data.lower().strip().split()
    
    
    result = countFrequency(data)
    # write to json file
    with open ( outputFile, "w") as output: 
       json.dump (result,output) 
    

# main
countWords_1('sample.txt', 'sample_output_1.json')



