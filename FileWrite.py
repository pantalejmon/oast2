import os

class FileWriter:
    def __init__(self,nm):
        if not os.path.exists('results'):
            os.makedirs('results')
        self.result_file = open('results/'+nm+'.txt', "w+")

    def write(self, line):
        self.result_file.write(line+'\n')

    def write_add_to_line(self, line):
        self.result_file.write(line)

    def close(self):
        self.result_file.close()
