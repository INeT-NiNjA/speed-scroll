import os
try:
    os.system('clear')
except Exception:
    os.system('cls')
try:
    import speedtest
    from colorama import Fore
except ImportError:
    print(" [Seems like some required packages are missing]")
    print()
    print(' Use the following command:')
    print()
    print(" pip install -r requirements.txt")
    quit()

test = speedtest.Speedtest()

print(' • INeT-NiNjA/speed-scroll •')
print()
print(Fore.CYAN + " Loading available servers...")
print()
test.get_servers()

print(' Choosing best server...')
print()
best = test.get_best_server()
print(Fore.GREEN + ' Server located')
print()
print(Fore.BLUE + ' Performing speed tests...')

dl = test.download()
ul = test.upload()
ping = test.results.ping

print(Fore.MAGENTA)
print(f" Download speed: {dl /1024 /1024:.2f} MB/s")
print(f" Upload speed: {ul /1024 /1024:.2f} MB/s" )
print(f" Ping: {ping:.2f} ms" )
