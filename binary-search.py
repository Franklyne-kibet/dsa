#Binary Search and complexity analysis in python 
def locate_card(cards, query):
    #create a variable position with the value 0
    position = 0  
    #set up a loop for repetition
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

#Sample inputs & outputs 
cards = [13,11,10,7,4,3,1,0]
query = 7
output = 3 

result = locate_card(cards,query)
print(result)

#test result output
print(result == output)

#test case
test = {
    'input':{
        'cards':[13,11,10,7,4,3,1,0],
        'query': 7
    },
    'output':3
}

# Test the function
print(locate_card(**test['input']) == test['output'])