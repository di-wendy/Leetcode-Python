class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for letter in ransomNote:
            if letter in magazine:
                if len(magazine) > 1:
                    magazine = magazine.replace(letter,"",1)
                else:
                    magazine = ""
            else:
                return False
        
        return True
        
