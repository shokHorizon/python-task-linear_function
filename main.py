class dotsclass:
    def __init__(self, x:int=None, y:int=None) -> None:
        # Предусмотрена возможность инициализации класса без мнговенного добавления точки
        self.dots = list()
        if None not in (x, y):
            self.__call__(x, y)
        
    def __call__(self, x: int, y: int):
        self.add_dot(x, y)
        return self
        
    def add_dot(self, x: int, y: int):
        try:
            # Поиск и замена существующей координаты x
            index = [dot[0] for dot in self.dots].index(x)
            self.dots[index] = (x, y,)
        except ValueError:
            # Добавление новой точки и сортировка массива
            self.dots.append((x, y,))
            self.dots.sort(key=lambda x: x[0])
            
    def y(self, x):
        try:
            # Поиск ближайших точек
            less_x_dot = [dot for dot in self.dots if dot[0]<=x][-1]
            greater_x_dot = [dot for dot in self.dots if dot[0]>=x][0]
            # Вычисление коэффицентов и подстановка в формулу
            linear_equasion = self.get_linear_equation(
                less_x_dot[0],
                greater_x_dot[0],
                less_x_dot[1],
                greater_x_dot[1]
                )
            result = x * linear_equasion[0] + linear_equasion[1]
            print(result)
        except IndexError:
            # Введенная координата за пределами функции
            print(f"{self.dots[0]=} and {self.dots[-1]=} but got {x=}")
            raise ValueError("x coordinate is out of boundaries")
            
    def print_table(self):
        print('_'*25)
        print(f"| {'  | '.join(('x1', 'x2', ' a', ' b'))}  |")
        for i in range(len(self.dots)-1):
            print('-'*25)
            dot1 = self.dots[i]
            dot2 = self.dots[i+1]
            a, b = self.get_linear_equation(dot1[0], dot2[0], dot1[1], dot2[1])
            print(f"|{dot1[0]:5}|{dot2[0]:5}|{a:5.2f}|{b:5.2f}|")
        print('-'*25)
    
    @staticmethod
    def get_linear_equation(x1, x2, y1, y2):
        if x2 != x1:
            a = (y2-y1)/(x2-x1)
            b = (x2*y1-x1*y2)/(x2-x1)
            return((a, b))
        raise ValueError


def main():
    f = dotsclass(0,100)(10,122)
    f(30,0)
    f.y(5)
    f.print_table()


if __name__ == "__main__":
    main()
