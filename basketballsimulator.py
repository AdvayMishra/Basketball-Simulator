
#Basketball Simulator
print("\033[H\033[2J", end="")   # Clear screen
print("\033[H\033[3J", end="")   # Clear screen + scrollback
print("\033c", end="")           # Full terminal reset

import time
"""
Going to make 2 basketball teams: Team A and Team B
Players are being made using OOP, Object Oriented Programing
Players are going to have a shooting percentage and a blocking percentage
Each player has a unique name
Every turn there is a jump ball for possesion
Game will be simulation of 100 shots
Compare blocking percentage versus blocking percentage
Finding out which player performed the best in the match
"""
# __________________________________________________________________________________________________________
#Creates Names for all of the players in the game
import random

first_name_list = ["Steph", "Lebron", "Kobe", "John", "Mike", "Bob", "Jimmy", "Jordan", "Bruno", "Ruud"]
last_name_list = ["Curry", "James", "Bryant", "Smith", "Fernandes", "Gullit", "Jackson", "Garcia", "Lee"]

all_players_list = []

for i in range(15):
    player_name = (random.choice(first_name_list) + " " + random.choice(last_name_list))

#Checks if name is in all_players_list to make sure there is no duplicates
    if player_name not in all_players_list:
        all_players_list.append(player_name)

#__________________________________________________________________________________________________________
#Creating a class to define and start making the players
class player(object):
    def __init__(self, name, shooting_percentage, blocking_percentage, points):
        self.name = name
        self.shooting_percentage = shooting_percentage
        self.blocking_percentage = blocking_percentage
        self.points = points
#__________________________________________________________________________________________________________
#Creating Team A
print("_________________________________________________________________________________________________")
print("Team A Roster:\n")
A_team_player_1 = player(all_players_list[0], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(A_team_player_1.name))
print("Shooting Percentage: " + str(A_team_player_1.shooting_percentage))
print("Blocking Percentage: " + str(A_team_player_1.blocking_percentage))
print(" ")

A_team_player_2 = player(all_players_list[1], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(A_team_player_2.name))
print("Shooting Percentage: " + str(A_team_player_2.shooting_percentage))
print("Blocking Percentage: " + str(A_team_player_2.blocking_percentage))
print(" ")

A_team_player_3 = player(all_players_list[2], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(A_team_player_3.name))
print("Shooting Percentage: " + str(A_team_player_3.shooting_percentage))
print("Blocking Percentage: " + str(A_team_player_3.blocking_percentage))
print(" ")

A_team_player_4 = player(all_players_list[3], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(A_team_player_4.name))
print("Shooting Percentage: " + str(A_team_player_4.shooting_percentage))
print("Blocking Percentage: " + str(A_team_player_4.blocking_percentage))
print(" ")

A_team_player_5 = player(all_players_list[4], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(A_team_player_5.name))
print("Shooting Percentage: " + str(A_team_player_5.shooting_percentage))
print("Blocking Percentage: " + str(A_team_player_5.blocking_percentage))
print(" ")

# Tells us the team OVR(Overall Rating)

#Finding out the team's average shooting
AShootingOVR = (A_team_player_5.shooting_percentage + A_team_player_4.shooting_percentage + A_team_player_3.shooting_percentage + A_team_player_2.shooting_percentage + A_team_player_1.shooting_percentage)
ASovr = round(AShootingOVR/5)
print ("Team A Shooting: " + str(ASovr))

#Finding out the team's average blocking
ABlockingOVR = (A_team_player_5.blocking_percentage + A_team_player_4.blocking_percentage + A_team_player_3.blocking_percentage + A_team_player_2.blocking_percentage + A_team_player_1.blocking_percentage)
ABovr = round(ABlockingOVR/5)

print ("Team A Blocking: " + str(ABovr))

#Finding out the team rating
TeamAOvr = round((ABovr + ASovr)/2)
print("Team A OVR: " + str(TeamAOvr))

Team_A = [A_team_player_1,A_team_player_2,A_team_player_3,A_team_player_4,A_team_player_5]
print("_________________________________________________________________________________________________")
#__________________________________________________________________________________________________________
# Creating Team B

print("\nTeam B Roster:\n")
B_team_player_1 = player(all_players_list[5], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(B_team_player_1.name))
print("Shooting Percentage: " + str(B_team_player_1.shooting_percentage))
print("Blocking Percentage: " + str(B_team_player_1.blocking_percentage))
print(" ")

B_team_player_2 = player(all_players_list[6], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(B_team_player_2.name))
print("Shooting Percentage: " + str(B_team_player_2.shooting_percentage))
print("Blocking Percentage: " + str(B_team_player_2.blocking_percentage))
print(" ")

B_team_player_3 = player(all_players_list[7], random.randint(50, 100), random.randint(5, 100), points = 0)

print("Name: " + str(B_team_player_3.name))
print("Shooting Percentage: " + str(B_team_player_3.shooting_percentage))
print("Blocking Percentage: " + str(B_team_player_3.blocking_percentage))
print(" ")

B_team_player_4 = player(all_players_list[8], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(B_team_player_4.name))
print("Shooting Percentage: " + str(B_team_player_4.shooting_percentage))
print("Blocking Percentage: " + str(B_team_player_4.blocking_percentage))
print(" ")

B_team_player_5 = player(all_players_list[9], random.randint(50, 100), random.randint(50, 100), points = 0)

print("Name: " + str(B_team_player_5.name))
print("Shooting Percentage: " + str(B_team_player_5.shooting_percentage))
print("Blocking Percentage: " + str(B_team_player_5.blocking_percentage))
print(" ")

# Tells us the team OVR(Overall Rating)
ShootingOVR = (B_team_player_5.shooting_percentage + B_team_player_4.shooting_percentage + B_team_player_3.shooting_percentage + B_team_player_2.shooting_percentage + B_team_player_1.shooting_percentage)
Sovr = round(ShootingOVR/5)
print ("Team B Shooting: " + str(Sovr))

BlockingOVR = (B_team_player_5.blocking_percentage + B_team_player_4.blocking_percentage + B_team_player_3.blocking_percentage + B_team_player_2.blocking_percentage + B_team_player_1.blocking_percentage)
Bovr = round(BlockingOVR/5)

print ("Team B Blocking: " + str(Bovr))

#Finding out the team rating
TeamBOvr = round((Bovr + Sovr)/2)
print("Team B OVR: " + str(TeamBOvr))
print("_________________________________________________________________________________________________")

Team_B = [B_team_player_1, B_team_player_2, B_team_player_3, B_team_player_4, B_team_player_5]
#__________________________________________________________________________________________________________

# Making the Main game
Team_Score_A = 0
Team_Score_B = 0
countdown = 100
while countdown > 0:
    countdown = countdown - 1
    if countdown in [75, 50, 25, 0]:
        time.sleep(0.001)
        print("###########################################################################")
        print("Team A Score: " + str(Team_Score_A) + " Team B Score: " + str(Team_Score_B))
        print("###########################################################################")
    #choosing a player from each team
    player_A = random.choice(Team_A)
    player_B = random.choice(Team_B)

    #choosing which team has ball
    Start_Ball = random.randint(1,2)
    if Start_Ball == 1:
        print("Team A starts with ball")
    else:
        print("Team B starts with ball")



    #comparing the blocking and shooting
    if Start_Ball == 1:
        player_A.shooting_percentage - player_B.blocking_percentage
    else:
        player_B.shooting_percentage - player_A.blocking_percentage

    #if player's blocking is higher give ball to opposing team
    if Start_Ball == 1:
        if player_A.shooting_percentage - player_B.blocking_percentage < 0:
            print(player_A.name + " recieves the ball. He dribbles up... and " + player_B.name + " steals the ball from him!")
            if Start_Ball == 1:
                print("Team A gets the ball")
            else:
                print("Team B get the ball")
    else:
        if player_B.shooting_percentage - player_A.blocking_percentage < 0:
            print(player_B.name + " recieves the ball. He dribbles up... and " + player_A.name + " steals the ball from him!")
            if Start_Ball == 2:
                print("Team A gets the ball")
            else:
                print("Team B get the ball")

    #if player's shooting is higher roll to see if player makes it
    shooting_chance = random.randint(0,100)
    points = random.randint(2,3)
    if Start_Ball == 1:
        if player_A.shooting_percentage - player_B.blocking_percentage > 0:
            if shooting_chance > player_A.shooting_percentage - player_B.blocking_percentage:
                print(player_A.name + " recieves the ball. He dribbles up... and " + player_B.name + " distracts him, making him miss!")
            else:
                print(player_A.name + " jukes out Team B... He faces up againts " + player_B.name + ", breaks his ankles and shoots... HE MAKES IT!!!\n")
                if points == 3:
                    Team_Score_A = Team_Score_A + 3
                    player_A.points = player_A.points + 3
                else:
                    Team_Score_A = Team_Score_A + 2
                    player_A.points = player_A.points + 2
    else:
        if player_B.shooting_percentage - player_A.blocking_percentage > 0:
            if shooting_chance > player_B.shooting_percentage - player_A.blocking_percentage:
                print(player_B.name + " recieves the ball. He dribbles up... and " + player_A.name + " distracts him, making him miss!")
            else:
                print(player_B.name + " jukes out Team A... He faces up againts " + player_A.name + ", breaks his ankles and shoots... HE MAKES IT!!!\n")
                if points == 3:
                    Team_Score_B = Team_Score_B + 3
                    player_B.points = player_B.points + 3
                else:
                    Team_Score_B = Team_Score_B + 2
                    player_B.points = player_B.points + 2
# __________________________________________________________________________________________________________
#tell who won
time.sleep(1)
if Team_Score_A < Team_Score_B:
    print("\n============")
    print("Team B Wins!")
    print("============")
elif Team_Score_A > Team_Score_B:
    print("\n============")
    print("Team A Wins!")
    print("============")
if Team_Score_A == Team_Score_B:
#Creates an overtime function that runs when both teams are tied
    print("")
    print("OVERTIME!")
    print("Teams are tied. Playing 50 more shots...")
    print("")
    #number of shots played in overtime
    overtime = 50

    while overtime > 0:

        overtime = overtime - 1

        player_A = random.choice(Team_A)
        player_B = random.choice(Team_B)

        Start_Ball = random.randint(1,2)

        shooting_chance = random.randint(0,100)
        points = random.randint(2,3)

        #comparing the blocking and shooting
        if Start_Ball == 1:

            print("Team A starts with ball")

            if player_A.shooting_percentage - player_B.blocking_percentage < 0:

                print(player_A.name + " receives the ball. He dribbles up... and " +
                    player_B.name + " steals the ball from him!")

            else:

                if shooting_chance > player_A.shooting_percentage - player_B.blocking_percentage:

                    print(player_A.name + " receives the ball. He dribbles up... and " +
                        player_B.name + " distracts him, making him miss!")

                else:

                    print(player_A.name + " jukes out Team B... He faces up against " +
                        player_B.name + ", breaks his ankles and shoots... HE MAKES IT!!!\n")

                    Team_Score_A = Team_Score_A + points

        else:

            print("Team B starts with ball")

            if player_B.shooting_percentage - player_A.blocking_percentage < 0:

                print(player_B.name + " receives the ball. He dribbles up... and " +
                    player_A.name + " steals the ball from him!")

            else:

                if shooting_chance > player_B.shooting_percentage - player_A.blocking_percentage:

                    print(player_B.name + " receives the ball. He dribbles up... and " +
                        player_A.name + " distracts him, making him miss!")

                else:

                    print(player_B.name + " jukes out Team A... He faces up against " +
                        player_A.name + ", breaks his ankles and shoots... HE MAKES IT!!!\n")

                    Team_Score_B = Team_Score_B + points

# __________________________________________________________________________________________________________
    #Prints Overtime final Score and replays overtime if teams are STILL tied
    print("")
    print("OVERTIME FINAL SCORE")
    print("Team A Score: " + str(Team_Score_A))
    print("Team B Score: " + str(Team_Score_B))

    if Team_Score_A > Team_Score_B:
        print("Team A wins in overtime!!!")

    elif Team_Score_B > Team_Score_A:
        print("Team B wins in overtime!!!")
    else:
        print("")
        print("Double OVERTIME!")
        print("Teams are tied. Playing 50 more possessions...")
        print("")
    
        overtime = 50
    
        while overtime > 0:
    
            overtime = overtime - 1
    
            player_A = random.choice(Team_A)
            player_B = random.choice(Team_B)
    
            Start_Ball = random.randint(1,2)
    
            shooting_chance = random.randint(0,100)
            points = random.randint(2,3)
    
            if Start_Ball == 1:
    
                print("Team A starts with ball")
    
                if player_A.shooting_percentage - player_B.blocking_percentage < 0:
    
                    print(player_A.name + " receives the ball. He dribbles up... and " +
                            player_B.name + " steals the ball from him!")
    
                else:
    
                    if shooting_chance > player_A.shooting_percentage - player_B.blocking_percentage:
    
                        print(player_A.name + " receives the ball. He dribbles up... and " +
                                player_B.name + " distracts him, making him miss!")
    
                    else:
    
                        print(player_A.name + " jukes out Team B... He faces up against " +
                                player_B.name + ", breaks his ankles and shoots... HE MAKES IT!!!")
    
                        Team_Score_A = Team_Score_A + points
    
            else:
    
                print("Team B starts with ball")
    
                if player_B.shooting_percentage - player_A.blocking_percentage < 0:
    
                    print(player_B.name + " receives the ball. He dribbles up... and " +
                            player_A.name + " steals the ball from him!")
    
                else:
    
                    if shooting_chance > player_B.shooting_percentage - player_A.blocking_percentage:
    
                        print(player_B.name + " receives the ball. He dribbles up... and " +
                                player_A.name + " distracts him, making him miss!")
    
                    else:
    
                        print(player_B.name + " jukes out Team A... He faces up against " +
                                player_A.name + ", breaks his ankles and shoots... HE MAKES IT!!!")
    
                        Team_Score_B = Team_Score_B + points
            if Team_Score_A > Team_Score_B:
                    print("Team A wins in overtime!!!")
                    print("")
            elif Team_Score_B > Team_Score_A:
                print("Team B wins in overtime!!!")
                print("")
            else:
                winner = random.randint(1,2)
                if winner == 1:
                    print("Team A wins in overtime!!!")
                    print("")
                else:
                    print("Team B wins in overtime!!!")
                    print("")
# __________________________________________________________________________________________________________
#tells us who was MVP (Most valuable player)

Team_A.extend(Team_B)

# Start MVP as the first real player instead of a fake player
MVP_player = Team_A[0]

MVP_players_list = [MVP_player.name]

#Checks each players points and appends them to the MVP list if they have as much or beat the current MVP
for individual_player in Team_A:
    print(individual_player.name + " Points: " + str(individual_player.points))

    if individual_player.points > MVP_player.points:
        MVP_player = individual_player
        MVP_players_list[0] = individual_player.name

    elif individual_player.points == MVP_player.points:

        Mvp_Ovr = round((MVP_player.shooting_percentage + MVP_player.blocking_percentage)/2)

        Individual_Player_Ovr = round((individual_player.shooting_percentage + individual_player.blocking_percentage)/2)

        # Higher OVR wins the tiebreak
        if Individual_Player_Ovr > Mvp_Ovr:
            MVP_player = individual_player
            MVP_players_list[0] = individual_player.name

        # If OVR is tied, randomly select one
        elif Individual_Player_Ovr == Mvp_Ovr:

            MVPwinner = random.randint(1,2)

            if MVPwinner == 1:
                MVP_player = individual_player
                MVP_players_list[0] = individual_player.name

# Calculates final MVP OVR
Mvp_Ovr = round((MVP_player.shooting_percentage + MVP_player.blocking_percentage)/2)

# Prints the MVP for the user to see
print("\n====================")
print("MVP")
print("====================")
print("Name: " + MVP_player.name)
print("Points: " + str(MVP_player.points))
print("Shooting: " + str(MVP_player.shooting_percentage))
print("Blocking: " + str(MVP_player.blocking_percentage))
print("OVR: " + str(Mvp_Ovr))
print(MVP_player.name)
