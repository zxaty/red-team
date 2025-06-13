import subprocess

def scan(target):
    result = subprocess.run(["nmap", "-Pn", target], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    scan("127.0.0.1")