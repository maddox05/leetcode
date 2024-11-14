def subtract(num):
    
    if(num>=900):
        return 900
    elif (num>=400):
        return 400
    elif(num>=90):
        return 90
    elif(num>=40):
        return 40
    elif(num>=9):
        return 9
    elif(num>=4):
        return 4
    


def find_max(num):
    if(num>=1000):
        return 1000
    elif(num >=500):
        return 500
    elif(num>=100):
        return 100
    elif(num>=50):
        return 50
    elif(num>=10):
        return 10
    elif(num>=5):
        return 5
    elif(num>=1):
        return 1

def roman_numeral(num):
    int_to = {
    1: 'I',
   4: 'IV',
    5: 'V',
   9: 'IX',
    10: 'X',
   40: 'XL',
    50: 'L',
   90: 'XC',
    100: 'C',
   400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
    }
    roman = ''
    while num != 0:
        if(str(num)[0] != "4" and str(num)[0] != "9"):
            to_remove = find_max(num)
            num-=to_remove

            roman+=int_to.get(to_remove)
        else:
            to_remove=subtract(num)
            num-=to_remove

            roman+=int_to.get(to_remove)
    return roman


class Solution:
    def intToRoman(self, num: int) -> str:
      return roman_numeral(num)  
