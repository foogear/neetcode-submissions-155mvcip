class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # it's not a permutations problem
        perm = {}
        for p in s1:
            perm[p] = 0

        def moveLeft(L, R):
            while L < R:
                L += 1
                if s2[L] not in perm:
                    continue
                perm[s2[L]] -= 1

                if s2[R] not in perm:
                    continue
                if perm[s2[R]] == 1:
                    break

            return L

        L, R, s1Len = 0, 0, len(s1)
        for R in range(len(s2)):
            if s2[R] not in perm:
                # L = R Wrong 
                L = moveLeft(L, R)
                continue

            perm[s2[R]] += 1 # 1️⃣
            # if perm[s2[R]]: Wrong 1️⃣
            if perm[s2[R]] > 1:
                L = moveLeft(L, R)
            # else:
                # perm[s2[R]] += 1 1️⃣
            
            # if R - L < 3:
            if R - L < s1Len:
                continue 
            else:
                return True

        return False

        