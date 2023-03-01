def myp_add_new_data(d, article, name, count, price):
    with open("MypinputLab4.txt", "a", encoding='utf-8') as f:
        for v in d:
            f.write(f"{v['article']},{v['name']},{v['count']},{v['price']}\n")
        f.write(f"{article},{name},{count},{price}\n")
    d.append({"article": article, "name": name, "count": int(count), "price": int(price)})

class Row:
    article = 0

    def __init__(self, article: str):
        self.article = article

    def get_article(self):
        return self.article

    def set_article(self, val):
        self.article = val


class RowModel(Row):
    article = ""
    name = ""
    count = ""
    price = ""

    def __init__(self, article: str, name: str, count: str, price: str):
        super().__init__(article)
        self.name = name
        self.count = count
        self.price = price

    def __str__(self):
        return f"Запись №{self.article}, {self.name}, {self.count}, {self.price}"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data:
    file_path = ""
    data = []
    pointer = 0

    def __init__(self, path: str):
        self.file_path = path
        self.data = self.parse(self.file_path)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            z = self.data[self.pointer]
            self.pointer += 1
            return z

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")

        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    def name_sort(self):
        return list(sorted(self.data, key=lambda f: f.name))

    def count_sort(self):
        return list(sorted(self.data, key=lambda f: f.count))

    def select_len(self, value):
        return [rm for rm in self.data if len(rm.price) > value]

    # def add_new(self, name, count, price):
    #     if len(self.data) == 0:
    #         self.data.append(RowModel(1, name, count, price))
    #     else:
    #         self.data.append(RowModel(self.data[len(self.data) - 1].article + 1, name, count, price))
    #     self.save(self.file_path, self.data)

    # def myp_add_new_data(self, article, name, count, price):
    #     self.data.append(RowModel(article, name, count, price))

    @staticmethod
    def output(vec):
        for k in vec:
            print(f"Запись №{k.article}, {k.name}, {k.count}, {k.price}")

    @staticmethod
    def parse(path):
        parsed = []
        with open(path, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (article, name, count, price) = line.replace("\n", "").split(",")
                parsed.append(RowModel(article, name, count, price))
        return parsed

    @staticmethod
    def save(path, new_data):
        with open(path, "w", encoding='utf-8') as f:
            for rm in new_data:
                f.write(f"{rm.article},{rm.name},{rm.count},{rm.price}\n")


if __name__ == '__main__':
    data = Data('MypinputLab4.txt')

    print('\n\n\nБез сортировки' + '\n' + '_' * 128)
    print(str(data))

    print('\n\n\nИтератор' + '\n' + '_' * 128)
    for item in iter(data):
        print(item)

    print('\n\n\nГенератор' + '\n' + '_' * 128)
    for item in data.generator():
        print(item)

    print('\n\n\nСортировка по названию' + '\n' + '_' * 128)
    data.output(data.name_sort())

    print('\n\n\nСортировка по количеству' + '\n' + '_' * 128)
    data.output(data.count_sort())

    print('\n\n\nСортировка по значению цены' + '\n' + '_' * 128)
    data.output(data.select_len(70))

    print('\n\n\nВыбор по индексу' + '\n' + '_' * 128)
    article = int(input("Индекс: "))
    print(f"\n{data[article]}")

    # добавление строки
    #data.add_new("T E S T 3", "2027-02-02 15:15:00", "MDA")
    myp_add_new_data(Data.data, "1112ууу4", "Новизна", "10", "8")
    #print(Data.data)
