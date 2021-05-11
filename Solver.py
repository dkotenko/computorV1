from const import EPSILON

class Solver():

    def ft_abs(n):
        if n < 0: n *= -1
        return n


    def squareRoot(n) :
        x = n
        count = 0 
    
        while (1) :
            count += 1 
            root = 0.5 * (x + (n / x)) 
            if (self.ft_abs(root - x) < EPSILON) :
                break
            x = root
        return root