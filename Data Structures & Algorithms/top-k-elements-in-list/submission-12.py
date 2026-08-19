class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        solution = []

        # Create hashmap
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        for num, counts in hashmap.items():
            freq[counts].append(num)
            

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution
