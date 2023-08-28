
class User:
    def __init__(self, name, email, position, age, attribute) -> None:
        self.name       = name
        self.email      = email
        self.position   = position
        self.__age      = age      # atributo privado para probar acceso
        self._attribute = attribute

    @property
    def age(self):
        return self._User__age

    @age.setter
    def age(self, age):
        self._User__age = age

if __name__ == '__main__':
    user1 = User('Aldair', 'correo@gmail.com', 'admin', 54, 'attribute')
    print(type(user1))
    print(isinstance(user1, User))
    try:
        #print(user1.__age)
        user1.age = 15

    except AttributeError as error:
        print(error)
    print(user1.age)
    #print(user1._attribute)

    #print(user1._User__age) # acceder a un atributo privado _Class__attribute

