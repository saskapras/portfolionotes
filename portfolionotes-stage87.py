# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: PortfolioNotes
def compare_reports(report_a, report_b):
    keys_a = set(report_a.keys())
    keys_b = set(report_b.keys())
    only_in_a = sorted(keys_a - keys_b)
    only_in_b = sorted(keys_b - keys_a)
    common = sorted(keys_a & keys_b)
    return only_in_a, only_in_b, common

def compare_values(report_a, report_b, keys):
    results = {}
    for key in keys:
        if isinstance(report_a[key], dict) and isinstance(report_b[key], dict):
            results[key] = compare_values(report_a[key], report_b[key], report_a[key].keys())
        else:
            results[key] = report_a[key] == report_b[key]
    return results

def report_summary(report):
    total = 0.0
    for holding in report.get("holdings", []):
        total += holding.get("amount", 0) * holding.get("price", 0)
    return total
