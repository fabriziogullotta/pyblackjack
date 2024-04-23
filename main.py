import random;

#Number of players
nPlayers = 1
#Deck
deck = [];
#Starting n° cards
startPhase = 2;
#Players' hands
hands = {}
#Cpu's hand
cpu = []

#Players configuration
def configPlayers():
	#Create players records
	for item in range(nPlayers):
		hands['player_'+str(item)] = [];
	return hands;

#Refill the deck with cards
def refillDeck():
	#Full deck
	cards = ['A','A','A','A',
		2,2,2,2,
		3,3,3,3,
		4,4,4,4,
		5,5,5,5,
		6,6,6,6,
		7,7,7,7,
		8,8,8,8,
		9,9,9,9,
		10,10,10,10,
		'J','J','J','J',
		'Q','Q','Q','Q',
		'K','K','K','K']
	return cards

#Remove a card from the deck
def removeCard(card):
	deck.remove(card)

#Draw a card from the deck
def drawCard(entity,deck):
	#Check if there is at least 1 card to draw
	if len(deck) > 0:
		#Pick a random card
		card = random.randint(0,len(deck)-1)
		#Add card to player's hand
		hands[entity].append(deck[card])
		#Remove the card from the deck
		removeCard(deck[card])

#Draw a card from the deck for CPU
def drawCardCPU(entity,deck):
	#Check if there is at least 1 card to draw
	if len(deck) > 0:
		#Pick a random card
		card = random.randint(0,len(deck)-1)
		#Add card to cpu's hand
		entity.append(deck[card])
		#Remove card from the deck
		removeCard(deck[card])

#Show hand with just some stuff to print
def showHand(player,entity):
	print("============")
	print(player.upper() + " Hand: " + str(entity))
	print(player.upper() + " Total: " + str(cardsValue(entity)))
	print("###################")

#Calculate cards value
def cardsValue(entity):
	total = 0
	value = 0
	#For every card in hand, check if a figure, ace or normal, and set the value
	for card in entity:
		if card == 'J' or card == 'Q' or card == 'K':
			value = 10
		elif card == 'A':
			# TODO! Change value between 1 or 11
			value = 11
		else:
			value = card
	#Sum all values and return the total
		total += int(value)
	return total

#All winning/losing checks
def checkResult(player,cpu):
	#Player or CPU over 21
	if player <= 21:
	#Player winning
		if cpu > 21:
			print("You win!")
	#CPU winning 
		elif player < cpu:
			print("You lose!")
	#Draw
		elif player == cpu:
			print("Draw!")
	#Player winning
		else:
			print("You win!")
	#CPU winning 
	else:
		print("You lose!")

def main():
	#Initialize hands and deck
	hands = configPlayers()
	deck = refillDeck()
	#Start serving cards based on starting N° cards
	for turn in range(startPhase):
		#Players
		for elem in hands:
			drawCard(elem,deck)
		#CPU
		drawCardCPU(cpu,deck)
	for player in hands:
		playerVal = cardsValue(hands[player])
		showHand(player,hands[player])
		while playerVal <= 21:
			#Ask player what to do
			playerChoice = input("1)Draw\n2)Hit\n")
			if playerChoice == "2":
				drawCard(player,deck)
				showHand(player,hands[player])
				playerVal = cardsValue(hands[player])
			elif playerChoice == "1":
				showHand(player,hands[player])
				break
		cpuVal = cardsValue(cpu)
		showHand("CPU",cpu)
		if playerVal <= 21:
			while cpuVal < playerVal:
				#CHECK
				drawCardCPU(cpu,deck)
				cpuVal = cardsValue(cpu)
				showHand("CPU",cpu)
		#Check the winner
		checkResult(playerVal,cpuVal)
		
if __name__ == '__main__':
	main()