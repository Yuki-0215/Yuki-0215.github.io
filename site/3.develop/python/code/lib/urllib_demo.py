import urllib.request

response = urllib.request.urlopen('https://yuki-0215.github.io/site/0.Internet/2024-02-20-5g-docs/')

http = response.read()

print(http[:1000])