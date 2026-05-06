class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter_list=[]
        
        for i in str(s):
            ascii_val=ord(i)
            if 48<=ascii_val<=57 or 65<=ascii_val<=90 or 97<=ascii_val<=122:
                letter_list.append(i.lower())
        total_length=len(letter_list)
        middle=int(total_length/2)
        if total_length==0:
            return True

        for i in range(middle+1):
            if letter_list[i]!=letter_list[total_length-1-i]:
                return False
        return True 
            
        