def my_adder(x, y):
    return x + y


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    """返回句子字母数量"""
    def letter_count(self):
        return len(self.sentence)

    """返回句子单词数量"""
    def word_count(self):
        return len(self.sentence.split(" "))

    """返回所有字母大写后的句子"""
    def upper(self):
        return self.sentence.upper()
