import sys
import os
import asyncio
import subprocess
import shlex
import math

import chess
import chess.engine
import chess.pgn

SF_CALL = '/home/jamestaylor/stockfish/stockfish_20090216_x64_bmi2'
M = 290.680623072
L = 1.548090806
LIM = 0.25

async def main() -> None:
    transport, sf = await chess.engine.popen_uci(SF_CALL)

    with open('/home/jamestaylor/Documents/Carlsen-Taylor.pgn') as f:
        game = chess.pgn.read_game(f)

    board = chess.Board()
    with open('evals.txt', 'w') as f:
        cp = 0
        for move in game.mainline_moves():
            res = await sf.analyse(
                board,
                chess.engine.Limit(nodes=10000),
                info=0b110,
            )
            for key, val in res.items():
                if key == 'score':
                    new_cp = int(
                        str(val.white()).translate(str.maketrans('', '', '+'))
                    )
                    # f.write(f"{key}: {cp}\n")
                    if abs(
                        (math.atan(new_cp / M) / L)
                        - (math.atan(cp / M) / L)
                    ) > LIM:
                        for k,v in last_res.items():
                            f.write(f"{k}: {v}\n")
                        f.write(last_fen)
            cp = new_cp
            last_fen = board.fen()+"\n"+str(move)+"\n"
            last_res = res
            board.push(move)

if __name__ == "__main__":
    asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
    asyncio.run(main(), debug=True)
