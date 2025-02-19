% Факты с одним аргументом (жанры игр)
genre(action).
genre(adventure).
genre(rpg).
genre(strategy).
genre(simulation).
genre(sports).
genre(puzzle).
genre(shooter).
genre(platformer).
genre(horror).
genre(racing).
genre(fighting).
genre(mmorpg).
genre(sandbox).
genre(stealth).
genre(survival).
genre(rhythm).
genre(visual_novel).
genre(roguelike).
genre(metroidvania).

% Факты с двумя аргументами (игры и их жанры)
game(witcher_3, rpg).
game(minecraft, sandbox).
game(counter_strike, shooter).
game(fifa_23, sports).
game(tetris, puzzle).
game(mario_bros, platformer).
game(civilization_vi, strategy).
game(grand_theft_auto_v, action).
game(portal, puzzle).
game(dark_souls, rpg).
game(fortnite, shooter).
game(stardew_valley, simulation).
game(mortal_kombat, fighting).
game(world_of_warcraft, mmorpg).
game(resident_evil, horror).

% Факты с двумя аргументами (игры и их разработчики)
developer(witcher_3, cd_projekt_red).
developer(minecraft, mojang).
developer(counter_strike, valve).
developer(fifa_23, ea_sports).
developer(tetris, alexey_pajitnov).
developer(mario_bros, nintendo).
developer(civilization_vi, firaxis_games).
developer(grand_theft_auto_v, rockstar_games).
developer(portal, valve).
developer(dark_souls, fromsoftware).

% Правила
% Игра является RPG, если она относится к жанру RPG
is_rpg(Game) :- game(Game, rpg).

% Игра является шутером, если она относится к жанру shooter
is_shooter(Game) :- game(Game, shooter).

% Игра разработана компанией Valve, если Valve указана как разработчик
valve_game(Game) :- developer(Game, valve).

% Игра является популярной, если она относится к жанру shooter или rpg
popular_game(Game) :- game(Game, shooter); game(Game, rpg).

% Игра является инди, если ее разработчик - небольшая студия (пример)
indie_game(Game) :- developer(Game, Developer),
                    Developer \= ea_sports,
                    Developer \= rockstar_games,
                    Developer \= valve.

% Игра является классикой, если она была выпущена до 2000 года (пример)
classic_game(tetris).
classic_game(mario_bros).

% Игра рекомендуется для любителей сложных игр, если она RPG или относится к жанру souls-like
challenging_game(Game) :- is_rpg(Game), developer(Game, fromsoftware).

