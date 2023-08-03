import os
import re
from ethereum.utils import mk_contract_address, encode_hex, privtoaddr

# find address with the most leading zeros
NUMITER = 1000 

# find the vanity address
best = None
best_private_key = None
for _ in range(NUMITER):
    # generate a random private key
    private_key = os.urandom(32)
    addr = privtoaddr(private_key)
    contract_addr = encode_hex(mk_contract_address(addr, 0))
    
    # count leading zeros
    num_leadings = re.search('(?!0)', contract_addr).start()

    if best is None or num_leadings > best:
        best = num_leadings
        best_addr = contract_addr
        best_private_key = private_key

        print(f"0x{best_addr}")

print(f"Found 0x{best_addr} with {best} leading zeros.")
print("The Private key is :")
print(encode_hex(best_private_key))