import pprint

import requests
from bs4 import BeautifulSoup


def sort_stories_by_votes(hn_lists):
    return sorted(hn_lists, key=lambda k: k['votes'], reverse=True)


def create_custom_news(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace('points', ''))

            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')

    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')

    pprint.pprint(create_custom_news(links, subtext))
