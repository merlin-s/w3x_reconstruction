from shared import Color


class Region:
    def __init__(self,
                 name: str,
                 minx: float,
                 miny: float,
                 maxx: float,
                 maxy: float,
                 color: Color
                 ):
        self.name = name
        self.left = minx
        self.right = maxx
        self.bottom = miny
        self.top = maxy
        self.color = color