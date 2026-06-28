class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count to the list of anagrams
                                # use defaultdict to avoid edge case where count == None

        for s in strs:
            count = [0] * 26 # a, b, ..., z

            for c in s:
                count[ord(c) - ord('a')] += 1 
                # subtract the ASCII value of 'a' from the ASCII value of the current letter to map it to a value from 0-25
                # then increment this value by one to count that character

            res[tuple(count)].append(s)
            # if a string has the same character count (it is an anagram) append it to the dictionary/hashmap
            # convert count from a tuple to a list so that it is a valid key in a Python dict (must be immutable)

        return list(res.values()) # return only the values of the hashmap without the keys




        