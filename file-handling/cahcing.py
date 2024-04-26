import json
import requests


def fetch_data(*, update: bool = False, json_cache: str, url: str):
    if update:
        json_data = None
    else:
        try:
            with open(json_cache, "r") as file:
                json_data = json.load(file)
                print("Data loaded from cache")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Cache file not found or invalid: {e}")
            json_data = None

    if not json_data:
        print("Fetching data from the server")
        json_data = requests.get(url).json()
        with open(json_cache, "w") as file:
            json.dump(json_data, file, indent=2)
            print("Data saved to cache")
    return json_data


if __name__ == "__main__":
    api_url = 'https://dummyjson.com/comments'
    json_cache_file = 'comments.json'
    data = fetch_data(update=False, json_cache=json_cache_file, url=api_url)
    # data = fetch_data(update=True, json_cache=json_cache_file, url=api_url)
    print(data)
