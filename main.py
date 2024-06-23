import tkinter as tk
import random


class PlayYourCardsRight:

  def __init__(self, root):
    self.root = root
    self.root.geometry("800x500")
    self.root.configure(bg="green")
    self.root.title("Play your cards right!")

    self.score = 0
    self.current_card = ""

    self.create_main_menu()

  def create_main_menu(self):
    self.main_frame = tk.Frame(self.root, bg="green")
    self.main_frame.pack(fill='both', expand=True)

    self.label1 = tk.Label(
        self.main_frame,
        text="Play your cards right!",
        font=('Arial', 18),
        fg="white",
        bg="green",
    )
    self.label1.pack(pady=(30, 0))

    self.button_start = tk.Button(self.main_frame,
                                  text="Start game",
                                  font=('Arial', 18),
                                  fg="green",
                                  command=self.start_game)
    self.button_start.pack(pady=(80, 20))

    self.button_instructions = tk.Button(self.main_frame,
                                         text="Instructions",
                                         font=('Arial', 18),
                                         fg="green",
                                         command=self.show_instructions)
    self.button_instructions.pack()

  def show_instructions(self):
    self.main_frame.pack_forget()

    self.instructions_frame = tk.Frame(self.root, bg="green")
    self.instructions_frame.pack(fill='both', expand=True)

    label2 = tk.Label(self.instructions_frame,
                      text="How to play:",
                      font=('Arial', 18),
                      fg="green")
    label2.pack(pady=10)

    text_instructions = tk.Text(self.instructions_frame,
                                height=7,
                                width=57,
                                fg="green")
    text_instructions.pack(pady=20)
    text_instructions.insert(
        tk.END,
        "You need to predict whether the next number will be higher or lower than the first number. If the prediction is correct, the next number is revealed, and you continue to make predictions for each subsequent number. If a prediction is incorrect, you lose your progress."
    )
    text_instructions.config(state=tk.DISABLED)

    button_back = tk.Button(self.instructions_frame,
                            text="Back",
                            font=('Arial', 18),
                            fg="green",
                            command=self.back_to_main)
    button_back.pack(pady=(20, 20))

  def back_to_main(self):
    self.instructions_frame.pack_forget()
    self.main_frame.pack(fill='both', expand=True)

  def restart_game(self):
    self.game_frame.pack_forget()
    self.main_frame.pack(fill='both', expand=True)

  def start_game(self):
    self.main_frame.pack_forget()

    self.game_frame = tk.Frame(self.root, bg="green")
    self.game_frame.pack(fill='both', expand=True)

    self.deck = list(range(2, 15)) * 4
    random.shuffle(self.deck)
    self.current_card = self.deck.pop()

    label3 = tk.Label(self.game_frame,
                      text="H = Higher L = Lower",
                      font=('Arial', 18),
                      fg="green")
    label3.pack(pady=10)

    self.text_current_card = tk.Label(self.game_frame,
                                      height=4,
                                      width=20,
                                      font=('Arial', 10))
    self.text_current_card.pack(pady=60)
    self.text_current_card.config(
        text=f"The current card is: {self.current_card}")

    self.guess_entry = tk.Entry(self.game_frame, width=2, font=('Arial', 18))
    self.guess_entry.pack(pady=10)

    self.button_check = tk.Button(self.game_frame,
                                  text="Check",
                                  font=('Arial', 18),
                                  fg="green",
                                  command=self.check_guess)
    self.button_check.pack(pady=(80, 20))

  def check_guess(self):
    next_card = self.deck.pop()
    guess = self.guess_entry.get().lower()

    if (guess == "h" and next_card > self.current_card) or (
        guess == "l" and next_card < self.current_card):
      self.current_card = next_card
      self.text_current_card.config(
          text=f"The current card is: {self.current_card}")
      self.guess_entry.delete(0, tk.END)
      self.score += 1

    else:
      self.end_game()

  def end_game(self):
    self.guess_entry.destroy()
    self.button_check.destroy()
    text_wrong_guess = tk.Label(
        self.game_frame,
        text=f"Wrong guess! Game over. Your score was {self.score}!",
        font=('Arial', 20),
        height=2,
        width=60,
        fg="red",
        bg="black")
    text_wrong_guess.pack()
    button_back2 = tk.Button(self.game_frame,
                             text="Back",
                             font=('Arial', 18),
                             fg="green",
                             command=self.restart_game)
    button_back2.pack(pady=(20, 20))
    self.score = 0


if __name__ == "__main__":
  root = tk.Tk()
  game = PlayYourCardsRight(root)
  root.mainloop()
