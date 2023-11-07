import socket, requests

#def get_ip():
    #response = requests.get('https://api.ipify.org')
    #if response.status_code == 200:
        #return response.text
    #else:
        #return None

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #server_address = (get_ip(), какой-то порт)
        server.bind(('localhost', 2000))
        print('Working...')
        server.listen(5)
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
            if data == 'test':
                response = 'Дай Бог автомат по мат анализу'
            elif data == 'test2':
                response = 'Дай Бог автомат по линалу'
            else:
                response = 'неизвестный запрос'

            client_socket.send(response.encode('utf-8'))
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('End working')

if __name__ == '__main__':
    start_server()