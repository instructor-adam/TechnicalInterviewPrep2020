class Solution:
    tab_dict = {}
    memo_dict = {}

    def fib(self, N: int) -> int:
        # return self.fib_rec(N)
        # return self.fib_memo(N)
        # return self.fib_tab(N)
        return self.fib_itr(N)

    def fib_rec(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib_rec(N-1) + self.fib_rec(N-2)

    def fib_itr(self, N: int) -> int:
        if N == 0:
            return 0
        f1 = 0
        f2 = 1
        num = 1
        while num < N:
            temp = f1 + f2
            f1 = f2
            f2 = temp
            num += 1
        return f2

    def fib_memo(self, N: int) -> int:
        if N in self.memo_dict:
            return self.memo_dict[N]
        if N == 0:
            return 0
        if N == 1:
            return 1
        self.memo_dict[N] = self.fib_memo(N-1) + self.fib_memo(N-2)
        return self.memo_dict[N]

    def fib_tab(self, N: int) -> int:
        self.tab_dict[0] = 0
        self.tab_dict[1] = 1
        i = 2
        while i <= N:
            self.tab_dict[i] = self.tab_dict[i-1] + self.tab_dict[i-2]
            i += 1
        return self.tab_dict[N]

