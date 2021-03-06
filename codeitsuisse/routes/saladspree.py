import logging
import json
import numpy as np

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/salad-spree', methods=['POST'])
def evaluateSalad():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    numberOfSalads = data.get("number_of_salads")
    streetArray = data.get("salad_prices_street_map")
    result = {"result" : saladSpree(numberOfSalads, streetArray)}
    logging.info("My result :{}".format(result))
    return jsonify(result)

def saladSpree(numberOfSalads, streetArray):
    min_ = 0
    strlen = len(streetArray[0])
    for i, street in enumerate(streetArray):
        j = 0
        while (j) < strlen-numberOfSalads:
            tmp = street[j:j+numberOfSalads]
                
            if "X" in tmp:
                d = tmp.index("X")
                j += d + 1
                continue

            else: 
                sum_ = eval("+".join(street[j:j+numberOfSalads]))
                if min_ == 0 or min_ > sum_:
                    min_ = sum_
                j += 1

            # print(street[j:j+numberOfSalads])
        
    return min_

# def saladSpree(numberOfSalads, streetArray):
#     charArr = np.array([np.array(x) for x in streetArray])
#     min_ = 0
#     X = min_
#     for i, street in enumerate(charArr):
#         for j, stall in enumerate(street[:-numberOfSalads]):
#             tmp = charArr[i][j:j+numberOfSalads]
#             sum_ = eval("+".join(charArr[i][j:j+numberOfSalads]))
#             if min_ == 0 or min_ > sum_:
#                 min_ = sum_
#                 X = min_ + 1
#     return min_

# def saladSpree(numberOfSalads, streetArray):
#     n = len(streetArray[0])
#     currentSum = 0
#     for street in streetArray:
#         lenOfStreet = len(street) #finding out the length of the street
#         noOfX = 0
#         noOfShops = 0
#         sumOnStreet = 0 #This will be the value stored on each street
#         for index in range(len(street)):
#             if (street[index]!="X"):
#                 noOfShops += 1
#                 sumOnStreet+=int(street[index])
#                 if (noOfShops == numberOfSalads): #When the current number of shops matches the no of required salads
#                     if (currentSum==0 or currentSum>sumOnStreet): #Assigning the minimum sum
#                         currentSum = sumOnStreet
#                     if (index-numberOfSalads>=0):
#                         sumOnStreet-=int(street[index-numberOfSalads]) #Minusing the previous element that is no longer needed  
#             else:
#                 noOfX+=1
#                 sumOnStreet=0
#                 if (len(street)-index<numberOfSalads): #Check the number of remaining indexes shops are enough
#                     break #Break out of the current street and move on the other street
#     return currentSum

# def saladSpree(numberOfSalads, streetArray):
#     n = len(streetArray[0])
#     currentSum = 0
#     for street in streetArray:
#         i=0
#         while i < n-numberOfSalads:
#             if all([x.isnumeric() for x in street[i:i+numberOfSalads]]):
#                 sum_ = sum([int(x) for x in street[i:i+numberOfSalads]])
#                 i+=1
#                 if not currentSum:
#                     currentSum = sum_
#                 else :
#                     if sum_ < currentSum:
#                         currentSum = sum_
#             else:
#                 i += "".join(street[i:i+numberOfSalads]).rindex("X")
#     return currentSum