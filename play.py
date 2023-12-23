
players = {}
next_player = True
while next_player:
    name = input("Welcome! \n Type your name: ")
    bid = input("Type your bid: ")
    bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    players[name] = bid
    if bidders != 'yes':
        next_player = False

for key, value in players.items():
    winner = 0
    
    if int(value) > winner:
        winner = value
        name_of_winner = key

print(winner)
print(players )
print(f"The auction won {name_of_winner}, he bet {winner}")





















