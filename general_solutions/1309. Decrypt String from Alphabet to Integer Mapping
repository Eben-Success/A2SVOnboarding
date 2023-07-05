class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        a_i = {"1" : "a", 
              "2" : "b", 
              "3" : "c",
              "4" : "d",
              "5" : "e",
              "6" : "f",
              "7" : "g",
              "8" : "h",
              "9" : "i"
              }
        
        j_z = {"10" : "j",
              "11" : "k",
              "12" : "l",
              "13" : "m",
              "14" : "n",
              "15" : "o",
              "16" : "p",
              "17" : "q",
              "18" : "r",
              "19" : "s",
              "20" : "t",
              "21" : "u",
              "22" : "v",
              "23" : "w",
              "24" : "x",
              "25" : "y",
              "26" : "z"
              }
        
        
        i = len(s) - 1
        res = []
        
        while i >= 0:
            if s[i] == "#":
                cur = concat(s[i-2], s[i-1])
                res.append(j_z[cur])
                i -= 3
                
            else:
                cur = s[i]
                res.append(a_i[cur])
                i -= 1
                
        return "".join(res[::-1])
