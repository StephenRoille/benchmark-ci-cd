import platform
import random


class Colors:
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CHOICES = (VIOLET, BLUE, CYAN, GREEN, YELLOW, RED, BOLD, UNDERLINE)


if __name__ == "__main__":

    ATTRS = ("machine", "version", "platform", "system", "processor")
    print("========================================================================")
    print("======== Python Execution Script =======================================")
    print("========================================================================")
    for attr in ATTRS:
        color = random.choice(Colors.CHOICES)
        print(f"{color}{attr}{Colors.ENDC}: {getattr(platform, attr)()}")
    print("========================================================================")
