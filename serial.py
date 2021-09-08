import Media

class Series(Media.Media):
    
    def __init__(self, n, d, s, u, dur, cs, g,f,q):
        super().__init__( n, d, s, u, dur, cs)
        self.genre = g
        self.fasl = f
        self.qesmat = q
    
    def showInfo(self):
        super().showInfo()
        print('Genre: ', self.genre)
        print('Season: ', self.fasl)
        print('Episode: ', self.qesmat)
        
    def edit(self):
        super().edit()
        new_genre = input('Genre = ')
        new_fasl = input('fasl = ')
        new_qesmat = input('qesmat = ')
        self.genre = new_genre
        self.fasl = new_fasl
        self.qesmat = new_qesmat