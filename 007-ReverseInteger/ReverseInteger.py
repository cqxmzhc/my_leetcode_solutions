#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        sign = False
        if x < 0:
            x *= -1
            sign = True

        x = str(x)
        len_x = len(x)
        reversed_x = ""

        for i in range(len_x-1, -1, -1):
            j = x[i]
            reversed_x += x[i]

        reversed_x = int(reversed_x)
        if sign:
            reversed_x = -1 * reversed_x

        bound = 2 ** 31
        if reversed_x > bound or reversed_x < -1*bound:
            return 0

        return reversed_x


def main():
    s = Solution()
    print(s.reverse())


if __name__ == '__main__':
    main()
