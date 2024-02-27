import tkinter as tk
import random as rand


def swap(two):
    t = two[0]
    two[0] = two[1]
    two[1] = t


def game_logic():

    a, b, c = grids[0][0]["text"], grids[0][1]["text"], grids[0][2]["text"]
    d, e, f = grids[1][0]["text"], grids[1][1]["text"], grids[1][2]["text"]
    g, h, i = grids[2][0]["text"], grids[2][1]["text"], grids[2][2]["text"]

    back_slash = (e != empty) and (a == e) and (e == i)
    if back_slash:
        grids[0][0].configure(bg="red")
        grids[1][1].configure(bg="red")
        grids[2][2].configure(bg="red")
        return e

    slash = (e != empty) and (c == e) and (e == g)
    if slash:
        grids[0][2].configure(bg="red")
        grids[1][1].configure(bg="red")
        grids[2][0].configure(bg="red")
        return e

    middle_column = (e != empty) and (b == e) and (e == h)
    if middle_column:
        grids[0][1].configure(bg="red")
        grids[1][1].configure(bg="red")
        grids[2][1].configure(bg="red")
        return e

    middle_row = (e != empty) and (d == e) and (e == f)
    if middle_row:
        grids[1][0].configure(bg="red")
        grids[1][1].configure(bg="red")
        grids[1][2].configure(bg="red")
        return e

    up = (a != empty) and (a == b) and (a == c)
    if up:
        grids[0][0].configure(bg="red")
        grids[0][1].configure(bg="red")
        grids[0][2].configure(bg="red")
        return a

    left = (a != empty) and (a == d) and (a == g)
    if left:
        grids[0][0].configure(bg="red")
        grids[1][0].configure(bg="red")
        grids[2][0].configure(bg="red")
        return a

    down = (i != empty) and (g == i) and (i == h)
    if down:
        grids[2][0].configure(bg="red")
        grids[2][2].configure(bg="red")
        grids[2][1].configure(bg="red")
        return i

    right = (i != empty) and (c == i) and (i == f)
    if right:
        grids[0][2].configure(bg="red")
        grids[2][2].configure(bg="red")
        grids[1][2].configure(bg="red")
        return i

    return empty


def end_game():
    for g in grids:
        for i in g:
            if i["state"] != "disabled":
                i["state"] = "disabled"


def switch(i, j):
    b = grids[i][j]
    if b["state"] == "normal" or b["state"] == "active":
        b["state"] = "disabled"
        b["text"] = marker[0]
        winner = game_logic()
        if winner == empty:
            swap(marker)
        else:
            print(f"The winner is {marker[0]}")
            end_game()


def initialization():
    if rand.choice([True, False]):
        swap(marker)

    black = "black"
    white = "white"
    gray = "gray"
    default_font = ("Helvetica", 50)

    root.resizable(False, False)
    root.title('Tic Tac Toe')
    padx, pady = 8, 8
    for i in range(0, 3):
        g = []
        for j in range(0, 3):
            b = tk.Button(
                root,
                text=empty,
                font=default_font,
                bg=white,
                fg=black,
                command=lambda i=i, j=j: switch(i, j)
            )
            b.grid(row=i, column=j, padx=padx, pady=pady)
            g.append(b)
        grids.append(g)


root = tk.Tk()
grids = []
empty = "    "
o = ' o '
x = ' x '
marker = [' o ', ' x ']


if __name__ == "__main__":
    initialization()
    root.mainloop()
