def sid_bytes_to_str(hexstr):
    """
    Convert a SID hex string from MS SQL to a readable SID string.
    Input: 0x0105000000000005150000005b7bb0f398aa2245ad4a1ca451040000
    """

    hexstr = hexstr.strip().lower()
    if hexstr.startswith("0x"):
        hexstr = hexstr[2:]
    hexstr = ''.join(hexstr.split())

    b = bytes.fromhex(hexstr)

    revision = b[0]
    subauth_count = b[1]
    identifier_authority = int.from_bytes(b[2:8], byteorder='big')
    sub_authorities = []
    for i in range(subauth_count):
        start = 8 + i * 4
        sub_authority = int.from_bytes(b[start:start+4], byteorder='little')
        sub_authorities.append(sub_authority)

    sid_str = f"S-{revision}-{identifier_authority}"
    for sub in sub_authorities:
        sid_str += f"-{sub}"
    return sid_str, sub_authorities  


if __name__ == "__main__":
    hexstr = input("Enter Hex String: ")

    sid_str, sub_auths  = sid_bytes_to_str(hexstr)
    domain_sid = '-'.join(sid_str.split('-')[:-1])

    print(f"\nDomain SID: {domain_sid}")
    if sub_auths:
        print(f"RID: {sub_auths[-1]}")
