import telnetlib
import time

def TelnetM40ButtonTest():
    try:
        HOST = "192.168.1.6"
        #HOST = '192.168.1.99'
        print('Starting button test on ' + HOST)
        PORT = 23
        TIMEOUT = 5
        tn = telnetlib.Telnet(host=HOST, port=PORT, timeout=TIMEOUT)
        tn.write(b'$login,factory,factory\n')
        tn.write(b"$bts,s,0\n")
        tn.write(b"$bts,G\n\r")
        ret = tn.read_all()
        print(ret)
        while True:
            tn.write(b"$bts,G\n")
            time.sleep(1)
            tn.write(b"$\r")
            ret = tn.read_all()
            print(ret)
            time.sleep(1)
        tn.close()
    except OSError as err:
        #tn.close
        print(err)
        return False, err

def __init__(self):
    super().__init__()
    self.initUI()


def main():
    ret  = TelnetM40ButtonTest()
    print(ret)
    pass


if __name__ == '__main__':
    main()
