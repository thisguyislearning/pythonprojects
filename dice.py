import random
import json


with open ( "input.json" ) as jsonfile:
    jsonObject = json.load ( jsonfile )
    jsonfile.close ( )

total: int = jsonObject['Total']
i: int = jsonObject['integer']
rolls: int = jsonObject['rolls']

def roll():
    total: int = jsonObject['Total']
    i: int = jsonObject['integer']
    rolls: int = jsonObject['rolls']
    roll: int = 0;
    while i < rolls:
        dice1 = random.randint ( 1, 6 );
        dice2 = random.randint ( 1, 6 );
        dice3 = random.randint ( 1, 6 );
        i += 1
        roll: int = dice1 + dice2 + dice3;
        total: int = total + roll;
    return total
    # return json.dumps( total )


print ( roll ( ) )

json_output = dict ( Total=roll ( ), Rolled=rolls )
with open('output.json','w') as jsonOut:
    json.dump(json_output, jsonOut)
    jsonOut.close()