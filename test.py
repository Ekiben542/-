
import time

class Server:
    def __init__(self, ip):
        self.ip = ip
        self.status = "Loading. . ."

servers = []

def add_server():
    ip = input("IPを入力してください: ")
    servers.append(Server(ip))
    print(f"Server {len(servers)}として追加しました。")

def set_maintenance():
    print("現在あるサーバー:")
    for i, server in enumerate(servers, 1):
        print(f"{i}. {server.ip} - {server.status}")
    server_num = int(input("メンテナンスするサーバーの番号を入力してください: "))
    servers[server_num - 1].status = "Maintenance"
    print(f"Server {server_num}をMaintenanceとしました。")

def main():
    while True:
        print("Server Status CLI")
        for i, server in enumerate(servers, 1):
            print(f"Server {i}: {server.status}")
        print("Press key to enter ↓")
        print("1. Add Server")
        print("2. Choose server Maintenance")
        choice = int(input())
        if choice == 1:
            add_server()
        elif choice == 2:
            set_maintenance()

if __name__ == "__main__":
    main()
