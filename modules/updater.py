from console.utils import set_title
from colorama import Fore,init
from requests import get
from time import sleep
init(autoreset=True)
red = Fore.RED
cyan = Fore.CYAN
reset = Fore.RESET

def check():
    set_title("Calani AIO | Checking For Updates | MickeyYe#0003")
    print(f"    [{cyan}>{reset}] Checking for updates")
    try:
        v = repr(get("https://raw.githubusercontent.com/Mickey758/Calani-AIO/master/version").text.rstrip())
        if v != "0.1.5-alpha":
            return False
        else:
            return True
    except:
        print(f"    [{red}>{reset}] Could not connect to update server")
        sleep(2)
        return False