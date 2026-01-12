import re
import json
import csv
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description="Threat Intelligence Aggregator")
parser.add_argument("--data", default="data", help="Path to threat intel feeds directory")
args = parser.parse_args()

DATA_DIR = args.data


ioc_sources = defaultdict(set)


def classify_ioc(ioc):
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ioc):
        return "ip"
    elif ioc.startswith("http"):
        return "url"
    elif re.match(r"^[a-fA-F0-9]{32,64}$", ioc):
        return "hash"
    else:
        return "domain"


def process_txt(file, source):
    with open(file, "r") as f:
        for line in f:
            ioc = line.strip()
            if ioc:
                ioc_sources[ioc].add(source)

def process_csv(file, source):
    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ioc = row.get("indicator")
            if ioc:
                ioc_sources[ioc].add(source)

def process_json(file, source):
    with open(file, "r") as f:
        data = json.load(f)
        for ioc in data.get("indicators", []):
            if ioc:
                ioc_sources[ioc].add(source)


def severity(count):
    if count >= 3:
        return "HIGH"
    elif count == 2:
        return "MEDIUM"
    else:
        return "LOW"


process_txt(f"{DATA_DIR}/feed1.txt", "feed1.txt")
process_csv(f"{DATA_DIR}/feed2.csv", "feed2.csv")
process_json(f"{DATA_DIR}/feed3.json", "feed3.json")


outputs = {
    "ip": [],
    "domain": [],
    "url": [],
    "hash": []
}

for ioc, sources in ioc_sources.items():
    count = len(sources)
    ioc_type = classify_ioc(ioc)
    sev = severity(count)
    srcs = ", ".join(sorted(sources))
    outputs[ioc_type].append(
        f"{ioc} | sources: {srcs} | occurrences: {count} | severity: {sev}"
    )


for ioc_type, values in outputs.items():
    with open(f"output/malicious_{ioc_type}s.txt", "w") as f:
        for v in values:
            f.write(v + "\n")


with open("output/normalized_iocs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IOC", "Type", "Occurrences", "Severity", "Sources"])

    for ioc, sources in ioc_sources.items():
        count = len(sources)
        ioc_type = classify_ioc(ioc)
        sev = severity(count)
        writer.writerow([ioc, ioc_type, count, sev, ", ".join(sorted(sources))])

with open("output/high_risk_iocs.txt", "w") as f:
    for ioc, sources in ioc_sources.items():
        if len(sources) >= 2:
            f.write(f"{ioc} | sources: {', '.join(sources)}\n")



print("[+] Aggregation complete")
print(f"[+] Total IOCs processed: {len(ioc_sources)}")
