from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, base, altura): # Llaman esto
        super().__init__()
        self.base = base
        self.altura = altura
        self.tipo = "Shape"
    
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return f"{self.tipo} de base {self.base} y altura {self.altura}"
    


class Triangle(Shape):

    def area(self):
        return self.base * self.altura/2
    
    def description(self):
        return f"un triangulo muy bonito de base {self.base} y altura {self.altura}"
    
    def color(self):
        return "azul"
    
    
class Rectangle(Shape):
    def __init__(self, base, altura):
        super().__init__(base, altura) #Esto
        self.tipo = "Rectangulo"
    
    def area(self):
        return self.base * self.altura
    
   