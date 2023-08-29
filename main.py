import struct

# pulse[0] = [700, 1400]
# pulse[1] = [1400, 700]
# pulse[2] = [3000, 700]
#
# rawCode = '21100'

text = open('byteNumbers').read().split('\n')
numbs = []
for numb in text:
    numbs.append({'state': numb.split(' ')[0], 'value': int(numb.split(' ')[1])})

print(numbs)


def numbers2bytes(byteList):
    isPreambleOmitted = False
    allBytes = []
    for value in byteList:
        if not isPreambleOmitted:
            isPreambleOmitted = True
            continue
        num = value['value']
        hexNum = str(struct.pack(">H", num))[2:-1].split('\\x')[1:]
        if len(hexNum) == 1:
            numFiller=int(num-256*int(hexNum[0][1:2]))
            hexNum.append(f"{numFiller:02x}")
        for hexNumb in hexNum:
            allBytes.append(hexNumb)
        print(f'{value["state"]}, {num}: {hexNum}')
    print(len(allBytes))


def bin2bytes(binary):
    low = '03'
    high = 'ee'
    sequence = []
    for num in binary:
        if num == 1:
            sequence.extend([high, low])
        else:
            sequence.extend([low, high])
    print(sequence)
    return sequence


numbers2bytes(numbs)
#bin2bytes('11011001')
#print(len(numbs))
