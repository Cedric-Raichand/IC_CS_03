import re
import requests
from urllib.parse import urlparse

# suspicious keywords attackers love
SUSPICIOUS_WORDS = [
    "login", "verify", "account", "secure", "update",
    "bank", "paypal", "password", "confirm"
]

def has_ip_address(url):
    return bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))

def has_at_symbol(url):
    return "@" in url

def is_long_url(url):
    return len(url) > 75

def has_many_subdomains(url):
    domain = urlparse(url).netloc
    return domain.count('.') > 3

def has_hyphen(domain):
    return "-" in domain

def has_suspicious_words(url):
    url = url.lower()
    return any(word in url for word in SUSPICIOUS_WORDS)

def has_https(url):
    try:
        response = requests.get(url, timeout=5)
        return response.url.startswith("https")
    except:
        return False

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = {
        "ip_address": has_ip_address(url),
        "at_symbol": has_at_symbol(url),
        "long_url": is_long_url(url),
        "many_subdomains": has_many_subdomains(url),
        "hyphen_domain": has_hyphen(domain),
        "suspicious_words": has_suspicious_words(url),
        "https": has_https(url)
    }

    return features
