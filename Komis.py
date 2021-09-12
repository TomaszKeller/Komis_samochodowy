from osobowe import *
from motocykl import *
from ciezarowe import *


class Komis:

    def __init__(self):
        self.osobowe = []
        self.ciezarowe = []
        self.motocykle = []
        self.budzet = [100000]

    def kup(self, typ, obj):
        if obj.typ == 'osobowe':
            self.osobowe.append(obj)
            return self.osobowe
        elif obj.typ == 'ciezarowe':
            self.ciezarowe.append(obj)
            return self.ciezarowe
        elif obj.typ == 'motocykle':
            self.motocykle.append(obj)
            self.budzet -= obj.cena
            return self.motocykle, self.budzet


    def sprzedaj(self, index_obj):
        if index_obj.typ == 'osobowe':
            self.budzet += (index_obj.cena + (index_obj.cena/10))
            self.osobowe.pop(index_obj)
            return self.osobowe, self.budzet
        elif index_obj.typ == 'ciezarowe':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.ciezarowe.pop(index_obj)
            return self.ciezarowe, self.budzet
        elif index_obj.typ == 'motocykle':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.motocykle.pop(index_obj)
            return self.motocykle, self.budzet


