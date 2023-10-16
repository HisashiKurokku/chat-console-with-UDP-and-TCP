import socket


def start_client():
    # Tạo ống nối UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Gửi dữ liệu
    message = input("Nhập tin nhắn: ")
    client_socket.sendto(message.encode('utf-8'), ('localhost', 42069))

    # Đóng kết nối
    client_socket.close()


if __name__ == "__main__":
    start_client()
