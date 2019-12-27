# coding: utf-8
"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。　　

　　例如下面的二维数组就是每行、每列都递增排序。如果在这个数组中查找数字7，则返回true；如果查找数字5，由于数组不含有该数字，则返回false。

1 2 8 9
2 4 9 12
4 7 10 13
6 8 11 15
"""
"""
解题思路：
从右上或者左下方开始找，保证的是横的、竖的这两个方向上数值的增大或者减小的趋势是相反的，这样查找的时候就比较好查找。
比如，我们从右上角开始，
如果目标数值比这个数大，那么目标的数一定在该行的下面。
如果目标数值比这个数小，那么目标的数一定会在该行的左边。
这样就会逐步缩小这个矩阵，直至遍历完成。
"""


class Solution(object):
    """
    input: array : [[1,2,3,4], [5,6,7,8]]
    output: true or false
    """

    def __init__(self):
        """init for array and target number"""
        self.array = None
        self.target = None

    def judge_is_exists(self):
        """
        judge if the target number is in given array
        :return:
        """
        if self.array is None or len(self.array) == 0:
            return False
        else:
            rows = 0
            lines = len(self.array[0])
            number = self.array[rows][lines - 1]
            flag = False
            while rows < len(self.array) and lines >= 0:
                if self.target > number:
                    rows = rows + 1
                    number = self.array[rows][lines - 1]
                elif self.target < number:
                    lines = lines - 1
                    number = self.array[rows][lines - 1]
                else:
                    flag = True
                    break
            return flag
