class export2file():
    def init(self, filename, codestyle):
        self.codestyle = codestyle
        self.filename = open(filename, "w", encoding=codestyle)

    def write(self, strval):
        # print('write', strval, strval.encode(
        #     self.codestyle, 'ignore').decode(self.codestyle))
        self.filename.write(strval.encode(
            self.codestyle, 'ignore').decode(self.codestyle))

    def close(self):
        self.filename.flush()
        self.filename.close()
