import numpy as np


def extract_features(url):
    features = []

    features.append(len(url))

    features.append(1 if "@" in url else 0)

    features.append(1 if "-" in url else 0)

    features.append(url.count("."))

    features.append(1 if url.startswith("https") else 0)

    # Phishing keywords
    keywords = ["login", "verify", "update", "secure", "account"]
    features.append(1 if any(k in url.lower() for k in keywords) else 0)

    return np.array(features).reshape(1, -1)
