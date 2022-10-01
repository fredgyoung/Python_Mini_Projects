

INPUT_FILE = 'input.csv'
OUTPUT_FILE = 'output.json'


class App:

    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file
        self.output_file = output_file
        self.csv_data = None
        self.json_data = None

    def read_input_file(self):
        with open(self.input_file) as file:
            self.csv_data = file.read()

    def convert(self):
        self.json_data = self.csv_data

    def write_output_file(self):
        with open(self.output_file, 'w') as file:
            file.write(self.json_data)

    def go(self):
        self.read_input_file()
        self.convert()
        self.write_output_file()


if __name__ == '__main__':
    app = App(INPUT_FILE, OUTPUT_FILE)
    app.go()
