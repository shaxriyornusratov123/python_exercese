class Palindrome:
    def PalindromChecker(s:str)->bool:
        s=s.lower()
        if s==s[::-1]:
            return True
        return False 
    
print(Palindrome.PalindromChecker("Kiyik"))