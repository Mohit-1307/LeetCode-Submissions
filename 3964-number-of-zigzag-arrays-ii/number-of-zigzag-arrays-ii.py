class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        sz = 2 * m

        def mat_mul(A, B):
            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0:
                        continue
                    aik = A[i][k]

                    for j in range(sz):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def mat_vec_mul(A, v):
            res = [0] * sz

            for i in range(sz):
                s = 0
                row = A[i]

                for j in range(sz):
                    if row[j]:
                        s += row[j] * v[j]

                res[i] = s % MOD

            return res

        # transition matrix
        T = [[0] * sz for _ in range(sz)]

        # up'[i] = sum_{j < i} down[j]
        for i in range(m):
            for j in range(i):
                T[i][m + j] = 1

        # down'[i] = sum_{j > i} up[j]
        for i in range(m):
            for j in range(i + 1, m):
                T[m + i][j] = 1

        # length = 2 base vector
        V = [0] * sz

        for i in range(m):
            V[i] = i            # up
            V[m + i] = m - 1 - i  # down

        power = n - 2

        while power:
            if power & 1:
                V = mat_vec_mul(T, V)

            T = mat_mul(T, T)
            power >>= 1

        return sum(V) % MOD