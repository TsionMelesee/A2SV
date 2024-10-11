class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.a = 0
        self.b = 0
        self.c = 0
        self.dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.total = width * 2 + (height - 2) * 2

    def step(self, num: int) -> None:
        while num > 0:
            if self.a == 0:
                remain = self.width - 1 - self.b
            elif self.a == 1:
                remain = self.height - 1 - self.c
            elif self.a == 2:
                remain = self.b
            else:
                remain = self.c

            if remain >= num:
                self.b += self.dir[self.a][0] * num
                self.c += self.dir[self.a][1] * num
                num = 0
            else:
                self.b += self.dir[self.a][0] * remain
                self.c += self.dir[self.a][1] * remain
                self.a = (self.a + 1) % 4
                num -= remain
                num %= self.total
                if num == 0 and self.corner(self.b, self.c):
                    self.a = (self.a - 1 + 4) % 4

    def corner(self, b: int, c: int) -> bool:
        return (b == 0 and c == 0) or (b == 0 and c == self.height - 1) or (b == self.width - 1 and c == 0) or (b == self.width - 1 and c == self.height - 1)

    def getPos(self) -> list[int]:
        return [self.b, self.c]

    def getDir(self) -> str:
        directions = ["East", "North", "West", "South"]
        return directions[self.a]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
