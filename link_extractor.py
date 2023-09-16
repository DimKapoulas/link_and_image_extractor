"""
Web Page Download and Link Extraction Module

Provides functions to download web page content from a URL, extract links, and perform URL searches.

Functions:
- download_page(url: str) -> str: Download and return the page content as a UTF-8 encoded string.
- extract_links(page: str) -> List[str]: Extract links from the HTML page content.
- get_links(page_url: str) -> Optional[List[str]]: Extract links from a  page, filtered by hostname.

URL Search Functions:
- url_search(start_url: str, strategy: str = "DFS"): Perform URL search using DFS or BFS strategy.

Note: Requires the urlopen, re, and typing modules. Raises URLError or URL exceptions.
"""
from urllib.request import urlopen
from urllib.parse import urlparse, urljoin
import re
from typing import List, Optional, Deque
from collections import deque




def filter_none(iterable):
    """
    Helper function that filters out None values from an iterable and returns a new iterable with
    non-None elements.

    Args:
        iterable: An iterable (e.g., a list, tuple, or generator) containing elements to filter.

    Returns:
        Iterable: A new iterable containing only non-None elements from the input iterable.

    Example:
        >>> filter_none([1, 2, None, 3, None, 4])
        [1, 2, 3, 4]

    """
    return (item for item in iterable if item is not None)


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


def extract_links(page: Optional[str]) -> Optional[List[str]]:
    """
    Extract and return a list of links from the provided HTML page content.

    Args:
        page Optional[str]: The HTML page content in string format, if any

    Returns:
        Optional[List[str]]: A list of URLs extracted from the HTML. May be empty

    Note:
        The function uses a regular expression to find links in the HTML content.
    """
    if not page:
        return []
    link_regex = re.compile("<a[^>]+href=[\"'](.*?)[\"']", re.IGNORECASE)
    links = link_regex.findall(page)
    links = [urljoin(page, link) for link in links]
    return links


def get_links(page_url: str) -> Optional[List[str]]:
    """
    Extracts links from a web page identified by the given 'page_url'.

    Args:
        page_url (str): The URL of the web page from which links will be extracted.

    Returns:
        Optional[List[str]]: A list of links (URLs) found on the web page, filtered to include only
        links with the same hostname as the input 'page_url'. If no links are found, an empty list
        is returned. If there is an issue with downloading or parsing the page, None is returned.

    Note:
        - The function uses the 'urlparse' function to determine the hostname of the
            'page_url'.
        - It then downloads the web page using 'download_page' and extracts links
            using 'extract_links'.
        - Links with different hostnames are excluded from the final list.
        - In case of errors or inability to download the page, the function returns None.
    """
    parsed_url = urlparse(page_url)
    host = parsed_url.hostname
    page = download_page(page_url)
    links = extract_links(page)
    if links:
        return [link for link in links if urlparse(link).hostname == host] or None
    return []


def url_search(start_url: str, stategy: str = "DFS"):
    """
    Perform URL search using Depth-First Search (DFS) or Breadth-First Search (BFS) strategy.

    Args:
        start_url (str): The URL to start the search from.
        stategy (str, optional): The search strategy to use, either "DFS" (default) or "BFS".

    Returns:
        None

    This function explores URLs using either Depth-First Search (DFS) or Breadth-First Search (BFS)
    strategy. It starts from the given start_url and visits links in the chosen strategy order.
    The function uses a queue (implemented as a deque) to manage which URLs to explore next
    and a visited set to keep track of the URLs already explored.
    The exploration process continues until all reachable URLs have been visited.

    Example:
        >>> url_search("https://example.com", "DFS")
        # Start a DFS search from "https://example.com"

    """
    visited = set()
    queue: Deque = deque()

    if stategy == "DFS":
        enqueue = queue.appendleft
    else:
        enqueue = queue.append

    enqueue(start_url)

    while queue:
        url = queue.pop()
        if url in visited:
            continue
        visited.add(url)

        links = filter_none(get_links(url))
        for link in links:
            enqueue(link)
            print(link)


if __name__ == "__main__":
    URL = "https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/"
    url_search(URL, 'BFS')
    # url_search(URL)
