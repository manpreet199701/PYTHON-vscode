import socket 
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.python.org', 80))
mysocket.send(b'GET / HTTP/1.0\r\n\r\n')
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysocket.close()
# This code connects to the Python website and retrieves the HTML content of the homepage.