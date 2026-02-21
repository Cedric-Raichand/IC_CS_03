import numpy as np


def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # Contains @
    features.append(1 if "@" in url else 0)

    # Contains hyphen
    features.append(1 if "-" in url else 0)

    # Dot count
    features.append(url.count("."))

    # HTTPS
    features.append(1 if url.startswith("https") else 0)

    # Phishing keywords
    keywords = ["login", "verify", "update", "secure", "account"]
    features.append(1 if any(k in url.lower() for k in keywords) else 0)

    return np.array(features).reshape(1, -1)