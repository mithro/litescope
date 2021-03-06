class LiteScopeIODriver():
    def __init__(self, regs, name):
        self.regs = regs
        self.name = name
        self.build()

    def build(self):
        self.input = getattr(self.regs, self.name + "_in")
        self.output = getattr(self.regs, self.name + "_out")

    def write(self, value):
        self.output.write(value)

    def read(self):
        return self.input.read()
