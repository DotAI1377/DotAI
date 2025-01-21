import difflib
from urllib.parse import urlparse


def check_website_cloning(website_url, known_websites):
    """
    Compares a website's structure and content with a list of known websites to detect potential cloning.

    Args:
        website_url (str): The URL of the website to analyze.
        known_websites (list): A list of URLs for comparison.

    Returns:
        dict: A dictionary containing cloning analysis results.
    """
    results = []
    analyzed_domain = get_domain(website_url)

    for known_website in known_websites:
        known_domain = get_domain(known_website)
        similarity = calculate_similarity(analyzed_domain, known_domain)

        if similarity > 0.8:  # Threshold for similarity
            results.append({
                "known_website": known_website,
                "similarity": similarity,
                "potential_clone": True
            })

    return {
        "input_website": website_url,
        "cloning_detected": len(results) > 0,
        "details": results
    }

def get_domain(url):
    """
    Extracts the domain from a given URL.

    Args:
        url (str): The URL to parse.

    Returns:
        str: The domain of the URL.
    """
    parsed_url = urlparse(url)
    return parsed_url.netloc

def calculate_similarity(domain1, domain2):
    """
    Calculates the similarity between two domains.

    Args:
        domain1 (str): The first domain.
        domain2 (str): The second domain.

    Returns:
        float: The similarity ratio between the two domains.
    """
    return difflib.SequenceMatcher(None, domain1, domain2).ratio()
