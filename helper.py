import requests
def get_input(day, session):
    cookies = {"session": session}
    response = requests.get(f"https://adventofcode.com/2024/day/{day}/input",cookies=cookies)
    if response.status_code == 200:
        return response.text

if __name__ == "__main__":
    print(get_input(1, session=""))