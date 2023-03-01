import os, os.path


def myp_get_string_using_csv_file_path(csv_file_path):
    dataa = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        for row in csv_file:
            article, name, count, price = row.replace("\n", "").split(",")
            try:
                dataa.append({"article": article, "name": name, "count": int(count), "price": int(price)})
            except ValueError:
                continue
    return dataa


def myp_add_new_data(d, article, name, count, price):
    with open("MypinputLab3.txt", "w", encoding='utf-8') as f:
        for v in d:
            f.write(f"{v['article']},{v['name']},{v['count']},{v['price']}\n")
        f.write(f"{article},{name},{count},{price}\n")
    d.append({"article": article, "name": name, "count": int(count), "price": int(price)})


def myp_count_files(path):
    (loc, dirs, files) = next(os.walk(path))
    return len(files)


if __name__ == '__main__':

    folder_name = input("Название папки:")
    print("Количество файлов в папке:")
    print(myp_count_files(folder_name))

    data = myp_get_string_using_csv_file_path("MypinputLab3.txt")

    myp_add_new_data(data, "1112ууу4", "Новизна", "10", "5")
    #print(data)
    n = 2
    print("Сортировка по названию")
    print(sorted(data, key=lambda d: d["name"]))
    print("Сортировка по цене")
    print(sorted(data, key=lambda d: d["price"]))
    print("Сортировка по количеству больше ", n)
    print([v for v in data if v["count"] > n])