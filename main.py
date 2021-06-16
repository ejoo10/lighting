from matrix import *
from draw import *
from display import *
from parse import *
import math
import random

s = new_screen()
c = [ 0, 0, 0 ]
zbuffer = new_buffer()

edges = [[], [], [], []]
triangles = [[], [], [], []]
m = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
cs = [m]
A = [255, 255, 0]
LightPoints = [[100, 100, 0]]
PointColors = [[255, 255, 0]]
Ka = [0.1, 0.1, 0.1]
Kd = [0.5, 0.5, 0.5]
Ks = [0.5, 0.5, 0.5]
x = 1.5


parse('script', edges, triangles, cs, s, c, zbuffer, A, LightPoints, PointColors, Ka, Kd, Ks, x)
