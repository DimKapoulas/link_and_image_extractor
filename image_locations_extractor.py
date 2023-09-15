"""
Web Page Content Download and Image Extraction Module

This module provides functions for downloading the content of a web page 
from a given URL and extracting image source URLs from the downloaded HTML content.

Functions:
- download_page(url: str) -> str: Download and return the web page content 
    as a UTF-8 encoded string.
- extract_image_locations(page: str) -> List[str]: Extract image source URLs 
    from the provided HTML content.
"""

from urllib.request import urlopen, urljoin
from typing import List
import re


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


def extract_image_locations(page: str) -> List[str]:
    """
    Extract and return a list of image source URLs from the provided HTML page content.

    Args:
        page (str): The HTML page content in string format.

    Returns:
        List[str]: A list of image source URLs.

    Example:
        >>> html_content = '<img src="image1.jpg"> <img src="image2.jpg">'
        >>> image_locations = extract_image_locations(html_content)
        >>> print(image_locations)
        ['image1.jpg', 'image2.jpg']
    """
    img_regex = re.compile("<img[^>]+src=[\"'](.*?)[\"']", re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == "__main__":
    URL = "http://www.apress.com"
    apress = download_page(URL)
    image_locations = extract_image_locations(apress)

    for src in image_locations:
        print(urljoin(URL, src))
