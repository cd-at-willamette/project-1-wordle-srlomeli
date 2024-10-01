########################################
# Name: Salvador Lomeli
# Collaborators (if any): Sam from the QUAD
# GenAI Transcript (if any):
# Estimated time spent (hr): 5
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import ENGLISH_WORDS, is_english_word
import random

# The main function to play the Wordle game.
def wordle():
    #Creates the answer
    mystery_word = random.choice([word for word in ENGLISH_WORDS if len(word) == 5]).upper()

    # What should happen when RETURN/ENTER is pressed.
    def enter_action():
        #Empty String for Player's Guess
        word_guessed = ""
        remaining_letters = list(mystery_word)
        def color_boxes():
            # First pass: mark correct letters
            for i in range(N_COLS):
                if word_guessed[i] == mystery_word[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    remaining_letters[i] = '*'  # Mark this letter as used
            # Second pass: mark present letters
            for i in range(N_COLS):
                if word_guessed[i] != mystery_word[i] and word_guessed[i] in remaining_letters:
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    remaining_letters[remaining_letters.index(word_guessed[i])] = '*'  # Mark this letter as used
                # Third pass: mark letters not in word
                elif word_guessed[i] != mystery_word[i]:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
        
        def change_rows():
            if word_guessed == mystery_word:
                gw.set_current_row(N_ROWS)
                gw.show_message('You Win Great Job!')
            elif gw.get_current_row() == N_ROWS - 1 and word_guessed != mystery_word:
                gw.show_message('GAME OVER THE WORDLE WAS: ' + mystery_word)
            else:
                gw.set_current_row(gw.get_current_row() + 1)

        def color_keys():
            for i in range (N_COLS):
                if gw.get_key_color(word_guessed[i]) == UNKNOWN_COLOR:
                    if word_guessed[i] == mystery_word[i]:
                        gw.set_key_color(word_guessed[i],CORRECT_COLOR)
                    elif word_guessed[i] in mystery_word:
                        gw.set_key_color(word_guessed[i],PRESENT_COLOR)                        
                    else:
                        gw.set_key_color(word_guessed[i],MISSING_COLOR)
        
        for i in range(N_COLS):
        # Obtain the player's guess
            word_guessed += gw.get_square_letter(gw.get_current_row(), i)
        # Check Guess Validity
        if is_english_word(word_guessed) and len(word_guessed) == len(mystery_word):
            gw.show_message('Great guess!')
            color_boxes()
            change_rows()
            color_keys()
        else:
            gw.show_message('Not in word list!')


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)



# Startup boilerplate
if __name__ == "__main__":
    wordle()
