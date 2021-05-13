import pyDes

class desCrypt():

    #加密
    def desEncrypt(self,encryptText):
        key = bytearray(b'eplatform_id\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        k = pyDes.triple_des(key, pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(encryptText)
        return d.hex()

