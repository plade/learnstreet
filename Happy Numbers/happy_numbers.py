#Happy Numbers Project
def happynum(num):
    '''Happy number is defined by following process:'''
    '''1) Starting with any positive integer, replace the number by the sum of the squares of its digits, and'''
    '''2) Repeat the process until the number equals 1 (where it will stay).'''
    '''If not, it loops endlessly in a cycle which does not include 1 (unhappy number!).'''
    if num == 1:
        return "Happy Number"
    been_here = []
    while (num != 1):
        num = sum(int(i)**2 for i in str(num))
        if num in been_here:
            return "Unhappy Number"
        else:
            been_here.append(num)
    return "Happy Number"
        