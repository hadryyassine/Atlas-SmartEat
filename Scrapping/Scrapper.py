import requests
recipe_url = 'https://www.sainsburysmagazine.co.uk/recipes/mains/roasted-roots-tagine'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(recipe_url, headers=headers)

if response.status_code == 200:
    content = response.text
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")