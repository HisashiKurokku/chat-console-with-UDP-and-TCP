import socket


def start_server():
    # Tạo ống nối UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Gán ống nối đến địa chỉ và cổng cụ thể
    server_socket.bind(('localhost', 42069))
    print("Máy chủ đang lắng nghe ở cổng 42069...")

    while True:
        # Nhận dữ liệu theo những phần nhỏ và truyền lại
        message, client_address = server_socket.recvfrom(1024)
        print(
            f"Tin nhắn đã nhận: {message.decode('utf-8')} from {client_address}")


if __name__ == "__main__":
    start_server()
