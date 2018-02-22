#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find and test each of the links in the docs to make sure they are working properly."""

import os
import re
import sys

from bs4 import BeautifulSoup
import requests

base_url = 'https://docs.threatconnect.com/'
pages = {
    "https://docs.threatconnect.com/en/latest/rest_api/": [
        'change_log.html',
        'quick_start.html',
        'overview.html',
        'associations/associations.html',
        'attributes/attributes.html',
        'groups/groups.html',
        'indicators/indicators.html',
        'owners/owners.html',
        'security_labels/security_labels.html',
        'tags/tags.html',
        'tasks/tasks.html',
        'victims/victims.html',
        'custom_metrics/custom_metrics.html'
    ],
    "https://docs.threatconnect.com/en/latest/python/": [
        'python_sdk.html',
        'quick_start.html',
        'groups/groups.html',
        'indicators/indicators.html',
        'owners/owners.html',
        'tasks/tasks.html',
        'victims/victims.html',
        'advanced.html'
    ],
    "https://docs.threatconnect.com/en/latest/javascript/": [
        'javascript_sdk.html'
    ],
    "https://docs.threatconnect.com/en/latest/java/": [
        'java_sdk.html'
    ]
}


def _get_heading_ids(soup):
    """Get the href/id of all of the headings in the given html."""
    headings = list()

    headings.extend([link['href'] for link in soup.findAll('a', {'class': 'headerlink'})])

    return headings


def test_links():
    """."""
    bad_links = 0
    excluded_patterns = ["readthedocs.com"]

    for base_page, subpages in pages.items():
        for subpage in subpages:
            page = base_page + subpage

            # request page
            r = requests.get(page)

            # find all hrefs
            soup = BeautifulSoup(r.text, 'html.parser')

            # get all of the links and headings from the page
            links = soup.find_all('a')
            headings = _get_heading_ids(soup)

            for link in links:
                href = link['href']

                # ignore "mailto:" links
                if href.startswith("mailto:"):
                    continue
                # ignore links to external locations
                elif href.startswith("//") or href.startswith("http"):
                    matches_exclusion_pattern = False
                    for pattern in excluded_patterns:
                        if pattern in href:
                            matches_exclusion_pattern = True
                            break

                    if matches_exclusion_pattern:
                        continue

                    if href.startswith("//"):
                        href = "http:" + href

                    r = requests.get(href)

                    if not r.ok:
                        print("\n\n>>> Reviewing {}".format(page))
                        print("{} error when requesting: {}".format(r.status_code, href))
                        bad_links += 1
                # check links that are relative to the base url
                elif href.startswith("/"):
                    target_url = base_url + href
                    r = requests.get(target_url)

                    if not r.ok:
                        print("\n\n>>> Reviewing {}".format(page))
                        print("{} error when requesting: {}".format(r.status_code, target_url))
                        bad_links += 1
                # check links to locations on the current page
                elif href.startswith("#"):
                    # skip any links that are just href="#"
                    if href == "#":
                        pass
                    elif href not in headings:
                        print("\n\n>>> Reviewing {}".format(page))
                        print("Link to {} does not exist".format(href))
                        bad_links += 1
                # check links that are relative to the current page
                else:
                    # create a target url by removing the file from the current page and adding the desired href
                    target_url = "/".join(page.split("/")[:-1]) + "/" + href
                    r = requests.get(target_url)

                    if str(r.status_code).startswith("4"):
                        print("\n\n>>> Reviewing {}".format(page))
                        print("{} error when requesting: {}".format(r.status_code, target_url))
                        bad_links += 1

    if bad_links > 0:
        print("\n\n{} bad links found".format(bad_links))
        sys.exit(3)


def test_standard_script_heading_link():
    """Make sure the standard script heading is still in the docs so that the links in the code snippets will work.

    See: https://docs.threatconnect.com/en/latest/python/python_sdk.html#standard-script-heading
    """
    response = requests.get("https://docs.threatconnect.com/en/latest/python/quick_start.html#standard-script-heading")
    soup = BeautifulSoup(response.text, "html.parser")

    heading_ids = _get_heading_ids(soup)
    heading_found = False

    for heading in heading_ids:
        if heading == "#standard-script-heading":
            heading_found = True
            break

    if not heading_found:
        raise RuntimeError("Unable to find the Standard Script Heading used in the code snippets.")


def test_no_dev_links():
    """Make sure there are no links to the dev version of the docs."""
    dev_pattern = "en/dev/"

    # iterate through the files in the /docs/ directory to make sure the are no links to the dev version of the documentation
    for path, dirs, files in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))):
        # ignore all directories that start with "_"
        if "/_" not in path:
            for file in files:
                # check to see if the dev pattern is in the file
                with open("{}/{}".format(path, file), 'r') as f:
                    print("Checking: {}/{}".format(path, file))
                    file_text = f.read()
                    assert dev_pattern not in file_text
                    print("check passed\n")


def test_markdown_links():
    """Make sure there are no links to the dev version of the docs."""
    markdown_link_pattern = '\[.*?\]\(.+\)'
    errors = 0

    for path, dirs, files in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), "../docs"))):
        # ignore all directories that start with "_"
        if "/_" not in path:
            for file in files:
                if not file.startswith('.'):
                    # check to see if the dev pattern is in the file
                    with open("{}/{}".format(path, file), 'r') as f:
                        file_text = f.read()
                        try:
                            markdown_links = re.findall(markdown_link_pattern, file_text)
                            assert markdown_links == []
                        except AssertionError:
                            print("Found what appears to be a markdown link in {}/{}: {}".format(path, file, markdown_links))
                            errors += 1

    assert errors == 0


# def test_no_broken_headings():
#     """Make sure there are no links to the dev version of the docs."""
#     broken_heading_pattern = 'id="id[0-9]'

#     for base_page, subpages in pages.items():
#         for subpage in subpages:
#             page = base_page + subpage

#             # request page
#             r = requests.get(page)

#             try:
#                 # check to see if there are any broken headings in the page
#                 assert len(re.findall(broken_heading_pattern, r.text)) == 0
#             except AssertionError as e:
#                 print("\n\n>>> Reviewing {}".format(page))
#                 raise e
