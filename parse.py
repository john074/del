import re
import csv
from collections import Counter

LOG_FILE = "kernel.log"

patterns = {
    "GENERAL_PROTECTION_FAULT": re.compile(r"GENERAL PROTECTION FAULT"),
    "DOUBLE_FAULT": re.compile(r"DOUBLE FAULT"),
    "PAGE_FAULT": re.compile(r"Page Fault"),
    "STACK_SEGMENT_FAULT": re.compile(r"STACK SEGMENT FAULT"),
    "SEGMENT_NOT_PRESENT": re.compile(r"SEGMENT NOT PRESENT"),
}

def parse_log(file_path):
    counter = Counter()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            for error_type, pattern in patterns.items():
                if pattern.search(line):
                    counter[error_type] += 1

    return counter

def save_to_csv(stats, filename="kernel_error_stats"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ErrorType", "Count"])
        for k, v in stats.items():
            writer.writerow([k, v])

def main():
    stats = parse_log(LOG_FILE)
    save_to_csv(stats)

    print("Error statistics:")
    total = sum(stats.values())

    for error, count in stats.items():
        percent = (count / total * 100) if total > 0 else 0
        print(f"{error}: {count} ({percent:.2f}%)")

    print(f"\nTotal errors: {total}")


if __name__ == "__main__":
    main()
