import random
import secp256k1 as ice
import time
import os

address_to_find = input("Which keyword do you want to find ? ")
start=time.time()
i = 0

def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)
    
while True:

    dec= int(RandomInteger(1, 115792089237316195423570985008687907852837564279074904382605163141518161494336))
    HEX = "%064x" % dec
    i += 1
    print("[{}] {}".format(i, ice.privatekey_to_address(0, False, dec)))
    str = ice.privatekey_to_address(0, False, dec)
    result = address_to_find in str
    if result :
        print("   => Eureka !!! Private key : {}".format(ice.btc_pvk_to_wif(HEX, False)))
        break

    i += 1
    print("[{}] {}".format(i, ice.privatekey_to_address(0, True, dec)))
    str = ice.privatekey_to_address(0, True, dec)
    result2 = address_to_find in str
    if result2 :
        print("   => Eureka !!! Private key : {}".format(ice.btc_pvk_to_wif(HEX)))
        break
end=time.time()
print('Running time: %s Seconds'%(end-start))
os.system("pause")
