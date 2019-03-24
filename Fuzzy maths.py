import scipy as sp
import numpy as np


class fuzzy:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def alpha_left(self, alpha):
        return (1-alpha)*self.left

    def alpha_right(self,alpha):
        return (1-alpha)*self.right

