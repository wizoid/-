#import tkinter as tk

#root=tk.Tk()
#root.title("Bombaster")
#root.geometry("800x500+500+200")
#root.iconbitmap("vk_logo_icon_256981.ico")
#root.resizable(False, False)

#label1 = tk.Label(text="Пшел нахуй пес!",
                  #font=("Roboto", 24, "bold"),
                 # bg="black", fg="white",
                 # width=800, height=2, padx=0, pady=0,
                  #атрибут anchor=
#"n" (север)-поднимет текст вверх; "s" (юг) – опустит текст вниз;
#"w" (запад) – разместит текст слева;"e"(восток) – текст будет размещен справа.
    #также есть тег justify.LEFT и тд. который выравнивает текст по "n" краю
                 #relief=tk.RIDGE, bd=5,
                 # )
#label1.pack()
#root.mainloop()




#                           КЛИКЕР БОМБА
import tkinter as tk
bomb = 100
score = 0
press_return = True
#Настройки окна
root = tk.Tk()
root.title("Bomb")
root.geometry("800x500+500+200")
root.iconbitmap("vk_logo_icon_256981.ico")

label = tk.Label(root, text="Press [Enter] to start", font=('Comic Sans MS', 14))
label.pack()

fuse_label = tk.Label(root, text=f"Fuse: {str(bomb)}", font=('Comic Sans MS', 14))
fuse_label.pack()

score_label = tk.Label(root, text=f"Score: {str(score)}", font=('Comic Sans MS', 14))
score_label.pack()

#Самое веселое
img1 = tk.PhotoImage(file="стасбарецкий-1.gif")
img2 = tk.PhotoImage(file="барецкий-2.gif")
img3 = tk.PhotoImage(file="барец-3.gif")
img4 = tk.PhotoImage(file="барецкий-4.gif")

bomb_label = tk.Label(image=img1)
bomb_label.pack()

# обновляем окно, помещая новые данные
def update_display():
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image=img1)
    elif 50 <= bomb < 80:
        bomb_label.config(image=img2)
    elif 0 < bomb < 50:
        bomb_label.config(image=img3)
    else:
        bomb_label.config(image=img4)
        fuse_label.config(text="Fuse: " + str(bomb))
        score_label.config(text="Score: " + str(score))
        fuse_label.after(100, update_display)

# проверяем не закончилась ли игра
def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        bomb = 0
        label.config(text="'Bang! Bang! Bang!")
        press_return = True
        return False
    else:
        return True
# реализуем таймер игры
def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)
# меняем счеt игрока
def update_score():
    global score
    if is_alive():
        score += 1
        score_label.after(3000, update_score)
# тут и так все понятно (запускаем процесс игры)
def start(event):
    global press_return
    if not press_return:
        pass
    else:
        update_bomb()
        update_score()
        update_display()
        label.config(text="")
        press_return = False

# Функция для click_button
def click():
    #global позволяет изменять переменную за пределами текущей области видимости
    global bomb
    if is_alive():
        bomb += 1
#Кнопка для продления игры
click_button = tk.Button(root, text="Click me", bg="white", fg="black",
                width=15, font=('Comic Sans MS', 14),
                command = click)
click_button.pack()

root.bind('<Return>', start)


root.mainloop()