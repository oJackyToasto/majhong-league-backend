import sqlite3
import os

MATCH_DB_ADDR = "databases/matches.db"
PLAYERS_DB_ADDR = "databases/players.db"


def init_db():  # Initializes the database

    if not os.path.exists(f"{os.curdir}/databases"):  # Init databases directory if not exist
        os.mkdir(f"{os.curdir}/databases")

    matches = sqlite3.connect(MATCH_DB_ADDR)

    cursor = matches.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS matches_four (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        time REAL NOT NULL,
        match_type INTEGER DEFAULT 0,
        player_1 TEXT UNIQUE,
        player_1_rank INTEGER NOT NULL,
        player_1_score INTEGER NOT NULL,
        player_1_pt REAL NOT NULL,
        player_2 TEXT UNIQUE,
        player_2_rank INTEGER NOT NULL,
        player_2_score INTEGER NOT NULL,
        player_2_pt REAL NOT NULL,
        player_3 TEXT UNIQUE,
        player_3_rank INTEGER NOT NULL,
        player_3_score INTEGER NOT NULL,
        player_3_pt REAL NOT NULL,
        player_4 TEXT UNIQUE,
        player_4_rank INTEGER NOT NULL,
        player_4_score INTEGER NOT NULL,
        player_4_pt REAL NOT NULL
    )
''')  # database for 4 person majhong
    matches.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches_three (
            game_id INTEGER PRIMARY KEY AUTOINCREMENT,
            time REAL NOT NULL,
            match_type INTEGER DEFAULT 0,
            player_1 TEXT UNIQUE,
            player_1_rank INTEGER NOT NULL,
            player_1_score INTEGER NOT NULL,
            player_1_pt REAL NOT NULL,
            player_2 TEXT UNIQUE,
            player_2_rank INTEGER NOT NULL,
            player_2_score INTEGER NOT NULL,
            player_2_pt REAL NOT NULL,
            player_3 TEXT UNIQUE,
            player_3_rank INTEGER NOT NULL,
            player_3_score INTEGER NOT NULL,
            player_3_pt REAL NOT NULL
        )
    ''')  # database for 3 person majhong
    matches.commit()
    matches.close()

    players = sqlite3.connect(PLAYERS_DB_ADDR)
    cursor = players.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players (
        player_id TEXT PRIMARY KEY,
        player_name TEXT NOT NULL,
        player_rank INTEGER DEFAULT 2,
        player_current_pt REAL DEFAULT 0,
        player_total_pt REAL DEFAULT 0,
        total_game_played INTEGER DEFAULT 0,
        first_ranked_games INTEGER DEFAULT 0,
        second_ranked_games INTEGER DEFAULT 0,
        third_ranked_games INTEGER DEFAULT 0,
        fourth_ranked_games INTEGER DEFAULT 0,
        top_raw_score INTEGER DEFAULT 0,
        player_current_pt_t REAL DEFAULT 0,
        player_total_pt_t REAL DEFAULT 0,
        total_game_played_t INTEGER DEFAULT 0,
        first_ranked_games_t INTEGER DEFAULT 0,
        second_ranked_games_t INTEGER DEFAULT 0,
        third_ranked_games_t INTEGER DEFAULT 0,
        top_raw_score_t INTEGER DEFAULT 0
    )
    ''')  # database for players

    players.commit()
    players.close()


def add_game(t: float, match_type: bool, player_no: int, player_ids: [str], player_ranks: [int], player_scores: [int],
             player_pt: [float]):  # Adds a game into the database
    if match_type:
        match_type = 1
    else:
        match_type = 0

    conn = sqlite3.connect(MATCH_DB_ADDR)
    cursor = conn.cursor()
    if player_no == 4:
        cursor.execute("INSERT INTO matches_four (t, match_type, player_1, player_2, player_3, player_4, "
                       "player_1_rank, player_2_rank, player_3_rank, player_4_rank, player_1_score, player_2_score, "
                       "player_3_score, player_4_score, player_1_pt, player_2_pt, player_3_pt, player_4_pt) VALUES (?, ?, "
                       "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (t, match_type, player_ids[0],
                                                                              player_ids[1], player_ids[2],
                                                                              player_ids[3],
                                                                              player_ranks[0], player_ranks[1],
                                                                              player_ranks[2], player_ranks[3],
                                                                              player_scores[0], player_scores[1],
                                                                              player_scores[2], player_scores[3],
                                                                              player_pt[0], player_pt[1], player_pt[2],
                                                                              player_pt[3]))
    else:
        cursor.execute("INSERT INTO matches_three (t, match_type, player_1, player_2, player_3, "
                       "player_1_rank, player_2_rank, player_3_rank, player_1_score, player_2_score, "
                       "player_3_score, player_1_pt, player_2_pt, player_3_pt) VALUES (?, ?, "
                       "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (t, match_type, player_ids[0],
                                                                              player_ids[1], player_ids[2],
                                                                              player_ranks[0], player_ranks[1],
                                                                              player_ranks[2],
                                                                              player_scores[0], player_scores[1],
                                                                              player_scores[2],
                                                                              player_pt[0], player_pt[1], player_pt[2]))
    conn.commit()
    conn.close()

    update_players(player_ids)


def add_player(player_id: str, player_name: str, player_rank: int = None):  # Adds a new player with no data
    if player_rank is None:
        player_rank = 2

    conn = sqlite3.connect(PLAYERS_DB_ADDR)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (player_id, player_name, player_rank) VALUES (?, ?, ?)",
                   (player_id, player_name, player_rank))
    conn.commit()
    conn.close()


def change_player_rank():
    ...


def fetch_game():
    ...


def fetch_player_by_id(player_id) -> tuple:  # fetches a player's data
    conn = sqlite3.connect(PLAYERS_DB_ADDR)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE player_id = ?", (player_id,))
    player = cursor.fetchone()
    conn.commit()
    conn.close()
    return player


def update_players(player_ids: [str]):  # updates all players passed in
    for player_id in player_ids:
        update_player(player_id)

    # TODO: add logic


def update_player(player_id: str):  # updates the player
    ...


def fetch_player_rank(player_id) -> int:
    return list(fetch_player_by_id(player_id))[2]



if __name__ == '__main__':
    test_player_id = "aaa"
    fetch_player_rank(test_player_id)
