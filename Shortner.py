import requests
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """Check if the given string is a valid URL."""
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def shorten_url(url: str, timeout: float = 5.0) -> str:
    """
    Shorten a URL using the TinyURL API.
    Includes error handling and timeout.
    """
    if not is_valid_url(url):
        return "Error: Invalid URL format."

    api_url = "https://tinyurl.com/api-create.php"
    params = {"url": url}

    try:
        response = requests.get(api_url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    print("🔗 Simple URL Shortener")
    url = input("Enter the URL to shorten: ").strip()

    short_url = shorten_url(url)
    print(f"➡ Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
