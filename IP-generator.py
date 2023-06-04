import random
def generate_ip():
    ip = "192.168."#class
    for i in range(100):
        octet = str(random.randint(0,254))
        ip += octet + "."
    ip = ip[:-1]
    return ip
print(generate_ip())
