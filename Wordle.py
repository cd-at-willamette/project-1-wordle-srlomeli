########################################
# Name: Salvador Lom
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        word_guessed = ""
        for i in range(N_COLS):
            letter = gw.get_square_letter(gw.get_current_row(), i)
            word_guessed += letter

        if word_guessed.lower() in ENGLISH_WORDS:
            gw.show_message("Great guess!")
        else:
             gw.show_message("Not in word list!")



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
