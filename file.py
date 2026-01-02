import subprocess
import time

server_ip = 'YOUR_SERVER_IP'  # Thay thế bằng IP của server Minecraft
server_port = 25565  # Cổng mặc định của Minecraft

for i in range(100):
    username = f'Bot_{i}'
    password = f'password_{i}'  # Bạn có thể tạo mật khẩu ngẫu nhiên ở đây
    command = f'mcprotoc {server_ip} {server_port} -u {username} -p {password}'
    subprocess.Popen(command, shell=True)
    time.sleep(1)  # Delay để tránh quá tải server
