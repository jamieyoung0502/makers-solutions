class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        no_vowels = ''
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                no_vowels += self.text[i]
            i += 1
        return no_vowels


remover = VowelRemover("aebioud")
result_no_vowels = remover.remove_vowels()