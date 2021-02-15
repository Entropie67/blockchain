# https://andersbrownworth.com/blockchain/block
from hashlib import sha256
from colorama import Fore, Style

class Block:


    def __init__(self, data, block=None):
        self.num_block = 0 if not block else (block.num_block + 1)
        self.nonce = 0
        self.data = data
        self.block_precedent = block
        self.hash = self._hashage()
        self.valide = False

    def _hashage(self):
        #print(self.__dict__)
        chaine = "".join([str(self.num_block), str(self.nonce), self.data, '' if not self.block_precedent else self.block_precedent.hash])
        return sha256(chaine.encode('utf-8')).hexdigest()

    def minage(self):
        """ Un block est valide s'il commence par un 0"""
        while not self.valide:
            self.nonce += 1
            temp = self._hashage()
            if temp[:4] == "0000":
                self.valide = True
                self.hash = temp

    def __str__(self):
        if self.valide:
            return f'{Fore.GREEN}' + str(self.__dict__) + f'{Style.RESET_ALL}'
        else:
            return f'{Fore.RED}' + str(self.__dict__) + f'{Style.RESET_ALL}'

    def chaine_valide(self):

        if self.valide:
            block = self.block_precedent
        else:
            return False
        while block.num_block >=0:
            print(block)
            if block.valide:
                block = self.block_precedent
            else:
                return False


block = Block("cocuou")
print(block._hashage())
print(block)
block.minage()
print(block)
block2 = Block('des trucs', block)
print(block2)
block2.minage()
print(block2)
block3 = Block('Je suis le puissant block numéro 3', block2)
print(block3)
block3.minage()
print(block3)
print("Validation")
print(block3.chaine_valide())