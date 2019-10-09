string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(0, len(string)):
 for j in range(0, len(alphabet)):
   if (string[i] == alphabet[j] and (ord(string[i]) != 32 and ord(string[i]) >= 97)):
    newNum = ord(string[i])+2
    if (newNum > 122):
      newNum = newNum - 26;
    print chr(newNum),

