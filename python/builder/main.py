class Computer:
    def __init__(self, serial_no):
        self.serial_no = serial_no
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        return "computer <serial no> {}\n<memory> {}\n<hdd> {}\n<gpu>{}".format(
            self.serial_no,
            self.memory,
            self.hdd,
            self.gpu)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("abc")

    def configure_hdd(self, hdd):
        self.computer.hdd = hdd

    def configure_gpu(self, gpu):
        self.computer.gpu = gpu

    def configure_memory(self, memory):
        self.computer.memory = memory


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def build(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in [self.builder.configure_gpu(gpu), self.builder.configure_hdd(hdd), self.builder.configure_memory(memory)]]

    @property
    def computer(self):
        return self.builder.computer

if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.build(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    print(engineer.computer)
    