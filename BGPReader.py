import pybgpdump as pbd

filename = 'data\\bview.20190202.0000.gz'

reader = pbd.BGPDump(filename)

print reader.next()