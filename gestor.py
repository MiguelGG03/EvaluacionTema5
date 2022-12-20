class Personaje:
    def __init__(self,nombre:str,vida:int,daño:int,defensa:int,alcanze:int):
        if(type(nombre)!=str):
            raise TypeError('El nombre debe ser un string')
        else:
            self.nombre=nombre
        if(type(vida)!=int):
            raise TypeError('La vida debe ser un entero')
        elif(vida<=0):
            raise ValueError('La vida debe ser mayor que 0')
        else:
            self.vida=vida
        if(type(daño)!=int):
            raise TypeError('El daño debe ser un entero')
        elif(daño<=0):
            raise ValueError('El daño debe ser mayor que 0')
        else:
            self.daño=daño
        if(type(defensa)!=int):
            raise TypeError('La defensa debe ser un entero')
        elif(defensa<=0):
            raise ValueError('La defensa debe ser mayor que 0')
        else:
            self.defensa=defensa
        if(type(alcanze)!=int):
            raise TypeError('El alcanze debe ser un entero')
        elif(alcanze<=0):
            raise ValueError('El alcanze debe ser mayor que 0')
        else:
            self.alcanze=alcanze


class Gestor:

    def __init__(self):
        self.lista_personajes=[]


    def añadir_personaje(self,personaje):
        if(type(personaje)!=Personaje):
            raise TypeError('El personaje debe ser de tipo Personaje')
        else:
            for i in self.lista_personajes:
                if(i==personaje):
                    raise ValueError('El personaje ya existe')
            self.lista_personajes.append(personaje)


    def eliminar_personaje(self,personaje):
        if(type(personaje)!=str):
            raise TypeError('Debe introducir el nombre del personaje')
        else:
            for i in self.lista_personajes:
                if(i.nombre==personaje):
                    self.lista_personajes.remove(i)


    def __str__personaje__(self,personaje):
        for i in self.lista_personajes:
            if(i.nombre==personaje):
                return 'Nombre: {}, Vida: {}, Daño: {}, Defensa: {}, Alcanze: {}'.format(i.nombre,i.vida,i.daño,i.defensa,i.alcanze)
    
    def __str__(self):
        print('Nombre, Vida, Daño, Defensa, Alcanze')
        for i in self.lista_personajes:
            print('{}, {}, {}, {}, {}'.format(i.nombre,i.vida,i.daño,i.defensa,i.alcanze))


def main_gestor():
    gestor=Gestor()
    caballero=Personaje('Caballero',4,2,4,2)
    arquero=Personaje('Arquero',2,4,1,8)
    guerrero=Personaje('Guerrero',2,4,2,4)
    print('No hay nada')
    gestor.__str__()
    gestor.añadir_personaje(caballero)
    gestor.añadir_personaje(arquero)
    gestor.añadir_personaje(guerrero)
    print('\nAñadimos 3 personajes\n')
    gestor.__str__()
    gestor.eliminar_personaje('Arquero')
    print('\nEliminamos al Arquero\n')
    gestor.__str__()


if __name__=='__main__':
    main_gestor()