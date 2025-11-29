import requests

def shorten_url(url: str) -> str:
    """Shorten a URL using TinyURL API."""
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Could not shorten the URL."

def main():
    print("Simple URL Shortener")
    url = input("Enter the URL to shorten: ").strip()
    short_url = shorten_url(url)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
