import paramiko

transport = paramiko.Transport(('193.22.152.113', 45798))
transport.connect(username='root', password='8tXrgM7WWdGgi@5')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('fromlinux.txt', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/root/1.log', '1.log')
transport.close()
