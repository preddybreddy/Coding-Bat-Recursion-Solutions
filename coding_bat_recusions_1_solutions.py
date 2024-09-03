def factorial_(n):
    if n == 0:
        return 1
    
    return n * factorial_(n - 1)




def bunnyEars(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 2
    
    return bunnyEars(n - 1) + 2



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 2) + fibonacci(n - 1)



def bunnyEars2(bunnies):
    if bunnies == 1:
        return 2
    
    if bunnies == 2:
        return 5
    
    return bunnyEars2(bunnies - 2) + 2 + 3

def triangle(rows):
    if rows == 0:
        return 0
    
    if rows == 1:
        return 1
    
    return triangle(rows - 1) + rows

def sumDigits(n):
    if n//10 == 0:
        return n
    
    return (n%10) + sumDigits(n//10)

def count7(n):
    if n == 0:
        return 0
    
    if n == 7:
        return 1
    
    return (1 if n%10 == 7 else 0) + count7(n//10)

def count8(n):
    if n == 0:
        return 0
    
    if n == 8:
        return 1

    last_char = n%10
    sub_ans = count8(n//10)
    if last_char == 8:
        if (n//10) % 10 == 8:
            return sub_ans + 2
        else:
            return sub_ans + 1
    return sub_ans

def powerN(base, n):
    if n == 0:
        return 1
    return powerN(base, n-1) * base

def countX(str):
    if len(str) == 0:
        return 0
    
    return countX(str[1:]) + (1 if str[0] == 'x' else 0)

def countHi(str):
    if len(str) < 2:
        return 0

    if str[:2] == 'hi':
        return 1 + countHi(str[2:])

    return countHi(str[1:])

def changeXY(str):
    if str == 'x':
        return 'y'
    
    return ('y' if str[0] == 'x' else str[0]) + changeXY(str[1:])

def changePi(str):
    if len(str) < 2:
        return str
    
    if str == 'pi':
        return '3.14'
    
    if str[:2] == 'pi':
        return '3.14' + changePi(str[2:])

    return str[0] + changePi(str[1:])

def noX(str):
    if len(str) == 0:
        return ''
    
    if str == 'x':
        return ''
    
    return ('' if str[0] == 'x' else str[0]) + noX(str[1:]) 


def array6(nums, index):
    if index >= len(nums):
        return False
    
    return array6(nums, index + 1) or (True if nums[index] == 6 else False)
    
def array11(nums, index):
    if index >= len(nums):
        return 0
    
    return array11(nums, index + 1) + (1 if nums[index] == 11 else 0)

def array220(nums, index):
    if index > len(nums)-2:
        return False
    
    return array220(nums, index + 1) or (nums[index + 1] == nums[index]*10)

def allStar(str):
    if len(str) < 2:
        return str
    
    if len(str) == 2: 
        return str[0] + '*' + str[1]
    
    return str[0] + '*' + str[1] + '*' + allStar(str[2:])


def pairStar(str):
    if len(str) < 2:
        return str
    
    if str[0] == str[1]:
        return (str[0] + '*') + pairStar(str[1:])
    
    return str[0] + pairStar(str[1:])

def endX(str):
    if len(str) == 1:
        return str
    
    if str[0] == 'x':
        return endX(str[1:]) + 'x'
    return str[0] + endX(str[1:])

def countPairs(str):
    if len(str) < 3:
        return 0
    
    if str[0] == str[2]:
        return 1 + countPairs(str[1:])
    
    return countPairs(str[1:])

def countAbc(str):
    if len(str) < 3:
        return 0
    
    if str[:3] in {'abc', 'aba'}:
        return 1 + countAbc(str[1:])
    
    return countAbc(str[1:])

def count11(str):
    if len(str) < 2:
        return 0
    
    if str[:2] == '11':
        return 1 + count11(str[2:])
    
    return count11(str[1:])

def stringClean(str):
    def stringCleanHelper(str, prevChar):
        if len(str) < 2:
            return str
        
        if str[0] == prevChar:
            return stringCleanHelper(str[1:], prevChar)

        if (str[0] == str[1]):
            return str[0] + stringCleanHelper(str[2:], str[1])
        
        return str[0] + stringCleanHelper(str[1:], prevChar)

    return stringCleanHelper(str, '')

def countHi2(str):
    if len(str) < 2:
        return 0
    
    if str[0] == 'x':
        start_index = 3 if len(str) > 2 else len(str)
        return countHi2(str[start_index:])
    
    if str[:2] == 'hi':
        return 1 + countHi2(str[2:])
    return countHi2(str[1:])

def parenBit(str):
    if str[0] == '(' and str[-1] == ')':
        return str
    
    if str[0] != '(':
        return parenBit(str[1:])
    
    if str[-1] != ')':
        return parenBit(str[:-1])
    
    return ""

def nestParen(str):
    if len(str) == 0:
        return True
    
    if len(str) % 2 != 0:
        return False
    
    return str[0] == '(' and str[-1] == ')' and nestParen(str[1:-1])

def strCount(str, sub):
    if len(str) < len(sub):
        return 0
    
    if str == sub:
        return 1
    
    if str[:len(sub)] == sub:
        return 1 + strCount(str[len(sub):], sub)
    
    return strCount(str[len(sub):], sub)
    
def strCopies(str, sub, n):
    if (len(str) < len(sub)) and n != 0:
        return False
    
    if n == 0:
        return True
    
    if str[:len(sub)] == sub:
        return strCopies(str[len(sub):], sub, n-1)
    
    return strCopies(str[1:], sub, n)

def strDist(str, sub):
    if len(str) < len(sub):
        return 0
    
    if str[:len(sub)] == sub and str[(-1*len(sub)):] == sub:
        return len(str)
    
    if str[:len(sub)] != sub:
        return strDist(str[1:], sub)
    
    if str[(-1*len(sub)):] != sub:
        return strDist(str[:-1], sub)

    return 0

print(strDist("cccatcowcatxx", "cat"))

