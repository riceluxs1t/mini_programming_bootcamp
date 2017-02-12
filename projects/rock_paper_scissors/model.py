import signal
from contextlib import contextmanager


"""
Exception that gets triggered when a function times out.
"""


class TimeoutException(Exception):
    pass


"""
A context manager registered to trigger TimeOutException.
"""


@contextmanager
def context_manager_time_limit(seconds=0.01):
    def signal_handler(signum, frame):
        raise TimeoutException("The move timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class RockPaperScissorsModel:

    FORFEIT = "forfeit"
    DRAW = "draw"
    P1_WIN = "player_one_win"
    P2_WIN = "player_two_win"

    ROCK = "R"
    SCISSORS = "S"
    PAPER = "P"

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_move_history = []
        self.player_two_move_history = []

    def _run_player_code(
            self,
            turn_idx,
            player,
            player_move_history,
            opponent_move_history
    ):
        try:
            with context_manager_time_limit():
                move = player.rps(
                    player.get_nickname(),
                    turn_idx,
                    player_move_history,
                    opponent_move_history
                )

        except TimeoutException:
            move = self.FORFEIT

        return move

    def _find_winner(self, move_one, move_two):
        if move_one == move_two:
            return self.DRAW
        elif move_one == self.ROCK and move_two == self.SCISSORS:
            return self.P1_WIN
        elif move_one == self.ROCK and move_two == self.PAPER:
            return self.P2_WIN
        elif move_one == self.PAPER and move_two == self.ROCK:
            return self.P1_WIN
        elif move_one == self.PAPER and move_two == self.SCISSORS:
            return self.P2_WIN
        elif move_one == self.SCISSORS and move_two == self.PAPER:
            return self.P1_WIN
        elif move_one == self.SCISSORS and move_two == self.ROCK:
            return self.P2_WIN
        else:
            raise Exception("Unrecognized moves found!")

    def play_single_round(self, turn_idx):

        player_one_move = self._run_player_code(
            turn_idx,
            self.player_one,
            self.player_one_move_history,
            self.player_two_move_history
        )

        player_two_move = self._run_player_code(
            turn_idx,
            self.player_two,
            self.player_two_move_history,
            self.player_one_move_history
        )

        self.player_one_move_history.append(player_one_move)
        self.player_two_move_history.append(player_two_move)

        if player_one_move == self.FORFEIT and player_two_move == self.FORFEIT:
            return player_one_move, player_two_move, self.DRAW
        elif player_one_move == self.FORFEIT:
            return player_one_move, player_two_move, self.P2_WIN
        elif player_two_move == self.FORFEIT:
            return player_one_move, player_two_move, self.P1_WIN
        else:
            return player_one_move, player_two_move, self._find_winner(player_one_move, player_two_move)
