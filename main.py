from packages.cpu.cpu import CPU
from packages.gpu.gpu import GPU

if __name__ == "__main__":
    cpu = CPU()
    gpu = GPU()
    cpu.update_display("Hello Project")
