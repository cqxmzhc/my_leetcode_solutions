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

    def dpPush(self):
        f = {}
        g = {}
        f[0] = 0
        g[0] = []
        w = 8
        for i in range(0, 16):
            if i + 1 <= w:
                if i + 1 not in f or f[i] + 1 < f[i+1]:
                    f[i+1] = f[i] + 1
                    tmp = [1]
                    tmp.extend(g[i])
                    g[i+1] = tmp

            if i + 5 <= w:
                if i + 5 not in f or f[i] + 1 < f[i+5]:
                    f[i+5] = f[i] + 1
                    tmp = [5]
                    tmp.extend(g[i])
                    g[i+5] = tmp

            if i + 11 <= w:
                if i + 11 not in f or f[i] + 1 < f[i+11]:
                    f[i+11] = f[i] + 1
                    tmp = [11]
                    tmp.extend(g[i])
                    g[i+11] = tmp

        print(f[w], g[w])


if __name__ == "__main__":
    s = Solution()
    s.dpPush()
