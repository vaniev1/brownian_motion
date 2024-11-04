import tkinter as tk
import random

# Параметры пути
num_steps = 5000  # Уменьшено количество шагов
step_size = 30    # Увеличен размер шага

class BrownianMotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brownian Motion")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        # Начальные координаты
        self.x = self.canvas.winfo_width() // 2
        self.y = self.canvas.winfo_height() // 2

        # Рисуем начальную точку
        self.canvas.create_oval(self.x - 2, self.y - 2, self.x + 2, self.y + 2, fill="green")

        # Начинаем рисовать путь
        self.step_counter = 0
        self.draw_next_step()

    def draw_next_step(self):
        if self.step_counter < num_steps:
            # Генерируем случайное направление
            direction = random.choice([(step_size, 0), (-step_size, 0), (0, step_size), (0, -step_size)])
            self.x += direction[0]
            self.y += direction[1]

            # Ограничиваем движение в пределах канваса
            self.x = max(0, min(self.canvas.winfo_width(), self.x))
            self.y = max(0, min(self.canvas.winfo_height(), self.y))

            # Рисуем точку
            self.canvas.create_oval(self.x - 1, self.y - 1, self.x + 1, self.y + 1, fill="green")

            # Увеличиваем счётчик шагов
            self.step_counter += 1

            # Запланировать следующий шаг с меньшей задержкой
            self.root.after(5, self.draw_next_step)  # Задержка 5 мс

# Запуск приложения
root = tk.Tk()
app = BrownianMotionApp(root)
root.mainloop()
