class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp_anagram = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in grp_anagram:
                grp_anagram.get(sorted_word).append(word)
            else:
                grp_anagram[sorted_word] = [word]

        return [word for word in grp_anagram.values()]
        
        