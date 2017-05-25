from math import *


class OldDriver:
    def __init__(self):
        # 赤道半径
        self.ra = 6378140
        # 极半径
        self.rb = 6356755
        # 扁率
        self.flatten = (self.ra - self.rb) / self.ra

    def calculate_distance(self, pt1_latitude, pt1_longitude, pt2_latitude, pt2_longitude):
        rad_pt1_lat = radians(pt1_latitude)
        rad_pt1_lgt = radians(pt1_longitude)
        rad_pt2_lat = radians(pt1_latitude)
        rad_pt2_lgt = radians(pt1_longitude)
        pA = atan(self.rb / self.ra * tan(rad_pt1_lat))
        pB = atan(self.rb / self.ra * tan(rad_pt2_lat))
        xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_pt1_lgt - rad_pt2_lgt))
        c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
        c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
        dr = self.flatten / 8 * (c1 - c2)
        distance = self.ra * (xx + dr)
        return distance
    