from hashlib import sha256

def hashage(chaine: str) -> str:
    """ Retourne le hash d'une chaine donnée"""
    return sha256(chaine.encode('utf-8')).hexdigest()

# https://andersbrownworth.com/blockchain/block

#print(hashage('Olivier'))

class Block:


    def __init__(self, num, data):
        self.num_block = num
        self.nonce = 0
        self.data = data
        self.hash = self._hashage()
        self.valide = False

    def _hashage(self):
        #print(self.__dict__)
        chaine = "".join([str(self.num_block), str(self.nonce), self.data])
        return sha256(chaine.encode('utf-8')).hexdigest()

    def minage(self):
        """ Un block est valide s'il commence par un 0"""
        if not valide:
            pass


block = Block(1, "cocuou")
print(block._hashage())