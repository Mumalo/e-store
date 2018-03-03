
import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='iashop', ssh_password='istradezoneuhjyt5654',
    remote_bind_address=('iashop.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='your PythonAnywhere username', password='your PythonAnywhere database password',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='iashop$shop',
    )
    print("I have connected successfully")
    connection.close()