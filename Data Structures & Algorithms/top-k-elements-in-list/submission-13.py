class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        solution = []

        # Create hashmap
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
            
        for key, value in hashmap.items():
            result.append((value, key))
            

        sort_result = sorted(result, reverse=True)

        for i in range(k):
            solution.append(sort_result[i][1])

        return solution
