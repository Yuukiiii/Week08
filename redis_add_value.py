import argparse


def set_value(index, length):
    value = str('a'*length)
    key_length = 3 + len(str(index))
    keyname = "key{}".format(str(index))
    proto = "*3\r\n$3\r\nSET\r\n${}\r\n{}\r\n${}\r\n{}\r\n".format(key_length, keyname, length, value)
    print(proto)


parser = argparse.ArgumentParser()
# 必选参数
parser.add_argument('-l', '--length', dest='length', required=True, type=int, help='value length')
parser.add_argument('-c', '--count', dest='count', required=True, type=int, help='value count')

# 提取命令参数
args = parser.parse_args()
# string
length = args.length
count = args.count

for i in range(0, count):
    set_value(i, length)
