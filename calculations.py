"""
This file is for calculations
"""
import time
from database import fetch_player_rank

SCORE_PT_BONUS = [[30, 10, -10, -30], [30, 0, -30]]  # 4-person game, 3-person game
RANK_NORMALISING = [(-6, 2), (-3, 3), (-2, 6)]  # Ascending number of A ranks


def calculate_game(player_ids: [str], match_type: bool, player_scores: [int], t: float = None):
    """
    Wrapper functions for 3-person and 4-person games *** IF THE 4th object of _player_id_ isq None,
    \it will indicate that it is a 3-person game
    :param player_ids: player ids from database
    :param match_type: east/south match
    :param player_scores: player scores inputted by uploader
    :param t: time of upload/time of match
    :return: None?
    """

    player_ranks = [fetch_player_rank(player) for player in player_ids]
    # Fetches the current rank of each player from database

    zipped_players = list(zip(player_scores, player_ids, player_ranks))

    sorted_zipped = sorted(zipped_players, key=lambda x: x[0] if x[0] is not None else float('-inf'), reverse=True)

    player_scores_sorted, player_ids_sorted, player_ranks_sorted = zip(sorted_zipped)
    player_scores_sorted = list(player_scores_sorted)
    player_ids_sorted = list(player_ids_sorted)
    player_ranks_sorted = list(player_ranks_sorted)
    # Sorts the players according to the scores for each player in descending order

    if t is None:
        t = time.time()
    # Time of the match being recorded
    if player_scores_sorted[3] is None:
        calc_3_person_game(player_ids_sorted, match_type, player_scores_sorted, player_ranks_sorted, t)
    else:
        calc_4_person_game(player_ids_sorted, match_type, player_scores_sorted, player_ranks_sorted, t)


def calc_3_person_game(player_ids: [str], match_type: bool, player_scores: [int], player_ranks: [int], t: float):
    ...


def calc_4_person_game(player_ids: [str], match_type: bool, player_scores: [int], player_ranks: [int], t: float):
    ...