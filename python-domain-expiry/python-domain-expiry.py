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

    for domain in list:
        r = query(domain)
        if r is not None:
            now = datetime.datetime.now()
            data["domains"].append({"domain": domain, "expiry": str(r), "remaining": str(r - now)})

            print(domain + " expires on " + str(r) + " which is in " + str(r - now))


        # dump export
        with open(exportPath, "w") as outfile:
            json.dump(data, outfile)
