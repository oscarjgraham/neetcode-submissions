class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort with the index and values swapped to count the frequency of each number

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # bounded by the length of the list

        for n in nums:
            count[n] = 1 + count.get(n, 0) # count the frequency of each number with a hashmap
        
        for n, c in count.items(): # for every key value pair in the frequency hashmap
            freq[c].append(n)      # append the number to the list in freq with an index corresponding to than number's frequency
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # loop through the list backwards
            for n in freq[i]: # look at each number that occurs at a specific frequency
                res.append(n) # append the highest frequency numbers to the results list until it contains k elements
                if len(res) == k:
                    return res
        
        

        