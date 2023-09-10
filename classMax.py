class Check:
    
        def __init__(self,numbers):
            self.numbers = numbers
            
            
            
        def max(self):
            max = numbers[0]
            for number in numbers:
                if number > max:
                    max = number
            return max
    