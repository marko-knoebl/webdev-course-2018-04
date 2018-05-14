from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com'
response = urlopen(url).read()
# print response

soup = BeautifulSoup(response)
# print soup.html.head.title.string

def get_website_title(url):
    response = urlopen(url).read()
    soup = BeautifulSoup(response)
    return soup.html.head.title.string

# print get_website_title('https://google.com')
# print get_website_title('https://en.wikipedia.org')

def get_profile_urls(soup):
    links = soup.findAll('a')

    profile_urls = []

    for link in links:
        if link.string == 'See full profile':
            profile_urls.append(url + link['href'])

    return profile_urls

profile_urls = get_profile_urls(soup)

def get_email_from_profile_url(profile_url):
    response = urlopen(profile_url).read()
    profile_soup = BeautifulSoup(response)
    span_element = profile_soup.find('span', attrs={'class': 'email'})
    email = span_element.string
    return email

for profile_url in profile_urls:
    print get_email_from_profile_url(profile_url)