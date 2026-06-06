class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = "/#*#/"
        encStrs = ""
        for s in strs:
            encStrs += s + separator

        return encStrs

    def decode(self, s: str) -> List[str]:
        separator = "/#*#/"
        I = 0
        decList, t = [], ""
        while I < len(s):
            if (s[I + 0] == separator[0]
            and s[I + 1] == separator[1]
            and s[I + 2] == separator[2]
            and s[I + 3] == separator[3]
            and s[I + 4] == separator[4]):
                decList.append(t)
                t = ""
                I += 5
                continue

            t += s[I]
            I += 1

        return decList

