import tkinter as tk
import random as rand


def swap(two):
    t = two[0]
    two[0] = two[1]
    two[1] = t


def game_logic():
    if grids[1][1]["text"] != empty:

        back_slash = (grids[0][0]["text"] == grids[1][1]["text"]) and (
            grids[1][1]["text"] == grids[2][2]["text"])
        slash = (grids[0][2]["text"] == grids[1][1]["text"]) and (
            grids[1][1]["text"] == grids[2][0]["text"])
        middle_column = (grids[0][1]["text"] == grids[1][1]["text"]) and (
            grids[1][1]["text"] == grids[2][1]["text"])
        middle_row = (grids[1][0]["text"] == grids[1][1]["text"]) and (
            grids[1][1]["text"] == grids[1][2]["text"])

        if (slash or back_slash) or (middle_column or middle_row):
            return grids[1][1]["text"]

    elif grids[0][0]["text"] != empty:

        up = (grids[0][0]["text"] == grids[0][1]["text"]) and (
            grids[0][0]["text"] == grids[0][2]["text"])
        left = (grids[0][0]["text"] == grids[1][0]["text"]) and (
            grids[0][0]["text"] == grids[2][0]["text"])

        if up or left:
            return grids[0][0]["text"]

    elif grids[2][2]["text"] != empty:

        down = (grids[2][0]["text"] == grids[2][2]["text"]) and (
            grids[2][2]["text"] == grids[2][1]["text"])
        right = (grids[0][2]["text"] == grids[2][2]["text"]) and (
            grids[2][2]["text"] == grids[1][2]["text"])

        if down or right:
            return grids[2][2]["text"]

    return empty


def switch(i, j):
    b = grids[i][j]
    if b["state"] == "normal" or b["state"] == "active":
        b["state"] = "disabled"
        b["text"] = marker[0]
        winner = game_logic()
        if winner != empty:
            print(f"The winner is {marker[0]}")
        else:
            swap(marker)

def initialization():
    # if rand.choice([True, False]):
    #     swap(marker)

    root.resizable(False, False)
    root.title('Tic Tac Toe')
    padx, pady = 12, 12
    for i in range(0, 3):
        g = []
        for j in range(0, 3):
            b = tk.Button(root, text=empty, width=2, height=2,
                          command=lambda i=i, j=j: switch(i, j))
            b.grid(row=i, column=j, padx=padx, pady=pady)
            g.append(b)
        grids.append(g)


root = tk.Tk()
grids = []
empty = "  "
marker = ['o', 'x']


if __name__ == "__main__":
    initialization()
    root.mainloop()
