import random
    
def getChoices( pChoice ):
    listCompChoices = ['Rock', 'Paper', 'Scissors'] 
    dictChoices = { 'player_choice': random.choice( listCompChoices ), 'computer_choice': random.choice( listCompChoices ) }
    return dictChoices

for i in range(10):
        print( getChoices('Rock') )

