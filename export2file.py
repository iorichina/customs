class export2file():
    def init(self, filename):
        self.filename = open(filename, "w", encoding='utf-8')

    def write(self, str):
        # print('write', str)
        self.filename.write(str)

    def close(self):
        self.filename.flush()
        self.filename.close()
