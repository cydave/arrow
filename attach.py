import argparse
import time
import pynvim
from pynvim import attach


class ArrowGuy:

    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
    MOVES = {
        UP: (-1, 0),
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
    }

    def __init__(self, nvim):
        self.nvim = nvim

    def get_pos(self):
        return self.nvim.current.window.cursor

    def get_char(self):
        _, column = self.get_pos()
        return self.nvim.current.line[column]

    def move_cursor(self, direction):
        line, col = self.get_pos()
        l, c = direction
        line += l
        col += c
        self.nvim.current.window.cursor = [line, col]

    def read_direction(self):
        c = self.get_char()
        return self.MOVES[c]

    def move(self):
        while True:
            try:
                direction = self.read_direction()
                self.move_cursor(direction)
                time.sleep(0.3)
            except KeyError:
                continue
            except (
                pynvim.api.common.NvimError,
                IndexError,
                EOFError,
                KeyboardInterrupt,
            ):
                break


def main(args):
    nvim = attach("socket", path=args.socket)
    fd = ArrowGuy(nvim)
    fd.move()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--socket", required=True, help="Path to nvim socket")
    args = ap.parse_args()
    exit(main(args))
