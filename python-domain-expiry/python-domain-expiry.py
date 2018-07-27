# python-domain-expiry
# copyright Vilhelm Prytz 2018
# https://github.com/mrkakisen/misc

# json configuration path
path = "domains.json"
exportPath = "export.json"

# imports
import whois
import json
import datetime

# current time
now = datetime.datetime.now()

# print
def print_no_newline(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()

# parse
def data():
    with open(path) as f:
        j = json.load(f)

    return j["domains"]

def query(domain):
    w = whois.whois(domain)
    return w.expiration_date

if __name__ == "__main__":
    list = data()
    data = {"exportDate": str(now), "domains": []}

    x = 1
    for domain in list:
        r = query(domain)

        if r is not None:
            now = datetime.datetime.now()
            data["domains"].append({"domain": domain, "expiry": str(r), "remaining": str(r - now)})

            print("\r" + domain + " expires on " + str(r) + " which is in " + str(r - now))
            print_no_newline("\rStatus: Domain " + str(x) + " out of " + str(len(list)))

        x = x + 1

        # dump export
        with open(exportPath, "w") as outfile:
            json.dump(data, outfile)

    print("\nCompleted. Export saved as " + str(exportPath))
