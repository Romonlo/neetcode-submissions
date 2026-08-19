class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Check each word and create a hash map for it
        if len(strs) == 1:
            return [[strs[0]]]
        
        solution = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 #We need to compare the position with 'a', which is the 0 index of our count array
            solution[tuple(count)].append(s)
        return list(solution.values())





        