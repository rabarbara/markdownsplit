import json
import re
import collections


def parse(text):
    """
    Create a json representation of the text
    """

    text_structure = []
    h2_count = 1
    for line in text.readlines():
        if line.strip().startswith('###'):
            try:
                text_structure[-1]['contents'][-1]['contents'].append(line)
            except IndexError:
                text_structure.append(line)
        elif line.strip().startswith('##'):
            name = '{}-{}'.format(h2_count, line)
            contents = []
            text_structure[-1]['contents'].append({'name': name, 'contents': contents})
            h2_count += 1
        elif line.strip().startswith('#'):
            name = '{}'.format(line)
            contents = []
            text_structure.append({'name': name, 'contents': contents})
        else:
            try:
                text_structure[-1]['contents'][-1]['contents'].append(line)
            except TypeError:
                text_structure[-1]['contents'].append(line)
            except IndexError:
                text_structure[-1]['contents'].append(line)
    return text_structure



if __name__ == '__main__':
    with open('main.md') as f:
        parse(f)
