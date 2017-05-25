from math import *
from scipy.optimize import leastsq
import numpy as np
import random


class OldDriver:
    def __init__(self, default_speed, default_bias_time):
        # 赤道半径
        self.__ra = 6378140
        # 极半径
        self.__rb = 6356755
        # 扁率
        self.__flatten = (self.__ra - self.__rb) / self.__ra
        # 默认速度
        self.default_speed = default_speed
        # 默认时间偏差
        self.default_bias_time = default_bias_time

    def calculate_distance(self, pt1_latitude, pt1_longitude, pt2_latitude, pt2_longitude):
        rad_pt1_lat = radians(pt1_latitude)
        rad_pt1_lgt = radians(pt1_longitude)
        rad_pt2_lat = radians(pt1_latitude)
        rad_pt2_lgt = radians(pt1_longitude)
        pA = atan(self.__rb / self.__ra * tan(rad_pt1_lat))
        pB = atan(self.__rb / self.__ra * tan(rad_pt2_lat))
        xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_pt1_lgt - rad_pt2_lgt))
        c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
        c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
        dr = self.__flatten / 8 * (c1 - c2)
        distance = self.__ra * (xx + dr)
        return distance

    def predict_remnant_time(self, ins_speed, rem_distance):
        return rem_distance / ins_speed + self.default_bias_time

    def fit_curve(self, pts, curve_term=5):
        latitude_x_list = []
        longitude_y_list = []
        for pt in pts:
            latitude_x_list.append(pt[0])
            longitude_y_list.append(pt[1])
        x_array = np.array(latitude_x_list)
        y_array = np.array(longitude_y_list)

        coefficients = []
        for i in range(curve_term):
            coefficients.append(random.random())
        # 定义曲线函数
        def curve_func(coefficients, x):
            func_str = ''
            for n in range(len(coefficients)):
                power_num = len(coefficients) - n - 1
                if power_num > 0:
                    func_str += str(coefficients[n]) + '*x**' + str(power_num) + ' + '
                else:
                    func_str += str(coefficients[n])
            print(func_str)
            return eval(func_str)
        # 定义误差函数
        def residuals(coefficients, x, y):
            return y - curve_func(coefficients, x)

        plsq = leastsq(residuals, np.array(coefficients), args=(x_array, y_array))
        print(plsq)
        def result_func(x):
            return curve_func(plsq[0].tolist(), x)
        return result_func

    def calculate_remnant_distance(self, c_pt_x, des_pt_x, curve_line_func):
        rem_dis = 0.0
        x1 = 0.0
        x2 = 0.0
        dx = 0.0001
        if c_pt_x < des_pt_x:
            x1 = c_pt_x
            x2 = des_pt_x
        else:
            x1 = des_pt_x
            x2 = c_pt_x
        for x in np.arange(x1, x2, dx):
            dl = (dx ** 2 + (curve_line_func(x+dx) - curve_line_func(x)) ** 2) ** 0.5
            rem_dis += dl
        print('the remnant distance is: ' + str(rem_dis))
        return rem_dis

if __name__ == "__main__":
    pts = [[1, 4], [2, 7], [3, 10], [5, 16], [6, 19], [7, 22], [8, 25]]
    od = OldDriver(2, 10)
    curve_func = od.fit_curve(pts)
    r1 = od.calculate_remnant_distance(1, 2, curve_func)

