import requests
import sys

def getDistrowatch():
    r = requests.get("https://distrowatch.com/random.php")

    if r.status_code == requests.codes.ok:
        raw = r.text

        return(raw.split("\n")[1].split(":")[1].split("<")[0])
    else:
        print("Error contacting distrowatch")

for _ in range(int(sys.argv[1])):
    print(getDistrowatch())
