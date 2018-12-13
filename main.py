from config import MATRIX
from lib import ChatMatrix

def main():
    print('demo')

if __name__ == '__main__':
    x = ChatMatrix()
    x.connect(MATRIX['HOST'], MATRIX['USER'], MATRIX['PASSWORD'], MATRIX['VALID_CERT'])
    # x.roomList()
    # x.roomListFind('Proyecto Policia Boliviana')
    x.roomMessages('!ixmXhojuzgNyklAaIC:agetic.gob.bo')
    main()
