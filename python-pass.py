class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        
        output = ""

        if len(s) == 1:
            print(s)
        else:
            
            for x in range(1, len(s)):
                if s == s[::-1]:                                    #check if s == reverse of s
                    if len(s) > len(output):
                        output = s
                    break
                else:
                    for i in range(1, len(s)):
                        subString = s[i:]                           #delete the first left char from s
                        if subString == subString[::-1]:            #check if subString == reverse of subString
                            if len(subString) > len(output):
                                output = subString
                            break
                
                s = s[:-x]                                          #delete the last char from s

        print(output)
        

Solution.longest_palindromic(s="htaaaacssss")                      # output = sssss
