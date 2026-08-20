class Solution:

    def encode(self, strs: List[str]) -> str:
        encstr = str()
        for word in strs:
            length = str(len(word))
            encstr += length
            encstr += '#'
            encstr += word
        print(encstr)
        return encstr


    def decode(self, s: str) -> List[str]:
        i = 0
        solution = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            solution.append(s[i:i+length])
            i += length
        return solution





