import socket

website = input("Enter website (e.g. google.com): ")
ip = socket.gethostbyname(website)

print(f"IP address of {website}: {ip}")
