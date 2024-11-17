#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_links(domain):
    try:
        # Send a GET request to the provided domain
        response = requests.get(domain)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags and extract the href attribute
        links = []
        for a_tag in soup.find_all('a', href=True):
            # Join relative URLs with the base domain
            link = urljoin(domain, a_tag['href'])
            links.append(link)
        
        # Print the links
        if links:
            print(f"\n[+] Found {len(links)} links on {domain}:\n")
            for link in links:
                print(link)
        else:
            print(f"[-] No links found on {domain}.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: Unable to fetch links from {domain}. {e}")

def main():
    print("""
    
            █ ▄ ▄▄▄▄  █  ▄ ▗▞▀▀▘
            █ ▄ █   █ █▄▀  ▐▌   
    一═デ︻ █ █ █   █ █ ▀▄ ▐▛▀▘  ︻デ═一 
            █ █       █  █ ▐▌   
              ℓιηк ƒєт¢нєя
               @vulncrax
 
    """)
    domain = input("Enter the domain (e.g., https://example.com): ").strip()
    
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "http://" + domain  # Default to HTTP if no protocol is specified

    print(f"\n[+] Fetching links from: {domain}\n")
    fetch_links(domain)

if __name__ == "__main__":
    main()
