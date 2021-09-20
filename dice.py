import random
import json

with open ( "input.json" ) as jsonfile:
    jsonObject = json.load ( jsonfile )
    jsonfile.close ( )

total: int = jsonObject['Total']
i: int = jsonObject['integer']
rolls: int = jsonObject['rolls']
dices: int = jsonObject['dices']


def roll():
    total: int = jsonObject['Total']
    i: int = jsonObject['integer']
    rolls: int = jsonObject['rolls']
    dices: int = jsonObject['dices']
    rolltotal: int = 0;
    a: int = 1;
    while i < rolls:
        for a in range ( 0, dices ):
            dice: int = random.randint ( 1, 6 );
            rolltotal = rolltotal + dice;
        i += 1
        total: int = rolltotal;
    return total
    # return json.dumps( total )


print ( roll ( ) )

json_output = dict ( Total=roll ( ), Rolled=rolls )
with open ( 'output.json', 'w' ) as jsonOut:
    json.dump ( json_output, jsonOut )
    jsonOut.close ( )
