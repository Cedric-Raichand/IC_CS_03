from url_features import extract_features

def rule_based_detection(url):
    features = extract_features(url)

    score = 0
    reasons = []

    if features["ip_address"]:
        score += 2
        reasons.append("Uses IP address instead of domain")

    if features["at_symbol"]:
        score += 2
        reasons.append("Contains @ symbol")

    if features["long_url"]:
        score += 1
        reasons.append("URL is unusually long")

    if features["many_subdomains"]:
        score += 2
        reasons.append("Too many subdomains")

    if features["hyphen_domain"]:
        score += 1
        reasons.append("Hyphenated domain")

    if features["suspicious_words"]:
        score += 2
        reasons.append("Contains phishing keywords")

    if not features["https"]:
        score += 2
        reasons.append("No HTTPS encryption")

    # decision thresholds
    if score >= 6:
        verdict = "PHISHING"
    elif score >= 3:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return verdict, score, reasons
