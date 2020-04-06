import requests
import datetime

key = "a123e0a3-4246-46db-a5e5-c726a59891e4"

while True:
    #key = input("Please enter your API key: ")
    playerName = input("Which player would you like to look at: ")
    if playerName == 'stop':
        sure = input("Are you sure you want to close the program [Y/N]")
        if sure == 'y' or sure == 'Y':
            exit()
    else:
            data = requests.get("https://api.hypixel.net/player?key=" + key + "&name=" + playerName).json()
            player = data["player"] if "player" in data else None
            if (player == None):
                print("Nope")
                continue
            
            mostRecentLogin = player["lastLogin"]
            lastLogout = player["lastLogout"]
            loggedInTime = (lastLogout - mostRecentLogin)/1000/60            

            mcVersionRp = player["mcVersionRp"]
            userLanguage = player["userLanguage"] if "userLanguage" in player else "English"
            mostRecentGame = player["mostRecentGameType"]
            SkywarsMode = player["stats"]["SkyWars"]["lastMode"]
            duelsMode = player["stats"]["Duels"]["duels_recently_played"]
            date = datetime.datetime.fromtimestamp(mostRecentLogin/1000).strftime('%c')

            print("The most recent login was on :" + (date))
            print("Player was logged in for {:3.1} minutes".format(loggedInTime))
            #print("The account played for : " + sessionPlaytime)
            print("The most recent version was " + mcVersionRp)
            print("The players language is set to :" + userLanguage)
            recentGame = "The most recent game played on the account was: "# + mostRecentGame)


            if mostRecentGame == 'SKYBLOCK':
                print(recentGame + "SkyBlock")
            elif mostRecentGame == 'SPEEDUHC':
                print(recentGame + "Speed UHC")
            elif mostRecentGame == 'SKYWARS':
                print(recentGame + "SkyWars(" + SkywarsMode + ")" )
            elif mostRecentGame == 'SKYCLASH':
                print(recentGame + "SkyClash")
            elif mostRecentGame == 'SuperSmash':
                print(recentGame + "Smash Heros")
            elif mostRecentGame == 'HungerGames':
                print(recentGame + "Blitz Survival Games")
            elif mostRecentGame == 'Arcade':
                print(recentGame + "Arcade")
            elif mostRecentGame == 'Walls':
                print(recentGame + "Walls")
            elif mostRecentGame == 'VampireZ':
                print(recentGame + "VampireZ")
            elif mostRecentGame == 'Arena':
                print(recentGame + "Arena")
            elif mostRecentGame == 'Quake':
                print(recentGame + "QuakeCraft")
            elif mostRecentGame ==  'Paintball':
                print(recentGame + "PaintBall")
            elif mostRecentGame ==  'Gingerbread':
                print(recentGame + "Turbo Kart Racers")
            elif mostRecentGame ==  'MCGO':
                print(recentGame + "Cops 'n' Crims")
            elif mostRecentGame == 'TNTGames':
                print(recentGame + "TNT Games")
            elif mostRecentGame ==  'Walls3':
                print(recentGame + "Mega Walls")
            elif mostRecentGame ==  'UHC':
                print(recentGame + "UHC Champions")
            elif mostRecentGame == 'BattleGround':
                print(recentGame + "WarLords")
            elif mostRecentGame == 'TrueCombat':
                print(recentGame + "Crazy Walls")
            elif mostRecentGame ==  'Duels':
                print(recentGame + "Duels")#(" + duelsMode + ")")
            elif mostRecentGame ==  'BedWars':
                print(recentGame + "BedWars")
            elif mostRecentGame ==  'MurderMystery':
                print(recentGame + "Murder Mystery")
            elif mostRecentGame ==  'BuildBattle':
                print(recentGame + "Build Battle")
            elif mostRecentGame ==  'Legacy':
                print(recentGame + "Classic Games")
            elif mostRecentGame ==  'Pit':
                print(recentGame + "The Pit")
            elif mostRecentGame ==  'SkyBlock':
                print(recentGame + "SkyBlock")
            elif mostRecentGame == 'Housing':
                print(recentGame + "Housing")
            else:
                print(recentGame + "Unknown")
            print("\n")

