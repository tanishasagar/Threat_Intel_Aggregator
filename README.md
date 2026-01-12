# Threat Inteligence Aggregator
Threat intelligence aggregation and analysis project built during a cybersecurity internship.

## Overview
This project is a **threat intelligence aggregation and analysis tool** developed during a cybersecurity internship.  
It collects Indicators of Compromise (IOCs) from multiple threat intelligence sources, normalizes them, and generates a consolidated output for analysis.

The main goal of this project is to understand how raw threat data from different sources can be combined and filtered to identify high-risk indicators efficiently.

---

## Features
- Aggregates threat intelligence from multiple data sources  
- Extracts and normalizes IOCs such as IPs, domains, URLs, and hashes  
- Identifies high-risk indicators appearing across multiple sources  
- Generates structured output files for further investigation  
- Simple and modular Python implementation  

---

## Project Structure
Threat_Intel_Aggregator/
│
├── data/
│ ├── feed1.txt # Threat intelligence feed in text format
│ ├── feed2.csv # Threat intelligence feed in CSV format
│ └── feed3.json # Threat intelligence feed in JSON format
│
├── output/
│ ├── high_risk_iocs.txt
│ ├── malicious_domains.txt
│ ├── malicious_hashes.txt
│ ├── malicious_ips.txt
│ ├── malicious_urls.txt
│ └── normalized_iocs.csv
│
├── reports/
│ └── Threat_Intel_Aggregator_Report.docx
│
├── aggregator.py # Main aggregation and normalization script
├── .gitattributes
├── README.md
└── LICENSE



---

## Tools & Technologies
- Python 3  
- Public threat intelligence feeds  
- Windows Command Line  
- Git & GitHub for version control  

---

## How It Works
1. Threat intelligence data is collected from different sources.  
2. The data is parsed and normalized into a common format.  
3. IOCs appearing in multiple sources are flagged as higher risk.  
4. Final results are written to output files for analysis and reporting.  

---

## Usage
Run the main script from the project root:

Make sure the input data is placed inside the `data/` directory before execution.

---

## Learning Outcomes
- Hands-on experience with threat intelligence aggregation  
- Understanding of IOC correlation and risk prioritization  
- Improved Python scripting and data handling skills  
- Exposure to real-world SOC-style analysis workflows  

---

## Documentation
Detailed static and dynamic analysis screenshots are included in the project report.

---

## Disclaimer
This project is intended strictly for **educational and research purposes**.  
All threat intelligence data used in this project is sourced from publicly available feeds.

---

## License
This project is licensed under the **MIT License**.


