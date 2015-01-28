''''''

import nsq
import tornado.ioloop
import puppet
import atexit
import time

puppet.puppet('test', '0.1.0')

def main(program):
    writer = nsq.Writer(["172.17.0.4:4150", ])
    tornado.ioloop.PeriodicCallback(pub_message(), 1000).start()

def pub_message(writer):
    return lambda: writer.pub('test', time.strftime('%H:%M:%S'), finish_pub)

def finish_pub(conn, data):
    print conn, data

atexit.register(nsq.run)
