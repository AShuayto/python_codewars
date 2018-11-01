'''
A stream of data is received and needs to be reversed. Each segment is 8 bits long, meaning the order of these segments need to be reversed, for example:

11111111  00000000  00001111  10101010
  byte1     byte2     byte3     byte4

should become:
10101010  00001111  00000000  11111111
  byte4     byte3     byte2     byte1

The total number of bits will always be a multiple of 8. The data is given in an array as such:
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
'''

def data_reverse(data):
    flattened = []
    a = [data[i:i+8] for i in range(0,len(data),8)]
    a.reverse()
    for array in a:
        for num in array:
            flattened.append(num)
    return flattened

'''
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

test.assert_equals(data_reverse(data1),data2)

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
test.assert_equals(data_reverse(data3),data4)
'''