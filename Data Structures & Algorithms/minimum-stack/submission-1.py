class MinStack:
    min_value = 0
    stack = []

    def __init__(self):
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        encoded_val = float(val)
        if float(val) < self.min_value:
            encoded_val = (2*float(val)) - self.min_value
            self.min_value = val
            
        self.stack.append(encoded_val)
        

    def pop(self) -> None:
        if self.stack[-1] < self.min_value : 
            self.min_value = (2*float(self.min_value)) - self.stack[-1]
        self.stack.pop()


    def top(self) -> int:
        if self.stack[-1] < self.min_value :
            return int(self.min_value)
        return int(self.stack[-1])

    def getMin(self) -> int:
        return int(self.min_value)
        
