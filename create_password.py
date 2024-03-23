import string


class CreatePassword:
    def __init__(self, address: str, number_of_passwords: int):
        self.file = open(address, 'w')
        self.number_of_passwords = number_of_passwords

    def create_password_string(self):
        self.file.seek(0)
        print('Start Generate Password...')
        words = string.printable.strip()

        if self.number_of_passwords == 2:
            return self.two(words)

        elif self.number_of_passwords == 3:
            return self.three(words)

        elif self.number_of_passwords == 4:
            return self.four(words)

        elif self.number_of_passwords == 5:
            return self.four(words)

        elif self.number_of_passwords == 6:
            return self.four(words)

        elif self.number_of_passwords == 7:
            return self.four(words)

        elif self.number_of_passwords == 8:
            return self.four(words)

        self.file.close()
        if self.number_of_passwords >= 9:
            return 'The Entered Number Must be Between 2-8'

    def two(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    if counter > 0:
                        self.file.write('\n')
                    else:
                        counter += 1
                    self.file.write(f'{word}{word2}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def three(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        if counter > 0:
                            self.file.write('\n')
                        else:
                            counter += 1
                        self.file.write(f'{word}{word2}{word3}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def four(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        for word4 in words:
                            if counter > 0:
                                self.file.write('\n')
                            else:
                                counter += 1
                            self.file.write(f'{word}{word2}{word3}{word4}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def five(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        for word4 in words:
                            for word5 in words:
                                if counter > 0:
                                    self.file.write('\n')
                                else:
                                    counter += 1
                                self.file.write(f'{word}{word2}{word3}{word4}{word5}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def six(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        for word4 in words:
                            for word5 in words:
                                for word6 in words:
                                    if counter > 0:
                                        self.file.write('\n')
                                    else:
                                        counter += 1
                                    self.file.write(f'{word}{word2}{word3}{word4}{word5}{word6}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def seven(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        for word4 in words:
                            for word5 in words:
                                for word6 in words:
                                    for word7 in words:
                                        if counter > 0:
                                            self.file.write('\n')
                                        else:
                                            counter += 1
                                        self.file.write(f'{word}{word2}{word3}{word4}{word5}{word6}{word7}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'

    def eight(self, words):
        try:
            counter = 0
            for word in words:
                for word2 in words:
                    for word3 in words:
                        for word4 in words:
                            for word5 in words:
                                for word6 in words:
                                    for word7 in words:
                                        for word8 in words:
                                            if counter > 0:
                                                self.file.write('\n')
                                            else:
                                                counter += 1
                                            self.file.write(f'{word}{word2}{word3}{word4}{word5}{word6}{word7}{word8}')
            return 'Complete...'

        except Exception as ex:
            return F'Error {ex.args}'
