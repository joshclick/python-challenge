# http://www.pythonchallenge.com/pc/def/map.html

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
newsent = []
for c in sentence:
    neword = ord(c) + 2
    # past end of alpha
    if neword > 122:
        neword -= 26
    # not alpha
    if neword < 97:
        neword -= 2
    newsent.append(chr(neword))

print "".join(newsent)
