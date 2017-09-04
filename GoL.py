import cv2
import numpy as np


class Board:
    """docstring for Board"""
    def __init__(self, *arg, **kwargs):
        self.row = kwargs['rows']
        self.column = kwargs['columns']
        self.cell_size = kwargs['cell_size']
        self.alive_cells = {}

    def initiate(self, *coordinates):
        for c in coordinates
            cell = Cell(coordinate=c, state=True)
            self.resurrection(cell)

    def resurrection(self, cell):
        self.alive_cells.add(cell)

    def killing(self, cell):


    def show():
        arr = np.zeros((1000, 1000),dtype=np.uint8)
        y = np.arange(400, 450)
        x = np.arange(500, 550)
        inds = np.meshgrid(x, y, sparse=False, indexing='xy')
        arr = np.zeros((1000, 1000),dtype=np.uint8)
        cv2.imwrite('test.png', arr)
        arr[inds] = 255

    def neighbors(self, cell):
        x, y = cell.coordinate
        inc_x = min(x+1, self.row)
        inc_y = min(y+1, self.column)
        dec_x = max(x-1, 0)
        dec_y = max(x-1, 0)
        return {(inc_x, inc_y),
                (inc_x, y),
                (inc_x, dec_y),
                (dec_x, inc_y),
                (dec_x, y),
                (dec_x, dec_y),
                (x, inc_y),
                (x, dec_y)
                }
class Cell:
    def __init__(self, *args, **kwargs):
        self.coordinate = kwargs['coordinate']
        self.state = kwargs['state']

    def __setitem__(self, value):
        self.state = value

    def __eq__(self, cell):
        return cell.coordinate == self.coordinate

    def __hash__(self):
        return hash(self.coordinate)


class GameOfLife:
    def __init__(self, *args, **kwargs):
        pass

    def __iter__(self):
        return next()
        """
           C   N                 new C
           1   0,1             ->  0  # Lonely
           1   4,5,6,7,8       ->  0  # Overcrowded
           1   2,3             ->  1  # Lives
           0   3               ->  1  # It takes three to give birth!
           0   0,1,2,4,5,6,7,8 ->  0  # Barren
        """
    