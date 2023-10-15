import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter your message: ")
    client_socket.sendto(message.encode('utf-8'), ('localhost', 12345))
    client_socket.close()

if __name__ == "__main__":
    start_client()
