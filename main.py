from urllib.parse import urlparse
import requests
import os
def get_url():
    url = input("inter link: ")
    return url


def html_writer(url, filename):
    try:

        response = requests.get(url)

        if response.status_code == 200:

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"files saved: {filename}")

        else:
            print(f"unsucsessful {response.status_code}")

    except Exception as e:
        print(f"erorr {e}")

if __name__ == "__main__":
    while True:

        url = get_url()

        parsed_url = urlparse(url)
        domain_name = parsed_url.netloc.replace("www.", "")
        
        filename = f"{domain_name}.html"

        html_writer(url, filename)

        continue_choice = input("countinue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break