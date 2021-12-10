from tkinter import *
from tkinter import filedialog as fd

out = []
str_ = ''
data_output = []


def read_file():
    file_name = fd.askopenfilename()
    f = open(file_name)
    data = f.read()
    data = data.replace(',', '.')
    data = data.split()
    edited_data = []
    for i in range(len(data)):
        edited_data.append(float(data[i]))
    f.close()
    return edited_data


def quantiles(n):
    if 15 < n <= 16:
        d1, d2 = 0.8884, 0.7236
    if 16 < n <= 21:
        d1, d2 = 0.8768, 0.7304
    if 21 < n <= 26:
        d1, d2 = 0.8686, 0.7360
    if 26 < n <= 31:
        d1, d2 = 0.8625, 0.7404
    if 31 < n <= 36:
        d1, d2 = 0.8578, 0.7440
    if 36 < n <= 41:
        d1, d2 = 0.8540, 0.7470
    if 41 < n <= 46:
        d1, d2 = 0.8508, 0.7496
    if 46 < n <= 51:
        d1, d2 = 0.8481, 0.7518
    if (n <= 15) or (n > 51):
        print("ERROR: n out of range:")
        print("n = " + n)
        exit(1)
    return d1, d2


def calculate():
    data = read_file()
    n = len(data)
    summa, sum_for_s, sum_fof_d = 0, 0, 0
    data_output.append(str(n))

    for i in range(n):
        summa += data[i]
    average_value = summa / n

    for i in range(n):
        sum_for_s += (data[i] - average_value) ** 2

    S = (sum_for_s / (n - 1)) ** 0.5
    data_output.append(str(S))

    for i in range(n):
        sum_fof_d += abs(data[i] - average_value)

    d = sum_fof_d / (n * S)
    d = round(d, 4)
    data_output.append(str(d))

    d1, d2 = quantiles(n)

    if d2 < d <= d1:
        str_ = 'Выборка принадлежит к нормальному рапределению'
    else:
        str_ = 'Выборка не принадлежит к нормальному рапределению'


def main():
    root = Tk()
    b2 = Button(text="Сделать расчет", command=calculate())
    b2.grid(row=1, column=1, sticky=W)
    l1 = Label(text=f"Результат для выборки из {data_output[0]} элементов,\n"
                    f"смещенное среднее квадратическое значение {data_output[1]},\n"
                    f"рассчитанное отношение d = {data_output[2]}", font="Arial 14")
    l1.config(bd=30)
    l1.grid(row=2, column=1)
    l2 = Label(text=str_, font="Arial 14")
    l2.config(bd=30)
    l2.grid(row=3, column=1)

    root.mainloop()


if __name__ == '__main__':
    main()
