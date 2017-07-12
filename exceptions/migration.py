import ducks
flocks=ducks.Flock()
donald=ducks.Duck()
daisy=ducks.Duck()
duck1=ducks.Duck()
duck2=ducks.Duck()
duck3=ducks.Duck()
duck4=ducks.Duck()
duck5=ducks.Duck()
percy=ducks.Penguin()
flocks.add_duck(donald)

flocks.add_duck(daisy)

flocks.add_duck(duck1)

flocks.add_duck(duck5)

flocks.add_duck(duck3)

flocks.add_duck(duck2)

flocks.add_duck(duck4)

flocks.add_duck(percy)

flocks.migrate()