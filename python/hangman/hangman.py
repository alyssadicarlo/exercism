# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_' * len(word)
        self.guessed_list = []

    def guess(self, char):
        if self.status == STATUS_WIN or self.status == STATUS_LOSE:
            raise ValueError(f"Game over - You {self.status}")
        if self.status == STATUS_ONGOING:
            if char in self.guessed_list:
                self.remaining_guesses -= 1
            else:
                self.guessed_list.append(char)

                count = 0
                for i in range(0, len(self.word)):
                    if self.word[i] == char:
                        self.masked_word = self.masked_word[:i] + char + self.masked_word[i+1:]
                        count += 1
                if count == 0:
                    self.remaining_guesses -= 1

            if self.word == self.masked_word:
                self.status = STATUS_WIN
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE


    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
