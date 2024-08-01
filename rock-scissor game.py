import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.choices = ['Rock', 'Paper', 'Scissors']

        # Create a frame to hold all widgets and center it in the window
        self.main_frame = tk.Frame(root)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Define font size
        self.font_size = 14

        # Widgets
        self.user_label = tk.Label(self.main_frame, text="Your Choice:", font=("Helvetica", self.font_size))
        self.user_label.grid(row=0, column=0, padx=20, pady=10)

        self.user_choice_var = tk.StringVar()
        self.user_choice_menu = tk.OptionMenu(self.main_frame, self.user_choice_var, *self.choices)
        self.user_choice_menu.config(font=("Helvetica", self.font_size))
        self.user_choice_menu.grid(row=0, column=1, padx=20, pady=10)

        self.play_button = tk.Button(self.main_frame, text="Play", command=self.play_game, font=("Helvetica", self.font_size + 2))
        self.play_button.grid(row=1, column=0, columnspan=2, pady=15)

        self.result_label = tk.Label(self.main_frame, text="", font=("Helvetica", self.font_size))
        self.result_label.grid(row=2, column=0, columnspan=2, pady=15)

        self.score_label = tk.Label(self.main_frame, text=f"Score - You: {self.user_score}, Computer: {self.computer_score}", font=("Helvetica", self.font_size))
        self.score_label.grid(row=3, column=0, columnspan=2, pady=15)

        self.play_again_button = tk.Button(self.main_frame, text="Play Again", command=self.reset_game, font=("Helvetica", self.font_size + 2))
        self.play_again_button.grid(row=4, column=0, columnspan=2, pady=15)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        if user_choice == "":
            messagebox.showwarning("Error", "Please select a choice.")
            return

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        if result == "Win":
            self.user_score += 1
            result_text = f"You Win! Computer chose {computer_choice}."
        elif result == "Lose":
            self.computer_score += 1
            result_text = f"You Lose! Computer chose {computer_choice}."
        else:
            result_text = f"It's a Draw! Both chose {computer_choice}."

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                (user_choice == "Paper" and computer_choice == "Rock") or \
                (user_choice == "Scissors" and computer_choice == "Paper"):
            return "Win"
        else:
            return "Lose"

    def reset_game(self):
        self.user_choice_var.set("")
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")  # Increase window size to accommodate larger widgets
    app = RockPaperScissors(root)
    root.mainloop()
