class Cell():
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        self.total = self.number_cells + other.number_cells
        return self.total

    def __sub__(self, other):
        self.total_sub = self.number_cells - other.number_cells
        if self.total_sub == 0:
            self.total_sub = 'разность ячеек двух клеток НЕ больше нуля'
        elif self.total_sub < 0:
            self.total_sub = -self.total_sub
        return self.total_sub

    def __mul__(self, other):
        self.total_mul = self.number_cells * other.number_cells
        new_cell = Cell(self.total_mul)
        return new_cell

    def __truediv__(self, other):
        if self.number_cells > other.number_cells:
            self.total_div = self.number_cells // other.number_cells
        else:
            self.total_div = other.number_cells // self.number_cells
        new_cell = Cell(self.total_div)
        return new_cell

    def make_order(self, numb_per_line):
        hgh

a1 = Cell(3)
a2 = Cell(4)

c = a1*a2
d = a1/a2
print(a1+a2)
print(a1-a2)
print(c.number_cells)
print(d.number_cells)