
class string(str):
    def lwhitespace(self):
        return len(self) - len(self.lstrip())

    def ltab(self):
        if self[0] == ' ':
            return int(((len(self) - len(self.lstrip())) / 4))
        else:
            return len(self) - len(self.lstrip())
