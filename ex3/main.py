import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)


def show_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.CYAN + item.name + "/")
            show_directory(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name)


path = Path(sys.argv[1])

if not path.exists():
    print(Fore.RED + "Шлях не існує")
elif not path.is_dir():
    print(Fore.RED + "Це не директорія")
else:
    print(Fore.CYAN + path.name + "/")
    show_directory(path)
