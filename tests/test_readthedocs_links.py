"""Find and test each of the links in the docs to make sure they are working properly."""
import sys

from bs4 import BeautifulSoup
import requests


def _get_headings(soup):
    """Get the href/id of all of the headings in the given html."""
    headings = list()

    headings.extend([link['href'] for link in soup.findAll('a', {'class': 'headerlink'})])

    return headings


def test_links():
    """."""
    bad_links = 0
    base_url = 'https://docs.threatconnect.com'
    # TODO: consider dynamically pulling the links below:
    docs_pages = ['https://docs.threatconnect.com/en/latest/getting_started.html',
                  'https://docs.threatconnect.com/en/latest/rest_api/rest_api.html',
                  'https://docs.threatconnect.com/en/latest/python/python_sdk.html',
                  'https://docs.threatconnect.com/en/latest/java/java_sdk.html',
                  'https://docs.threatconnect.com/en/latest/javascript/javascript_sdk.html',
                  'https://docs.threatconnect.com/en/latest/deployment_config.html',
                  'https://docs.threatconnect.com/en/latest/tcex/tcex.html',
                  'https://docs.threatconnect.com/en/latest/sdk_trademarks.html']

    for page in docs_pages:
        print("\n\n>>> Reviewing {}".format(page))
        # request page
        r = requests.get(page)

        # find all hrefs
        soup = BeautifulSoup(r.text, 'html.parser')

        links = soup.find_all('a')
        headings = _get_headings(soup)

        for link in links:
            href = link['href']

            # ignore "mailto:" links
            if href.startswith("mailto:"):
                continue
            # ignore links to external locations
            elif href.startswith("//") or href.startswith("http"):
                # TODO: consider checking these links too
                continue
            # check links that are relative to the base url
            elif href.startswith("/"):
                target_url = base_url + href
                r = requests.get(target_url)

                if str(r.status_code).startswith("4"):
                    print("{} error when requesting: {}".format(r.status_code, target_url))
                    bad_links += 1
            # check links to locations on the current page
            elif href.startswith("#"):
                # skip any links that are just href="#"
                if href == "#":
                    pass
                elif href not in headings:
                    print("Link to {} does not exist".format(href))
                    bad_links += 1
            # check links that are relative to the current page
            else:
                # create a target url by removing the file from the current page and adding the desired href
                target_url = "/".join(page.split("/")[:-1]) + "/" + href
                r = requests.get(target_url)

                if str(r.status_code).startswith("4"):
                    print("{} error when requesting: {}".format(r.status_code, target_url))
                    bad_links += 1

    if bad_links > 0:
        print("\n\n{} bad links found".format(bad_links))
        sys.exit(3)
