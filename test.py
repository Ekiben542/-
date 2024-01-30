import os
import time
import json

class Server:
    def __init__(self, ip):
        self.ip = ip
        self.status = self.ping()

    def ping(self):
        response = os.system("ping -c 1 " + self.ip)
        if response == 0:
            return "Online"
        else:
            return "Offline"

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

def remove_maintenance():
    print("現在あるサーバー:")
    for i, server in enumerate(servers, 1):
        print(f"{i}. {server.ip} - {server.status}")
    server_num = int(input("メンテナンスを外すサーバーの番号を入力してください: "))
    servers[server_num - 1].status = servers[server_num - 1].ping()
    print(f"Server {server_num}のMaintenanceを外しました。")

def save_data():
    data = [{"ip": server.ip, "status": server.status} for server in servers]
    with open("C:/Users/panpo/Downloads/servers.json", "w") as f:
        json.dump(data, f)
    print("サーバーデータを保存しました。")

def load_data():
    try:
        with open("C:/Users/panpo/Downloads/servers.json", "r") as f:
            data = json.load(f)
        for server_data in data:
            servers.append(Server(server_data["ip"]))
        print("サーバーデータを読み込みました。")
    except FileNotFoundError:
        print("サーバーデータが見つかりませんでした。")

def main():
    load_data()
    while True:
        print("Server Status CLI")
        for i, server in enumerate(servers, 1):
            print(f"Server {i}: {server.status}")
        print("Press key to enter ↓")
        print("1. Add Server")
        print("2. Choose server Maintenance")
        print("3. Remove server Maintenance")
        print("4. Save server data")
        choice = int(input())
        if choice == 1:
            add_server()
        elif choice == 2:
            set_maintenance()
        elif choice == 3:
            remove_maintenance()
        elif choice == 4:
            save_data()

if __name__ == "__main__":
    main()
