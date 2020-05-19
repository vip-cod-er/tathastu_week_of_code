player1= input("Enter the runs skored by player 1 in 60 balls : ")
player2= input("Enter the runs skored by player 2 in 60 balls : ")
player3= input("Enter the runs skored by player 3 in 60 balls : ")
strike_player1= float(player1)*100/600
strike_player2= float(player2)*100/600
strike_player3= float(player3)*100/600
print("\nStrike rate of player 1 : ",strike_player1)
print("Strike rate of player 2 : ",strike_player2)
print("Strike rate of player 3 : ",strike_player3)
print("\nIf each player played 60 more balls then score of player 1 will be : ",int(player1)*2)
print("If each player played 60 more balls then score of player 2 will be : ",int(player2)*2)
print("If each player played 60 more balls then score of player 3 will be : ",int(player3)*2)
print("\nMaximum number of sixes that player 1 could hit : ",int(player1)//6)
print("Maximum number of sixes that player 2 could hit : ",int(player2)//6)
print("Maximum number of sixes that player 3 could hit : ",int(player3)//6)
