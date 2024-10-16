import tkinter as tk
import random
import math

class DiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogue o dado!")
        self.rolling = False
        
        # Configurando a cor de fundo
        self.master.configure(bg="#8B4513")  # Cor de madeira
        
        # Título
        self.title_label = tk.Label(master, text="Jogue o dado!", font=("Arial", 24), bg="#8B4513", fg="white")
        self.title_label.pack(pady=20)
        
        # Canvas para os dados
        self.canvas = tk.Canvas(master, width=300, height=300, bg="#8B4513", highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Criando os dados (representados como círculos)
        self.dice1 = self.canvas.create_rectangle(50, 50, 100, 100, fill="white", outline="black")
        self.dice2 = self.canvas.create_rectangle(200, 50, 250, 100, fill="white", outline="black")
        
        # Botão Jogar
        self.roll_button = tk.Button(master, text="Jogar", font=("Arial", 16), command=self.roll_dice)
        self.roll_button.pack(pady=20)

    def poly_oval(self, x0, y0, x1, y1, steps=20, rotation=0):
        """return an oval as coordinates suitable for create_polygon"""
        # x0,y0,x1,y1 are as create_oval
        # rotation is in degrees anti-clockwise, convert to radians
        rotation = rotation * math.pi / 180.0

        # major and minor axes
        a = (x1 - x0) / 2.0
        b = (y1 - y0) / 2.0

        # center
        xc = x0 + a
        yc = y0 + b

        point_list = []

        # create the oval as a list of points
        for i in range(steps):
            # Calculate the angle for this step
            # 360 degrees == 2 pi radians
            theta = (math.pi * 2) * (float(i) / steps)

            x1 = a * math.cos(theta)
            y1 = b * math.sin(theta)

            # rotate x, y
            x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
            y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

            point_list.append(round(x + xc))
            point_list.append(round(y + yc))

        return point_list

    def reset_game(self):
        self.canvas.delete("all")  # Apagar todos os elementos do canvas
        self.dice1 = self.canvas.create_rectangle(50, 50, 100, 100, fill="white", outline="black")
        self.dice2 = self.canvas.create_rectangle(200, 50, 250, 100, fill="white", outline="black")
        self.rolling = False

    def roll_dice(self):
        if not self.rolling:
            self.reset_game()  # Resetar o jogo
            self.rolling = True
            self.animate_dice(0)
        else:
            print("Jogo ainda em andamento...")


    def animate_dice(self, angle):
    # Animação simples (aqui você pode adicionar a lógica de zoom e rotação)
        self.canvas.itemconfig(self.dice1, fill="black")
        self.canvas.itemconfig(self.dice2, fill="black")
        
        # Zoom effect
        center_x1 = 75
        center_y1 = 75
        center_x2 = 225
        center_y2 = 75
        for i in range(10):
            self.canvas.scale(self.dice1, center_x1, center_y1, 1.1, 1.1)
            self.canvas.scale(self.dice2, center_x2, center_y2, 1.1, 1.1)
            self.master.update_idletasks()
            self.master.after(50)
        
        # Rotation effect (using itemconfig to update the dice's appearance)
        for i in range(10):
            self.canvas.itemconfig(self.dice1, fill="black" if i % 2 == 0 else "white")
            self.canvas.itemconfig(self.dice2, fill="black" if i % 2 == 0 else "white")
            self.master.update_idletasks()
            self.master.after(50)
        
        # Atualizar a cor dos dados após um pequeno delay (simulando a rolagem)
        self.master.after(1000, self.update_dice)
        
    def draw_dice_points(self, number, canvas, x, y):
        # Desenhar os pontos do dado
        points = []
        if number == 1:
            points.append((x + 25, y + 25))
        elif number == 2:
            points.append((x + 0, y + 0))
            points.append((x + 50, y + 50))
        elif number == 3:
            points.append((x - 10, y - 10))
            points.append((x + 25, y + 25))
            points.append((x + 60, y + 60))
        elif number == 4:
            points.append((x - 20, y - 20))
            points.append((x - 20, y + 60))
            points.append((x + 60, y - 20))
            points.append((x + 60, y + 60))
        elif number == 5:
            points.append((x - 20, y - 20))
            points.append((x - 20, y + 60))
            points.append((x + 20, y + 20))
            points.append((x + 60, y - 20))
            points.append((x + 60, y + 60))
        elif number == 6:
            points.append((x - 20, y - 20))#CE
            points.append((x - 20, y + 60))#BE
            points.append((x + 60, y - 20))#CD
            points.append((x + 60, y + 60))#BD
            points.append((x - 20, y + 20))#ME
            points.append((x + 60, y + 20))#MD

        for point in points:
            self.canvas.create_oval(point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5, fill="black")

    def update_dice(self):
        # Atualizando a cor dos dados e mostrando o resultado
        self.canvas.itemconfig(self.dice1, fill="white")
        self.canvas.itemconfig(self.dice2, fill="white")
        
        # Desenhar os pontos dos dados
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        self.draw_dice_points(number1, self.canvas, 55, 55)
        self.draw_dice_points(number2, self.canvas, 205, 55)
        
        print(f"Dado 1: {number1}, Dado 2: {number2}")
        
        self.rolling = False
        self.roll_button.config(state="normal")

# Criação da janela principal
root = tk.Tk()
game = DiceGame(root)
root.mainloop()