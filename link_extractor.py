"""
Web Page Download and Link Extraction Module

Provides functions to download web page content from a URL and extract links.

Functions:
- download_page(url: str) -> str: Download and return the page content as a UTF-8 encoded string.
- extract_links(page: str) -> List[str]: Extract links from the HTML page content.

Note: Requires the urlopen, re and typing. modules. Raises URLError or URL exceptions
"""
from urllib.request import urlopen
import re
from typing import List


def download_page(url: str) -> str:
    """
    Download and return the content of a web page as a UTF-8 encoded string.

    Args:
        url (str): The URL of the web page to download

    Returns:
        str: The web page content as a UTF-I encoded string

    Raises:
        URLError: If there's an issue with the URL or the web page cannot fetched.
    """

    return urlopen(url).read().decode("utf-8")


def extract_links(page: str) -> List[str]:
    """Extract and return a list of links from the provided HTML page content.  Args:
        page (str): The HTML page content in string format.

    Returns:
        List[str]: A list of URLs extracted from the HTML.

    Note:
        The function uses a regular expression to find links in the HTML content.
    """
    link_regex = re.compile("<a[^>]+href=[\"'](.*?)[\"']", re.IGNORECASE)
    return link_regex.findall(page)


if __name__ == "__main__":
    TARGET_URL = "http://www.apress.com"
    apress = download_page(TARGET_URL)
    links = extract_links(apress)

    for link in links:
        print(link)
