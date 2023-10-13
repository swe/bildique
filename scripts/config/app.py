import yaml

with open('../../secrets.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['DBConnection']['datatablename'])
