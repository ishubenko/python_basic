from abc import abstractmethod, ABC

class Clothes(ABC):
    @property
    @abstractmethod
    def consuption(self):
        pass

    @property
    @abstractmethod
    def params(self):
        pass

class Costume(Clothes):
    def __init__(self, height, name):
        self.height = height
        self.type = name

    @property
    def consuption(self):
        return self.height * 2 + 0.3

    def params(self):
        return self.height

class Coat(Clothes):
    def __init__(self, size, name):
        self.size = size
        self.type = name

    @property
    def consuption(self):
        return self.size / 6.5 + 0.5

    def params(self):
        return self.size
