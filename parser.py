#!/usr/bin/env python
import json
import os.path
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

FLASK_VERSIONS = ('2.1.x', '2.0.x', '1.1.x', '1.0.x', '0.12.x')
FLASK_DOCS_URL = 'https://flask.palletsprojects.com/en/{version}/'
EXCLUDED_IDS = {'index-', 'module-'}


def parse():
    entries = []

    for version in FLASK_VERSIONS:
        with open(os.path.abspath(os.path.join('docs', 'genindex.html')), 'r') as genindex:
            index_soup = BeautifulSoup(genindex, 'lxml')

            for table in index_soup.find_all('table', class_='genindextable'):
                for a in table.find_all('a'):
                    href = a.get('href')
                    file, id = href.split('#')

                    if any(id.startswith(pattern) for pattern in EXCLUDED_IDS):
                        continue

                    with open(os.path.abspath(os.path.join('docs', file))) as html:
                        try:
                            topic_soup = BeautifulSoup(html, 'lxml')
                            topic = topic_soup.find(id=id)
                            parent = topic.parent

                            entry_data = {
                                'version': float(version.replace('.x', '')),
                                'id': id,
                                'title': '',
                                'permalink': urljoin(FLASK_DOCS_URL.format(version=version),
                                                     href.replace('.html', '/')),
                                'categories': [],
                                'default': '',
                                'content': '',
                                'weight': 1 if id.startswith('flask.') else 2,
                            }

                            # set the title
                            if any(character.isupper() for character in id):
                                entry_data['title'] = id[re.search('[A-Z]', id).start():]
                            else:
                                if topic.find(class_='descclassname'):
                                    entry_data['title'] += topic.find(class_='descclassname').get_text()
                                if topic.find(class_='descname'):
                                    entry_data['title'] += topic.find(class_='descname').get_text()
                                if parent.get('class') == 'glossary docutils':
                                    entry_data['title'] += topic.get_text()
                            # set the content
                            if parent.find('dd').find('p'):
                                entry_data['content'] = ' '.join(parent.find('dd').find('p').get_text().split())
                            # set the categories
                            if topic.find(class_='property'):
                                property_value = topic.find(class_='property').get_text().strip()
                                if property_value.startswith('='):
                                    entry_data['default'] = ' '.join(property_value.replace('=', '').split())
                                else:
                                    entry_data['categories'].append(property_value)
                            if id.startswith('flask.'):
                                entry_data['categories'] += id.split('.')[1:-1]

                            entries.append(entry_data)
                        except Exception:
                            print(href)
                            print(parent.name)
                            raise

    if entries:
        with open(os.path.abspath('data.json'), 'w') as fh:
            json.dump(entries, fh, indent=4)


if __name__ == '__main__':
    parse()
