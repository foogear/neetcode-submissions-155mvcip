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

            target = None

            if control == "duplicate":
                #print('duplicate')
                target = s2[R]
            elif control == "rmOne":
                #print('rmOne')
                R = L + 1

    
            #print(f"---------L[{L}]={s2[L]}")
            #print(f"---------R[{R}]={s2[R]}")



            while L < R:
                L += 1
                #print(f'---------L=[{L}]={s2[L]}')
                #print(f'---------R=[{R}]={s2[R]}')
                #print(f'---------{currSymbolMap}')
                #print(f'---------{currTotalSymbol}')

                if s2[L] in currSymbolMap:
                    currSymbolMap[s2[L]] -= 1
                    currTotalSymbol[0] -= 1

                if (target in currSymbolMap
                    and currSymbolMap[target] <= symbolMap[target]):
                    break




            #print(f"return L={L}")
            return L


        L, R = -1, -1
        while R < s2Len - 1:
            R += 1
            #print("+++++++++++++++++++++++++")
            #print(f'L=[{L}]={s2[L]}')
            #print(f'R=[{R}]={s2[R]}')
            #print(currSymbolMap)
            #print(currTotalSymbol)

            if R - L > s1Len:
                #print('rmOne')
                L = removeLeft(L, R, "rmOne")

            if s2[R] in currSymbolMap:
                currSymbolMap[s2[R]] += 1
                currTotalSymbol[0] += 1
                if currSymbolMap[s2[R]] > symbolMap[s2[R]]:
                    #print('duplicate')
                    L = removeLeft(L, R, "duplicate")

        


            if currTotalSymbol[0] == totalSymbol:
                #print(currTotalSymbol)
                #print(totalSymbol)
                return True

        return False







            

        



