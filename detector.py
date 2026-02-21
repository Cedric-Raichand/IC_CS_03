def rule_based_check(url):
    risk_score = 0
    reasons = []

    if len(url) > 75:
        risk_score += 1
        reasons.append("Long URL")

    if "@" in url:
        risk_score += 1
        reasons.append("Contains @ symbol")

    if "-" in url:
        risk_score += 1
        reasons.append("Hyphenated domain")

    if url.count(".") > 3:
        risk_score += 1
        reasons.append("Multiple subdomains")

    keywords = ["login", "verify", "update", "secure", "account"]
    if any(k in url.lower() for k in keywords):
        risk_score += 1
        reasons.append("Contains phishing keywords")

    if not url.startswith("https"):
        risk_score += 1
        reasons.append("No HTTPS encryption")

    if risk_score >= 3:
        status = "SUSPICIOUS"
    else:
        status = "LIKELY SAFE"

    return status, risk_score, reasons