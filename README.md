# chess_analysis

## UCI Protocol

UCI (Universal Chess Interface) protocol is a standard for communicating with chess engines, including both of the top open source engines in the world, Lc0 and Stockfish.

### Common Commands

Upon loading an engine, the first command to be issued should always be `isready`, after which the engine will respond `readyok` when it is ready to receive further commands. Following that, the most common next command is `ucinewgame` to indicate to the engine that a new set of analyses will be conducted.

At this point, analysis can begin and may take different paths. To set the start position, `position startpos` sets up the board with the starting position. Alternatively, a position FEN code can be input in place of startpos, if analysis is to pick up from a given position.

Instead of simply setting the pieces up in the starting position, I more often start analysis from a game position by providing moves from the start position in UCI format, providing a space-separated list of the algebraic notation of the square the piece was on and to which it moved -- eg. `position startpos moves d2d4 g8f6 c2c4 e7e6 b1c3 f8b4` (the first 3 moves (6 ply) of the dynamically balanced Nimzo-Indian Defense, which I have played with both colors at times).

Once the desired position is set-up, then we instruct the engine to start analyzing as we simultaneously provide it conditions on which to stop analysis. I commonly instruct it to `go infinite`, after which it will analyze the position indefinitely, going progressively deeper in its analysis until I tell it to stop with the command `stop`. Other options include analysis for a certain amount of time, depth, or nodes reached in the search.
