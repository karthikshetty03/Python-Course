import requests as r
from dataclasses import dataclass


@dataclass
class Quote:
    quote: str
    author: str


def get_quote(uri: str) -> Quote:
    response: r.Response = r.get(url=uri)
    data: dict = response.json()
    content: str = data.setdefault('content', '...')
    author: str = data.setdefault('author', '...')
    return Quote(quote=content, author=author)


if __name__ == '__main__':
    url: str = 'https://api.quotable.io/random'
    for i in range(3):
        quote: Quote = get_quote(uri=url)
        print('Quote', quote.quote)
        print('Author', quote.author)
        print()
