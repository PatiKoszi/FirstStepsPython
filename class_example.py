
class Dog:
    def voice(self):
        print("How, How")

class Cat:
    def voice(self):
        print("Miau, Miau")

dog = Dog()
cat = Cat()

dog.voice()
cat.voice()


class Dog:

    def __init__(self):
        pass

    def voice(self):
        print('Gaaf')


class Cat:

    def voice(self):
        print('Mew')


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()

    dog.voice()
    cat.voice()

