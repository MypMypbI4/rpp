from abc import abstractmethod, ABC


class Animal(ABC):
    __text = "Пример инкапсуляции в виде звука животного"

    def new_sound(self, txt):
        self.__text = txt

    def get_sound(self):
        return self.__text

    @abstractmethod
    def animal_name(self):
        pass
