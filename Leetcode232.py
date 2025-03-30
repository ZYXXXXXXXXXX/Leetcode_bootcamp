class MyQueue:
    def __init__(self):
        self.arr=[]

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        x=self.arr[0]
        del self.arr[0]
        return x
        
    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr)==0:
            return True
        return False
