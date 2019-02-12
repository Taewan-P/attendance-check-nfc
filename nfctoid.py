from random import randint
def idtest():
    return "AD:CG:3F"

def scan_id():
    id = ['AD:CG:3F:4B', 'EF:5F:95:60', '3D:51:B9:9A', '25:DB:C0:A4', '4D:D0:56:7D']
    num = randint(0, len(id)-1)
    #print(id[num])
    return id[num]