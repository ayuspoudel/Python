class LinearEquation:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def a(self):
        return self.point1[1] - self.point2[1]

    def b(self):
        return -(self.point1[0] - self.point2[0])

    def c(self):
        return self.point3[1] - self.point4[1]

    def d(self):
        return -(self.point3[0] - self.point4[0])

    def e(self):
        return ((self.point1[1] - self.point2[1]) * self.point1[0]) - ((self.point1[0] - self.point2[0]) * self.point1[1])

    def f(self):
        return ((self.point3[1] - self.point4[1]) * self.point3[0]) - ((self.point3[0] - self.point4[0]) * self.point3[1])

    
    def __str__(self):
        return  (f'The equation of the first line (with points ({self.point1[0]}, {self.point1[1]}) and ({self.point2[0]}, {self.point2[1]})) is: \n'
                f'{self.a}x + {self.b}y = {self.e}\n'
                f'The equation of the second line (with points ({self.point3[0]}, {self.point3[1]}) and ({self.point4[0]}, {self.point4[1]})) is: \n'
                f'{self.c}x + {self.d}y = {self.f}')

    def Boolean(self):
        status = True
        if (self.a * self.d) - (self.b * self.c) != 0:
            status = True
            return status
        else:
            status = False
            return status

    def intersecting_points(self):
        x = ((self.e * self.d) - (self.b * self.f)) / ((self.a * self.d) - (self.b * self.c))
        y = ((self.a * self.f) - (self.e * self.c)) / ((self.a * self.d) - (self.b * self.c))
        return x,y

def main():
    x1 , y1 = input("Enter the x and y coordinates of point 1:").split()
    x2 , y2 = input("Enter the x and y coordinates of point 2:").split()
    x3 , y3 = input("Enter the x and y coordinates of point 1:").split()
    x4 , y4 = input("Enter the x and y coordinates of point 1:").split()

    x1,x2,x3,x4,y1,y2,y3,y4 = float(x1), float(x2), float(x3), float(x4), float(y1), float(y2), float(y3), float(y4)

    point1 = (x1, y1)
    point2 = (x2, y2)
    point3 = (x3, y3)
    point4 = (x4, y4)

    linear = LinearEquation(point1,point2,point3,point4)

    print(linear)

    choice = linear.Boolean()
    intersect = linear.intersecting_points()
    if choice == True:
        print(f'The intersecting point is: ({intersect[0]:.1f}, {intersect[1]:.1f})')
    else:
        print('The two lines do not intersect.')
