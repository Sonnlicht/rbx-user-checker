import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from rich.console import Console

console = Console()

# put proxy here.
proxy = {
    "http": "1.1.1.1:1111", 
}

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.mount("http://", HTTPAdapter(max_retries=retries))

try:
    with open("input/username.txt", "r", encoding="utf-8", errors="ignore") as file:
        usernames = [line.strip() for line in file if line.strip()]
except Exception as e:
    console.print(f"Error reading username.txt: {e}", style="bold red")
    usernames = []


for username in usernames:
    url = f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=2000-01-01"
    try:
        response = session.get(url, proxies=proxy, timeout=10)
        data = response.json()
        if data["code"] == 0:
            console.print(f"{username} is available!", style="bold green")
            with open("output/untaken.txt", "a", encoding="utf-8") as untaken_file:
                untaken_file.write(f"{username}\n")
        else:
            console.print(f"{username} is taken. Reason: {data['message']}", style="bold red")
    except Exception as e:
        console.print(f"Skipping {username} due to error: {e}", style="bold yellow")