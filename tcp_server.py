import socket

def start_server():
    # Tạo ống nối TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Gán ống nối đến địa chỉ và cổng cụ thể
    server_socket.bind(('localhost', 42069))

    # Lắng nghe những kết nối đang đến
    server_socket.listen(1)
    print("Máy chủ đang lắng nghe ở cổng 42069...")

    while True:
        # Chờ một kết nối
        client_socket, client_address = server_socket.accept()
        print(f"Đã chấp nhận kết nối từ {client_address}")
        
        # Nhận dữ liệu theo những phần nhỏ và truyền lại
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Đã nhận tin nhắn: {message}")

        # Dọn dẹp kết nối
        client_socket.close()

if __name__ == "__main__":
    start_server()