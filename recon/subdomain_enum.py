import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    if response.ok:
        entries = {entry['name_value'] for entry in response.json()}
        return sorted(entries)
    return []

if __name__ == "__main__":
    domain = "example.com"
    subs = get_subdomains(domain)
    for s in subs:
        print(s)