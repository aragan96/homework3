zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
zk.delete("/MESSAGES", recursive = True)