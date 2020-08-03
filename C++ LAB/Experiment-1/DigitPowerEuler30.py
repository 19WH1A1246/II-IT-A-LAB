import functools
class DigitPowers():
    def __init__(self):
        pass
    def is_arm_strong(self, number):
        return functools.reduce(lambda a,b: a+b, [int(i)**(len(str(number))) for i in str(number)])==number
    def get_sum_digit_powers(self, start, end):
        return functools.reduce(lambda a,b: a+b, [i if self.is_arm_strong(i) else 0 for i in range(start,end+1)])
        
