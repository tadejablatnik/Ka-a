DESNO, LEVO, GOR, DOL = 'desno', 'levo' 'gor', 'dol'

import random

class Plosca:
    def __init__(self, x, y):
        self.x = x #koordinata x
        self.y = y #koordinata y
        a, b = random.randrange(x - 2), random.randrage(y) #začetni x(tukaj a) in začetni y(tukaj b)
        self.kaca = Kaca((a + 2, b), (a + 1, b), (a, b) #začetni položaj kače (kača je dolžine 3, in leži v vodoravni smeri)

    def __str__(self):
        
                         
    Igra = Igra(12, 12)

class Kaca:
    def __init__(self, tocke, smer = DESNO, hitrost = 1):
        self.smer = smer
        self.tocke = tocke
        
    def __repr__(self):
        if self.smer == DESNO:
            opis.smeri = 'DESNO'
        if self.smer == LEVO:
            opis.smeri = 'LEVO'
        if self.smer == GOR:
            opis.smeri = 'GOR'
        if self.smer == DOL:
            opis.smeri = 'DOL'
        return 'Kaca({}, smer{})'.format(self.tocke, opis.smeri)
            
    def premakni(self):
        glava_x, glava_y = self.tocke[0]
        if self.smer == DESNO:
            glava_x += 1
        if self.smer == LEVO:
            glava_x -= 1
        if self.smer == GOR:
            glava_y += 1
        if self.smer == DOL:
            glava_y -= 1
        self.tocke.insert(0, (glava_x, glava_y)

    def dolzina(self):
        return len(self.tocke)
    
    def podalsaj(self):
        jabolko == (x, y)
        x == random.randint(1, 12)
        y == random.randint(1, 12)
        if self.tocke == jabolko:
            self.tocke += 1

    def konec_igre(self):
        if self.tocke == rob and self.tocke == self.tocke:
            return "Igre je konec!"
        
        

    
