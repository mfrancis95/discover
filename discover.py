from argparse import ArgumentParser
from ping import ping
from socket import gethostbyaddr
from concurrent.futures import ThreadPoolExecutor

parser = ArgumentParser("discover")
parser.add_argument("--min", default = 0, type = int)
parser.add_argument("--max", default = 255, type = int)
args = parser.parse_args()

def print_ping(address):
    result = ping(address)
    if result is not None:
        print(address + " - " + gethostbyaddr(address)[0])

with ThreadPoolExecutor(16) as executor:
    executor.map(print_ping, map(lambda i: "192.168.1." + str(i), range(args.min, args.max + 1)))
