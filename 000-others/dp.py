class Solution(object):
    """
    1, 5, 11
    """

    def dp(self):
        f = {}
        g = {}
        f[0] = 0
        g[0] = []
        for i in range(1, 16):
            cost = float("+inf")
            if i - 1 >= 0:
                if f[i - 1] < cost:
                    cost = f[i - 1] + 1
                    tmp = [1]
                    tmp.extend(g[i - 1])
                    g[i] = tmp
            if i - 5 >= 0:
                if f[i - 5] < cost:
                    cost = f[i - 5] + 1
                    tmp = [5]
                    tmp.extend(g[i - 5])
                    g[i] = tmp
            if i - 11 >= 0:
                if f[i - 11] < cost:
                    cost = f[i - 11] + 1
                    tmp = [11]
                    tmp.extend(g[i - 11])
                    g[i] = tmp

            f[i] = cost
        print(f[14], g[14])


if __name__ == "__main__":
    s = Solution()
    s.dp()
