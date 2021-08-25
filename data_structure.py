class Data():
    def __init__(self, Y, H, std):
        self.Y = Y
        self.H = H
        self.std = std
        self.batch_ind = 0
    
    def getY(self):
        return self.Y
    
    def getH(self):
        return self.H
    
    def getStdDev(self):
        return self.std
    
    def completed(self):
        return self.batch_ind == self.Y.size
    
    #returns R and not s
    def getNextBatch(self):
        self.batch_ind += 1
        return self.H[self.batch_ind - 1].reshape(1,3), self.Y[self.batch_ind - 1][0], self.std[self.batch_ind - 1]**2    
    
    def reset(self):
        self.batch_ind = 0