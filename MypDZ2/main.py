from Cat import Cat
from Dog import Dog

if __name__ == '__main__':
    # наследование: Animal является родительским классом для Cat и Dog
    vec = [Cat(), Dog()]

    # полиморфизм - функция имени животного переопределена в классе каждого животного
    for i in vec:
        i.animal_name()
    print('\n')

    # инкапсуляция - теперь в виде звука животного!
    cat = Cat()
    dog = Dog()

    print(cat.get_sound())
    cat.new_sound("Никогда ранее не слышанный новый звук, однако, похоже, всё того же животного")
    print(cat.get_sound())
    print('\n')
