import sys
import requests
from termcolor import colored
import random
import string

# Read in the strings from the text file
with open("strings.txt", "r") as f:
    strings = [line.strip() for line in f.readlines()]

# Read in the domain names from the list
if len(sys.argv) < 2:
    print("Usage: python script.py <domains_file>")
    sys.exit(1)
with open(sys.argv[1], "r") as f:
    domains = [line.strip() for line in f.readlines()]

# Open the output file for writing
with open("redirection.txt", "w") as f_out:
    # Loop over each combination of string and domain
    for string in strings:
        for domain in domains:
            # Make the request to the combined URL
            url = f"http://{domain}/{string}"
            response = requests.get(url, allow_redirects=False)

            # Check if the request was redirected
            if response.status_code == 301:
                output = f"{url} redirected to {response.headers['Location']}\n"
                color = 'green'
            elif response.status_code == 200:
                output = f"{url} did not redirect\n"
                color = 'red'
            else:
                output = f"{url} returned status code {response.status_code}\n"
                color = 'red'

            # Print the output to the terminal with color
            print(colored(output, color))
            # Write the output to the file
            f_out.write(output)
