import Media

class Clip(Media.Media):
    
    def __init__(self,  n, d, s, u, dur, cs, sub):
        super().__init__( n, d, s, u, dur, cs)
        self.subject = sub
    
    def showInfo(self):
        super().showInfo()
        print('Subject: ', self.subject)
    
    def edit(self):
        super().edit()
        new_subject = input('Subject = ')
        self.subject = new_subject