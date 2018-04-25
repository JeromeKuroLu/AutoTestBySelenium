import urllib3
import selenium

from test.issues.arp_operation import Arp_Operation


class Monitor:

    def __init__(self):
        self.http = urllib3.PoolManager()

    def monitor(self, url):
        Arp_Operation().log_in_jenkins()
        print('hello world')


if __name__ == '__main__':
    print('begin')
    m = Monitor()
    m.monitor('d')
    print('end')