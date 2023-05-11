import tkinter
from tkinter import *
deltatime = 0.5
window_draw_size_x = 500
window_draw_size_y = 400
tp_v = 0.02 #теплопроводность воздуха
t_v = -25 # начальная температура воздуха
t_p1 = 10 # начальная температура комнаты 1
t_p2 = 10 # начальная температура комнаты 2
t_r = 40


bool_window1 = False
bool_window2 = False
bool_window3 = False
bool_window4 = False
bool_window5 = False
bool_door1 = False
bool_door2 = False
bool_regulator = False


main = Tk()
main.geometry("800x400")
main.resizable(width=False, height=False)


canvas1 = Canvas(main, bg="white", width=window_draw_size_x, height=window_draw_size_y)

room1 = canvas1.create_rectangle(window_draw_size_x * 0.1, window_draw_size_y * 0.2, window_draw_size_x * 0.4,
                                 window_draw_size_y * 0.8, fill="white")
room2 = canvas1.create_rectangle(window_draw_size_x * 0.4, window_draw_size_y * 0.2, window_draw_size_x * 0.8,
                                 window_draw_size_y * 0.8, fill="white")

window1 = canvas1.create_rectangle(window_draw_size_x * 0.2, window_draw_size_y * 0.18, window_draw_size_x * 0.3,
                                   window_draw_size_y * 0.22, fill="red")
text1 = canvas1.create_text((window_draw_size_x * 0.25, window_draw_size_y * 0.2), text="окно 1")



window2 = canvas1.create_rectangle(window_draw_size_x * 0.5, window_draw_size_y * 0.18, window_draw_size_x * 0.7,
                                   window_draw_size_y * 0.22, fill="red")
text2 = canvas1.create_text((window_draw_size_x * 0.6, window_draw_size_y * 0.2), text="окно 2")

window3 = canvas1.create_rectangle(window_draw_size_x * 0.78, window_draw_size_y * 0.4, window_draw_size_x * 0.82,
                                   window_draw_size_y * 0.6, fill="red")
text3 = canvas1.create_text((window_draw_size_x * 0.8, window_draw_size_y * 0.5), text="окно 3")

window4 = canvas1.create_rectangle(window_draw_size_x * 0.5, window_draw_size_y * 0.78, window_draw_size_x * 0.7,
                                   window_draw_size_y * 0.82, fill="red")
text4 = canvas1.create_text((window_draw_size_x * 0.6, window_draw_size_y * 0.8), text="окно 4")

window5 = canvas1.create_rectangle(window_draw_size_x * 0.08, window_draw_size_y * 0.4, window_draw_size_x * 0.12,
                                   window_draw_size_y * 0.6, fill="red")
text5 = canvas1.create_text((window_draw_size_x * 0.1, window_draw_size_y * 0.5), text="окно 5")

door1 = canvas1.create_rectangle(window_draw_size_x * 0.2, window_draw_size_y * 0.78, window_draw_size_x * 0.3,
                                 window_draw_size_y * 0.82, fill="red")
text_door1 = canvas1.create_text((window_draw_size_x * 0.25, window_draw_size_y * 0.8), text="дверь 1")

door2 = canvas1.create_rectangle(window_draw_size_x * 0.38, window_draw_size_y * 0.4, window_draw_size_x * 0.42,
                                 window_draw_size_y * 0.6, fill="red")
text_door2 = canvas1.create_text((window_draw_size_x * 0.4, window_draw_size_y * 0.5), text="дверь 2")

regulator = canvas1.create_rectangle(window_draw_size_x * 0.76, window_draw_size_y * 0.2, window_draw_size_x * 0.8,
                                 window_draw_size_y * 0.24, fill="red")
Label1 = tkinter.Label(text="Температура левой комнаты")
Label2 = tkinter.Label(text="Температура правой комнаты")
Label3 = tkinter.Label(text="Температура регулятора")
Label4 = tkinter.Label(text=str(t_p1))
Label5 = tkinter.Label(text=str(t_p2))
Label6 = tkinter.Label(text="Температура на улице")
Label1.place(x=560, y = 10)
Label2.place(x=560, y = 40)
Label3.place(x=560, y = 70)
Label4.place(x=730, y = 10)
Label5.place(x=730, y = 40)
Label6.place(x=560, y=100)

entry1 = tkinter.Entry()
entry2 = tkinter.Entry()
entry2.place(x=700, y=100)
entry2.insert(0, str(t_v))

entry1.place(x=700, y=70)
entry1.insert(0, str(t_r))
def click_button1():
    global window1
    global bool_window1
    if bool_window1 == False:
        canvas1.itemconfig(window1, fill="green")
        bool_window1 = True
    else:
        canvas1.itemconfig(window1, fill="red")
        bool_window1 = False

def click_button2():
    global window2
    global bool_window2
    if bool_window2 == False:
        canvas1.itemconfig(window2, fill="green")
        bool_window2 = True
    else:
        canvas1.itemconfig(window2, fill="red")
        bool_window2 = False

def click_button3():
    global window3
    global bool_window3
    if bool_window3 == False:
        canvas1.itemconfig(window3, fill="green")
        bool_window3 = True
    else:
        canvas1.itemconfig(window3, fill="red")
        bool_window3 = False

def click_button4():
    global window4
    global bool_window4
    if bool_window4 == False:
        canvas1.itemconfig(window4, fill="green")
        bool_window4 = True
    else:
        canvas1.itemconfig(window4, fill="red")
        bool_window4 = False

def click_button5():
    global window5
    global bool_window5
    if bool_window5 == False:
        canvas1.itemconfig(window5, fill="green")
        bool_window5 = True
    else:
        canvas1.itemconfig(window5, fill="red")
        bool_window5 = False

def click_button6():
    global door1
    global bool_door1
    if bool_door1 == False:
        canvas1.itemconfig(door1, fill="green")
        bool_door1 = True
    else:
        canvas1.itemconfig(door1, fill="red")
        bool_door1 = False

def click_button7():
    global door2
    global bool_door2
    if bool_door2 == False:
        canvas1.itemconfig(door2, fill="green")
        bool_door2 = True
    else:
        canvas1.itemconfig(door2, fill="red")
        bool_door2 = False


def click_button8():
    global door2
    global bool_regulator
    if bool_regulator == False:
        canvas1.itemconfig(regulator, fill="green")
        bool_regulator = True
    else:
        canvas1.itemconfig(regulator, fill="red")
        bool_regulator = False

bool_btn_window1 = tkinter.Button(text="окно 1", command=click_button1)
bool_btn_window2 = tkinter.Button(text="окно 2", command=click_button2)
bool_btn_window3 = tkinter.Button(text="окно 3", command=click_button3)
bool_btn_window4 = tkinter.Button(text="окно 4", command=click_button4)
bool_btn_window5 = tkinter.Button(text="окно 5", command=click_button5)
bool_btn_door1 = tkinter.Button(text="дверь 1", command=click_button6)
bool_btn_door2 = tkinter.Button(text="дверь 2", command=click_button7)
bool_btn_regulator = tkinter.Button(text="Регулятор", command=click_button8)


bool_btn_window1.place(x=510,y = 10)
bool_btn_window2.place(x=510,y = 40)
bool_btn_window3.place(x=510,y = 70)
bool_btn_window4.place(x=510,y = 100)
bool_btn_window5.place(x=510,y = 130)
bool_btn_door1.place(x=510,y = 160)
bool_btn_door2.place(x=510,y = 190)
bool_btn_regulator.place(x=510,y = 220)
canvas1.place(x=0, y=0)





def update():
    global t_p1, t_p2
    t_r = int(entry1.get())  # температура регулятора
    t_v = int(entry2.get())
    count_open_window = 0
    open_window = tp_v * (t_v - t_p1)
    # tp_v * (t_v - t_p2)
    open_door_tp_1 = tp_v * (t_p2 - t_p1)
    open_door_tp_2 = tp_v * (t_p1 - t_p2)
    open_reg = tp_v * (t_r - t_p2)

    if bool_regulator == False:
        if bool_window1 == True:
            count_open_window += 1
            if bool_door2 == True:
                t_p1 = t_p1 + (open_window + open_door_tp_1) * 5
            else:
                t_p1 = t_p1 + (open_window) * 5

        if bool_window5 == True:
            count_open_window += 1
            if bool_door2 == True:
                t_p1 = t_p1 + (open_window * count_open_window + open_door_tp_1) * 5
            else:
                t_p1 = t_p1 + (open_window * count_open_window) * 5
        if bool_door1 == True:
            count_open_window += 1
            if bool_door2 == True:
                t_p1 = t_p1 + (open_window*count_open_window + open_door_tp_1) * 5
            else:
                t_p1 = t_p1 + (open_window * count_open_window) * 5

        if bool_door2 == True:
            t_p1 = t_p1 + open_door_tp_1 * 5
            t_p2 = t_p2 + open_door_tp_2 * 5

        if bool_window2 == True:
            count_open_window += 1
            if bool_regulator == True:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2) + open_door_tp_2+open_reg) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)+open_reg) * 5
            else:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2) + open_door_tp_2) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)) * 5

        if bool_window3 == True:
            count_open_window += 1
            if bool_regulator == True:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window + open_door_tp_2+open_reg) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window+open_reg) * 5
            else:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window + open_door_tp_2) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window) * 5

        if bool_window4 == True:
            count_open_window += 1
            if bool_regulator == True:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window + open_door_tp_2+open_reg) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window+open_reg) * 5
            else:
                if bool_door2 == True:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window + open_door_tp_2) * 5
                else:
                    t_p2 = t_p2 + (tp_v * (t_v - t_p2)*count_open_window) * 5
    else:
        t_p2 = t_p2 + (tp_v * (t_r - t_p2)) * 5
        t_p1 = t_p1 + (tp_v * (t_r - t_p1)) * 5


    Label4["text"] = str(t_p1)
    Label5["text"] = str(t_p2)
    # print(count_open_window, bool_window1, bool_window5, bool_door1, bool_door2)


    print(t_p1, t_p2, t_r)
    main.after(int(1000*deltatime), update)

update()
main.mainloop()