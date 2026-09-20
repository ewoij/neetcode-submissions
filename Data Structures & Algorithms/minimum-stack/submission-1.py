class MinStack:

    def __init__(self):
        self._s = []

    def push(self, val: int) -> None:
        self._s.append((
            val, 
            min(val, self._s[-1][1]) if self._s else val
        ))

    def pop(self) -> None:
        return self._s.pop()[0]

    def top(self) -> int:
        return self._s[-1][0]

    def getMin(self) -> int:
        return self._s[-1][1]
        
