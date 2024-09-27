from pyswip import Prolog

prolog = Prolog()

prolog.consult("game.pl")

genres = {
    "action", "adventure", "rpg", "strategy", "simulation",
    "sports", "puzzle", "shooter", "platformer", "horror",
    "racing", "fighting", "mmorpg", "sandbox", "stealth",
    "survival", "rhythm", "visual_novel", "roguelike", "metroidvania"
}

genres_check = {
    "rpg", "shooter", "valve", "popular", "indie",
    "classic", "challenging"
}

developers = {
    "cd_projekt_red", "mojang", "valve", "ea_sports", "alexey_pajitnov", "nintendo",
    "firaxis_games", "rockstar_games", "valve", "fromsoftware"
}

games = {
    "witcher_3", "minecraft", "counter_strike", "fifa_23", "tetris", "mario_bros",
    "civilization_vi", "grand_theft_auto_v", "portal", "dark_souls", "fortnite",
    "stardew_valley", "mortal_kombat", "world_of_warcraft", "resident_evil"
}
def search_by_genre():
    genre = input(f"Enter game genre '{genres}': \n")
    query = f"game(Game, {genre})"
    games = list(prolog.query(query))
    if games:
        print(f"\nList of games in this category '{genre}': ")
        for game in games:
            print(game["Game"])
    else:
        print(f"\nThere are no games in this category '{genre}' in our list!")

def search_by_developer():
    developer = input(f"Enter name of developer '{developers}': ")
    query = f"developer(Game, {developer})"
    games = list(prolog.query(query))
    if games:
        print(f"\nList of games were produced by '{developer}': ")
        for game in games:
            print(game["Game"])
    else:
        print(f"\nThere are not games, which were created by '{developer}' in our list!")

def check():
    print("Enter the game name and game genre you want to check\n")
    genre = input(f"Enter game genre '{genres_check}': ")
    game = input(f"Enter game '{games}':\n")
    if genre == "rpg":
        query = f"is_rpg({game})"
    elif genre == "shooter" :
        query = f"is_shooter({game})"
    elif genre == "valve":
        query = f"valve_game({game})"
    elif genre == "popular":
        query = f"popular({game})"
    elif genre == "indie":
        query = f"indie_game({game})"
    elif genre == "classic":
        query = f"classic_game({game})"
    elif genre == "challenging":
        query = f"challenging_game({game})"
    result = list(prolog.query(query))
    if result:
        print(f"{game} is suitable for the genre {genre}.")
    else:
        print(f"{game} is not suitable for the genre {genre}.")

def ask():
    condition = True
    while condition:
        print("\n")
        print("-----------------------------------------------------")
        print("What do you want to do?")
        print("1. Search games by genre")
        print("2. Search games by developer")
        print("3. Check if a game is rpg, shooter, valve, popular, indie, classic, challenging")
        print("4. Exit")
        try:
            number = int(input("Enter a number: "))
            if number == 1:
                search_by_genre()
            elif number == 2:
                search_by_developer()
            elif number == 3:
                check()
            elif number == 4:
                condition = False
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")




if __name__ == '__main__':
    ask()


