class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Len, s2Len = len(s1), len(s2)
        if s1Len > s2Len:
            return False

        symbolMap, currSymbolMap = {}, {}
        totalSymbol, currTotalSymbol = 0, [0]
        for s in s1:
            if s not in symbolMap:
                symbolMap[s] = 0
                currSymbolMap[s] = 0
            symbolMap[s] += 1
            totalSymbol += 1


        def removeLeft(L, R, control):

            if control == "duplicate":
                R -= 1
            elif control == "rmOne":
                R = L + 1


            while L < R:
                L += 1
                if s2[L] in currSymbolMap:
                    currSymbolMap[s2[L]] -= 1
                    currTotalSymbol[0] -= 1

            return L


        L, R = -1, -1
        while R < s2Len - 1:
            R += 1

            if R - L > s1Len:
                L = removeLeft(L, R, "rmOne")

            if s2[R] in currSymbolMap:
                currSymbolMap[s2[R]] += 1
                currTotalSymbol[0] += 1
                if currSymbolMap[s2[R]] > symbolMap[s2[R]]:
                    L = removeLeft(R, L, "duplicate")


            if currTotalSymbol[0] == totalSymbol:
                return True

        return False








            

        



