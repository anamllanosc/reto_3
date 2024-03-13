class Point :
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,start:Point,end:Point): # parametro.Clase

        
        self.start=start
        self.end=end
        self.lenght=self.compute_lenght()
        self.slope=self.compute_slope()
        

    def compute_lenght(self):

        self.a=(self.end.x-self.start.x)
        self.b=(self.end.y-self.start.y)
        self.lenght=((self.a**2+self.b**2)**0.5)
        return (self.lenght)
    
    def compute_slope(self):

        if (self.end.x - self.start.x) == 0:
            return float('inf')
        else:
            self.slope=(self.b/self.a)
            return (self.slope)
    
    def compute_horizontal_cross(self):

        if self.start.y<0 and self.end.y>0:
            cross_point=Point(((0- self.start.y)/self.slope)+self.start.x , 0) # y = 0 => Corte con el eje X
            return (cross_point)
        else:
            return ("La linea no corta con el eje X")

class Rectangle:
    def __init__(self,method:int,*args):
    
        if method == 1:

            self.width=args[1]
            self.height=args[2]
            self.center=Point(args[0].x+(args[1]/2),args[0].y+(args[2]/2))


        elif method == 2:

            self.center:Point=args[0]
            self.width=args[1]
            self.height=args[2]
            

        elif method==3:

            self.center=Point(args[1].x-((args[1].x-args[0].x)/2),args[0].y-((args[1].y-args[0].y)/2))
            self.width=abs(args[1].x-args[0].x)
            self.height=abs(args[1].y-args[0].y)
            self.bottom_left=Point(args[1].x-args[0].x,args[1].y-args[0].y,)
            self.center=Point(args[1].x-((args[1].x-args[0].x)/2),args[0].y-((args[1].y-args[0].y)/2))

        elif method==4:
            
    
            self.l1:Line=args[0]
            self.l2:Line=args[1]
            
            self.l1.lenght

            if self.l1.lenght >= self.l2.lenght:
                self.width=(args[1].lenght)
                self.height=(args[0].lenght)

            else:
                self.width=(args[0].lenght)
                self.height=(args[1].lenght)

  
        else:
            return ("Invalid Method")     

    def compute_area(self):
        return(self.width*self.height)
    
    def compute_perimeter(self):
        return(2*self.width+2*self.height)
    

method=int(input("Ingrese el numero de metodo con el que desea inicializar el rectangulo:"))

if method== 1:

    width= float(input("Ingrese el ancho del rectangulo: "))
    height= float(input("Ingrese el alto del rectangulo: "))
    x= float(input("Ingrese la cordenada en x de la esquina inferior izquierda: "))
    y= float(input("Ingrese la cordenada en y de la esquina inferior izquierda: "))

    rectangle=Rectangle(1,Point(x,y),width,height)

    print(f"Bottom Left Point: {x},{y}")

elif method== 2:
    width= float(input("Ingrese el ancho del rectangulo: "))
    height= float(input("Ingrese el alto del rectangulo: "))
    x= float(input("Ingrese la cordenada en x de la esquina inferior izquierda: "))
    y= float(input("Ingrese la cordenada en y de la esquina inferior izquierda: "))
    center=Point(x+(width/2),y+(height/2))
    rectangle=Rectangle(2,center,width,height)

    print(f"Center Point: {center.x},{center.y}")

elif method == 3:
    x1=float(input("Ingrese la cordenada en x de la esquina inferior izquierda: "))
    y1=float(input("Ingrese la cordenada en y de la esquina inferior izquierda: "))
    x2=float(input("Ingrese la cordenada en x de la esquina superior derecha: "))
    y2=float(input("Ingrese la cordenada en y de la esquina superior derecha: "))

    rectangle=Rectangle(3,Point(x1,y1),Point(x2,y2))

elif method==4:
    x1=float(input("Ingrese la cordenada en x de la esquina superior izquierda del rectangulo: "))
    y1=float(input("Ingrese la cordenada en y de la esquina superior izquierda del rectangulo: "))
    y2=float(input("Ingrese la cordenada en y de la esquina inferior izquierda del rectangulo: "))
    x3=float(input("Ingrese la cordenada en x de la esquina inferior derecha del rectangulo: "))

    l1=Line(Point(x1,y1),Point(x1,y2))
    l2=Line(Point(x1,y2),Point(x3,y2))
    rectangle=Rectangle(4,l1,l2)


    

print(f"Area del rectangulo inicializado con el metodo #{method} = {rectangle.compute_area()}")
print(f"Perimetro del rectangulo inicializado con el metodo #{method} = {rectangle.compute_perimeter()}")

