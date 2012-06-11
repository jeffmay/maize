
##################
# Helper Methods #
##################

def location(point):
    try:
        x, y = point
        return x, y
    except ValueError:
        raise ValueError("'%s' is not a valid (x, y) tuple" % point)

##############
# Maze Skins #
##############

class Skin(object):

    @classmethod
    def __getitem__(cls, item):
        """Retrieve a skin element using a string lookup"""
        return getattr(cls, item)

##############
# Maze Logic #
##############

class DottedArenaSkin(Skin):
    OPEN = ' '
    WALL = 'X'
    BORDER_TOP_LEFT = '::'
    BORDER_TOP = ':'
    BORDER_TOP_RIGHT = '::'
    BORDER_LEFT = '::'
    BORDER_RIGHT = '::'
    BORDER_BOTTOM_LEFT = '::'
    BORDER_BOTTOM = ':'
    BORDER_BOTTOM_RIGHT = '::'

class Maze(object):
    NORTH = ( 0, -1)
    SOUTH = ( 0,  1)
    EAST  = ( 1,  0)
    WEST  = (-1,  0)
    DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

    INNER_TEMPLATE = '''{right_border_cell}\n{left_border_cell}'''
    BORDER_TEMPLATE = '''\
{top_left_border}{top_border}{top_right_border}
{left_border_cell}{inside}{right_border_cell}
{bottom_left_border}{bottom_border}{bottom_right_border}
'''

    def __init__(self, rows, cols, fill='WALL', start=(1,0), skin=DottedArenaSkin()):
        self._board = [[skin[fill]] * cols for row in range(rows)]
        self.rows = rows
        self.cols = cols
        self.area = rows * cols
        self.start = start
        self.skin = skin

    def _contains(self, point):
        x, y = location(point)
        return x >= 0 and y >= 0 and x < self.cols and y < self.rows

    def __getitem__(self, point):
        """Get the char at the given (x, y) point"""
        x, y = location(point)
        if self._contains((x, y)):
            return self._board[y][x]
        else:
            raise LookupError("(%s, %s) is not within the borders of this maze" % (x, y))

    def __setitem__(self, point, char):
        """Set the char at the given (x, y) point"""
        x, y = location(point)
        if self._contains((x, y)):
            self._board[y][x] = char
        else:
            raise LookupError("(%s, %s) is not within the borders of this maze" % (x, y))

    def __str__(self):
        """Render the maze"""
        # join every row with borders
        inner_bordered_rows = Maze.INNER_TEMPLATE.format(
                left_border_cell=self.skin.BORDER_LEFT,
                right_border_cell=self.skin.BORDER_RIGHT
            ).join(''.join(row) for row in self._board)
        # paste the inside between top and bottom borders
        return Maze.BORDER_TEMPLATE.format(
                top_left_border=self.skin.BORDER_TOP_LEFT,
                top_border=self.skin.BORDER_TOP * self.cols,
                top_right_border=self.skin.BORDER_TOP_RIGHT,
                left_border_cell=self.skin.BORDER_LEFT,
                inside=inner_bordered_rows,
                right_border_cell=self.skin.BORDER_RIGHT,
                bottom_left_border=self.skin.BORDER_BOTTOM_LEFT,
                bottom_border=self.skin.BORDER_BOTTOM * self.cols,
                bottom_right_border=self.skin.BORDER_BOTTOM_RIGHT
            )

