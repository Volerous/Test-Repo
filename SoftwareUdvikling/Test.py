class jumper(object):
    def __init__(self,height,distance):
        self.Hgt = height
        self.Dst = distance
        self.jDst = 0
        self.hDst = 0
    def jumpUp(self):
        self.hDst = self.hDst + self.Hgt
        print (self.hDst)
    def jumpDst(self):
        self.jDst = self.jDst + self.Dst
        print(self.jDst)
Player1 = jumper(3,4)
Player1.jumpUp()
Player1.jumpDst()