from tkinter import *
from tkinter import ttk
import random as rd


def multiply_x(a, b=2):
    """
    :param a: chek this var
    :param b: default 2
    :return: bool
    """
    if a % b == 0:
        c = True
    else:
        c = False
    return c


def decorator_tk(func):
    def wrapper(*args, **kwargs):
        root = Tk()
        root.title("Dz Mikhailov")
        root.geometry("800x230+300+150")

        # определяем столбцы
        columns = ("Number", "Comment_1", "Comment_2")

        tree = ttk.Treeview(columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=1)
        tree.column("#1", stretch=YES, anchor=S)
        tree.column("#2", stretch=YES, anchor=S)
        tree.column("#3", stretch=YES, anchor=S)

        # определяем заголовки
        tree.heading("Number", text="Число", anchor=S)
        tree.heading("Comment_1", text="Кратность 3", anchor=S)
        tree.heading("Comment_2", text="Кратность 2", anchor=S)

        in_passing = func(*args, **kwargs)

        # определяем данные для отображения
        listik = []
        num_dict = []
        for i in sorted(in_passing):
            listik.clear()
            listik.append(i)
            if multiply_x(i, 3):
                listik.append("Кратно 3")
            else:
                listik.append("Не кратно 3")

            if multiply_x(i):
                listik.append("Парное")
            else:
                listik.append("Не парное")
            num_dict.append(tuple(listik))
        # добавляем данные
        for table in num_dict:
            tree.insert("", END, values=table)

        root.mainloop()
        return func
    return wrapper


@decorator_tk
def make_set(a):
    """
    :param a: len(set)
    :return: set()
    """
    set_1 = set()
    while len(set_1) < a:
        set_1.add(rd.randint(1, 50 * a))
    return set_1


if __name__ == "__main__":

    make_set(10)
