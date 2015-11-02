from collections import deque
import random

class Markov:
    def __init__(self, ngrams):
        self.ngrams = ngrams
        self.mapping = {}

    def trainingComment(self, comment):
        words = comment.split()
        window = deque([None]*self.ngrams)

        for word in words:
            if tuple(window) not in self.mapping:
                self.mapping[tuple(window)] = set()
            self.mapping[tuple(window)].add(word)

            window.appendleft(word)
            window.pop()

        if tuple(window) not in self.mapping:
            self.mapping[tuple(window)] = set()
        self.mapping[tuple(window)].add(None)

    def generateComment(self):
        window = deque([None]*self.ngrams)
        comment = ""

        while True:
            word = random.sample(self.mapping[tuple(window)], 1)[0]

            if word == None:
                break

            comment += word + " "

            window.appendleft(word)
            window.pop()

        return comment