import struct
import base64
import bitstring

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
            if hexNum[0][-1:]==' ': hexNum[0]=hexNum[0][:-1]
            numFiller=int(num-256*int(hexNum[0][1:2]))
            hexNum.append(f"{numFiller:02x}")
        for hexNumb in hexNum:
            allBytes.append(hexNumb)
        print(f'{value["state"]}, {num}: {hexNum}')

    hexString=''.join(allBytes)
    #print(hexString)
    return hexString

def bytes2numbers(byteString):
    chunks = [byteString[i:i+2] for i in range(0, len(byteString), 2)]
    batches = [chunks[i:i+2] for i in range(0, len(chunks), 2)]
    print(batches)

    for batch in batches:
        print(bytes(batch[0], 'utf-8'))
        print(bytes(batch[1], 'utf-8'))
        byteIntList=list(bytes(batch[0], 'utf-8'))
        byteIntList.extend(list(bytes(batch[1], 'utf-8')))
        print(bytes(byteIntList))

        print(struct.unpack('>B', bytes(batch[1], 'utf-8')))
        batchBytes=bytes(batch[0], 'utf-8')+bytes(batch[1], 'utf-8')
        print(batchBytes)
        print(struct.unpack('>H', batchBytes))

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

def hex2base64(hexString):
    print(bytes(hexString, 'utf-8'))
    return str(base64.b64encode(bytes(hexString, 'utf-8')))[2:-1]

bytes2numbers('0dea0be503d902d605d605d902d9024005800301d605c00901fc86e0fd23e054230202d605')
# hex=numbers2bytes(numbs)
# print(hex)
# print(hex2base64(hex))
#bin2bytes('11011001')
#print(len(numbs))
