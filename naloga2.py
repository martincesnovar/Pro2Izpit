class Izdelek:
    def __init__(self,ime,cena):
        self.ime=ime
        self.cena=cena
    def __str__(self):
        return '{0} stane {1} EUR'.format(self.ime,self.cena)
    def __repr__(self):
        return '{0} stane {1} EUR'.format(self.ime,self.cena)
    def __add__(self,other):
        skupna_cena = self.cena + other.cena
        return '{0} in {1} stane {2} EUR'.format(self.ime,other.ime,skupna_cena)

def najcenejši(sez,ime):
    naj = None
    for el in sez:
        if el.ime == ime:
            if naj == None:
                naj=el
            else:
                if el.cena < naj.cena:
                    naj=el
    
    return naj

