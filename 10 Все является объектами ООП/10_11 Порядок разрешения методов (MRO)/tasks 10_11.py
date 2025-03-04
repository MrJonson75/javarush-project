# Использование super() и MRO

# Создайте классы A, B, C, и D, где B и C наследуют от A, а D наследует от B и C.
# В каждом классе определите метод method, который выводит имя класса и вызывает метод super().method().
# Создайте экземпляр класса D и вызовите метод method, чтобы понять порядок вызова методов по MRO.

# Напишите тут ваш код

class A:

    def method(self):
        print('class A')


class B(A):

    def method(self):
        print('class B')
        super().method()


class C(A):

    def method(self):
        print('class C')
        super().method()


class D(B, C):

    def method(self):
        print('class D')
        super().method()


obj = D()
obj.method()




# Переопределение метода

# Создайте классы M, N, и O, где N и O наследуют от M.
# В каждом классе определите метод action, который выводит имя класса
# и вызывает метод родительского класса с помощью super().
# Проверьте порядок вызова методов, создав экземпляр класса N и вызвав метод action.

# Напишите тут ваш код


class M:

    def action(self):
        print('class M')


class N(M):

    def action(self):
        print('class N')
        super().action()


class O(M):

    def action(self):
        print('class O')
        super().action()


obj = N()
obj.action()