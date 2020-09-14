import re

email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

print(name)
print(domain)

price = 'Price: $189.50'
price_expression = 'Price: \$([0-9].*\.[0-9].*)'

matches = re.search(price_expression, price)
print(matches.group(0))
print(matches.group(1))
