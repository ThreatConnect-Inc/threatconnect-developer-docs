"""Ensure the number of code-blocks shown on the docs page matches the number of code-blocks in the rst files."""
import os
import re

import bs4
import requests

mappings = {
    'https://docs.threatconnect.com/en/latest/rest_api/change_log.html': './docs/rest_api/change_log.rst',
    'https://docs.threatconnect.com/en/latest/rest_api/quick_start.html': './docs/rest_api/quick_start.rst',
    'https://docs.threatconnect.com/en/latest/rest_api/overview.html': './docs/rest_api/overview.rst',
    'https://docs.threatconnect.com/en/latest/rest_api/associations/associations.html': './docs/rest_api/associations/',
    'https://docs.threatconnect.com/en/latest/rest_api/attributes/attributes.html': './docs/rest_api/attributes/',
    'https://docs.threatconnect.com/en/latest/rest_api/groups/groups.html': './docs/rest_api/groups/',
    'https://docs.threatconnect.com/en/latest/rest_api/indicators/indicators.html': './docs/rest_api/indicators/',
    'https://docs.threatconnect.com/en/latest/rest_api/owners/owners.html': './docs/rest_api/owners/',
    'https://docs.threatconnect.com/en/latest/rest_api/security_labels/security_labels.html': './docs/rest_api/security_labels/',
    'https://docs.threatconnect.com/en/latest/rest_api/tags/tags.html': './docs/rest_api/tags/',
    'https://docs.threatconnect.com/en/latest/rest_api/tasks/tasks.html': './docs/rest_api/tasks/',
    'https://docs.threatconnect.com/en/latest/rest_api/victims/victims.html': './docs/rest_api/victims/',
    'https://docs.threatconnect.com/en/latest/rest_api/custom_metrics/custom_metrics.html': './docs/rest_api/custom_metrics/',
    'https://docs.threatconnect.com/en/latest/python/quick_start.html': './docs/python/quick_start.rst',
    'https://docs.threatconnect.com/en/latest/python/groups/groups.html': './docs/python/groups/',
    'https://docs.threatconnect.com/en/latest/python/indicators/indicators.html': './docs/python/indicators/',
    'https://docs.threatconnect.com/en/latest/python/owners/owners.html': './docs/python/owners/',
    'https://docs.threatconnect.com/en/latest/python/tasks/tasks.html': './docs/python/tasks/',
    'https://docs.threatconnect.com/en/latest/python/victims/victims.html': './docs/python/victims/',
    'https://docs.threatconnect.com/en/latest/python/advanced.html': './docs/python/advanced.rst',
    'https://docs.threatconnect.com/en/latest/javascript/javascript_sdk.html': './docs/javascript/',
    'https://docs.threatconnect.com/en/latest/java/java_sdk.html': './docs/java/'
}


def get_code_blocks_from_rtd(readthedocs_link):
    """Count the code blocks on the read the docs page."""
    code_divs = list()
    # for link in readthedocs_links:
    r = requests.get(readthedocs_link)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    if code_divs is not None:
        code_divs.extend(soup.findAll("div", {"class": "highlight"}))
    else:
        code_divs = soup.findAll("div", {"class": "highlight"})

    return len(code_divs)


def get_code_blocks_from_rst(location):
    """."""
    code_block_count = 0
    pattern = "\.\. code(-block)?::"

    # if the location is a file, read it
    if location.endswith(".rst"):
        with open(location, 'r') as f:
            code_block_count += len(re.findall(pattern, f.read()))
    # if the location is a directory, iterate through it
    else:
        for path, dirs, files in os.walk(location):
            for file_ in files:
                with open(os.path.join(path, file_), 'r') as f:
                    code_block_count += len(re.findall(pattern, f.read()))

    return code_block_count


def test_readthedocs_code_blocks():
    """Make sure the number of code-blocks on rtd is the number we are expecting from the rst files."""
    for mapping in mappings:
        readthedocs_code_blocks = get_code_blocks_from_rtd(mapping)
        rst_code_blocks = get_code_blocks_from_rst(mappings[mapping])

        try:
            assert readthedocs_code_blocks == rst_code_blocks
        except AssertionError as e:
            print("Missing code-blocks:")
            print("{} ({}) <-> {} ({})".format(mapping, readthedocs_code_blocks, mappings[mapping], rst_code_blocks))
            raise e
