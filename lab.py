# Utils methods
def get_valid_input(cast_type, enter_str = None, if_ex_ret = False):
    input_val = None
    x = None
    while(x == None):
        if enter_str: print(enter_str)
        try:
            input_val = input()
            x = cast_type(input_val)
        except:
            if if_ex_ret:
                return input_val
            print(f'Exception while casting to {cast_type}')
            continue
    return x


# tasks
def task2(): 
    print("Hellow, World!")

def task3():
    a = 3
    print('type of a =', type(a)) # will print int
    a = 3.5
    print('type of a =', type(a)) # will print float
    a = 'qwerty'
    print('type of a =', type(a)) # will print str
    a = True
    print('type of a =', type(a)) # will print bool
    a = '123'
    print('type of a =', type(a)) # will print str

def task4():
    a = 5.7
    print('a before =', a)
    a = int(a)
    print('a after =', a)
    a = -5.7
    print('a before =', a)
    a = int(a)
    print('a after =', a)
    print('Calculation result of [3**39 - int(float(3**39))] =', 3**39 - int(float(3**39)))

def task5():
    name = ''
    while(name == ''):
        print('Enter the username:')
        name = str(input())
    print('Hewo,', name)

def task6():
    hours, minutes = [get_valid_input(float, 'Enter the number:') for i in range(2)]
    # hours = get_valid_input(float, 'Enter the X:')
    # minutes = get_valid_input(float, 'Enter the Y:')
    print('X =', hours)
    print('Y =', minutes)
    print('Total:', hours * 60 + minutes)

def task7():
    a = False
    b = True
    c = False
    print("Result:", not a or b and c)
    print("Result2:", not (a or b) and c)

def task8():
    year = get_valid_input(int, f'Enter the year:')
    if (year < 1900 or year > 3000):
        print(f'This year [{year}] is not included in set.')
    elif (year % 4 == 0):
        print(f'This year [{year}] is a leap year')
    else:
        print(f'This year [{year}] is not a leap year')

def task9():
    i = 0
    while(i < 20):
        i += 2
        print(i, end=' ')
    print()

def task10():
    sum = 0
    input = None
    while(input != 0):
        input = get_valid_input(int, 'Enter the number:')
        sum += input
    print(f'Total sum: {sum}')

def factorization(num):
    lst = []
    rem = num
    divider = 2
    exit_num = 1
    while (rem != exit_num):
        while(rem % divider == 0):
            rem = rem / divider
            lst.append(divider)
            if (rem % 2 == 0): 
                exit_num = 0
            else:
                exit_num = 1
        divider += 1
    return lst

def task11():
    x, y = [get_valid_input(int, 'Enter the number') for i in range(2)]
    # x = get_valid_input(int, 'Enter the X:')
    # y = get_valid_input(int, 'Enter the Y:')
    lst1 = factorization(x)
    lst2 = factorization(y)

    intersection = []
    for x in lst1:
        if x in lst2: 
            lst1.remove(x)
            lst2.remove(x)
            intersection.append(x)
    result_lst = []
    result_lst.append(intersection)
    result_lst.append(lst1)
    result_lst.append(lst2)
    # j for i in x for j in i
    result_lst = [y for x in result_lst for y in x]
    result = 1
    for i in result_lst:
        result = result * i;
    
    print('Pieces count:', result)

def task12():
    for i in range(1,20):
        if (i % 2 == 0): print(i, end=' ')
    print()

def task13():
    a, b, c, d = [get_valid_input(int, 'Enter the number') for i in range(4)]
    # a = get_valid_input(int, 'Enter the number:')
    # b = get_valid_input(int, 'Enter the number:')
    # c = get_valid_input(int, 'Enter the number:')
    # d = get_valid_input(int, 'Enter the number:')

    mat = []

    for i in range(a, b + 1):
        row = []
        for j in range(c, d + 1):
            row.append(i * j)
        mat.append(row)

    print('Result:')
    for i in range(c, d + 1):
        print(f'\t{i}', end='')
    print()
    row_i = a
    for row in mat:
        print(f'{row_i}\t', end='')
        for j in row:
             print(f'{j}\t', end='')
        row_i += 1
        print()
    print()

def task14():
    n = get_valid_input(int, 'Enter the matrix size:')
    return 

# This is a useful Python script.
import time
from tkinter import messagebox

def task15():
    num = 3
    while(True):
        num -= 1
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
        time.sleep(5)
        if (num == 0): return

# TASK 16
from tkinter import *

class WindowProps:
    title = ''
    size = ''
    def __init__(self, title = '', size = '500x250'):
        self.title = title
        self.size = size

class App:
    window = {}
    messageBoxBtn = {}
    def __init__(self, windowProps = WindowProps(title='Application',size='500x500')):
        self.window = Tk();
        self.window.title(windowProps.title)
        self.window.geometry(windowProps.size)

        messageBoxLabel = Label(self.window, text='Press this button to run infinite MsgBox', font=('Arial Bold', 14))
        messageBoxLabel.grid(column=0, row=0)
        self.messageBoxBtn = Button(self.window, text='MsgBox', command=self.MsgBoxBtn_callback)
        self.messageBoxBtn.grid(column=1, row=0)

        exitLabel = Label(self.window, text='Press this button to exit', font=('Arial Bold', 14))
        exitLabel.grid(column=0, row=1)
        exitBtn = Button(self.window, text='Exit', command=self.exit_button_callback)
        exitBtn.grid(column=1, row=1)

    def run(self):
        self.window.mainloop()

    def MsgBoxBtn_callback(self): 
        while(True):
            messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
            time.sleep(5)

    def exit_button_callback(self):
        quit();

def task16():
    app = App();
    app.run()

taks_list = [
    task2,
    task3,
    task4,
    task5,
    task6,
    task7,
    task8,
    task9,
    task10,
    task11,
    task12,
    task13,
    task14,
    task15,
    task16
]

def main():
    for i in range(len(taks_list)):
        print('--- Task {} ---'.format(i + 2))
        taks_list[i]()
        print()
    
if __name__ == '__main__':
    main()