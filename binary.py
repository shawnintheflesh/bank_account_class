# with open("binary", 'bw') as bin_file:
#         bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as  binfile:
#     for b in binfile:
#         print(b)

a = 65534
b = 65535
c = 65536
d = 2998302

with open("binary2", 'bw') as more_bin:
    more_bin.write(a.to_bytes(2, 'big'))
    more_bin.write(b.to_bytes(2, 'big'))
    more_bin.write(c.to_bytes(4, 'big'))
    more_bin.write(d.to_bytes(4, 'big'))
    more_bin.write(d.to_bytes(4, 'little'))

with open("binary2", 'br') as more_bin:
    e = int.from_bytes(more_bin.read(2), 'big')
    print(e)
    f = int.from_bytes(more_bin.read(2), 'big')
    print(f)
    g = int.from_bytes(more_bin.read(4), 'big')
    print(g)
    h = int.from_bytes(more_bin.read(4), 'big')
    print(h)
    i = int.from_bytes(more_bin.read(4), 'big')
    print(i)



