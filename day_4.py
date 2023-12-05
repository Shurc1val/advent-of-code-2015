
from hashlib import md5

def find_lowest_num_to_produce_valid_hash(secret_key: str, num_leading_zeros: int):
    num = 0
    hashed = ''
    while (len(hashed) < num_leading_zeros) or (hashed[:num_leading_zeros] != "0" * num_leading_zeros):
        num += 1
        hashed = md5((secret_key + str(num)).encode()).hexdigest()
    return num


if __name__ == "__main__":
    print(find_lowest_num_to_produce_valid_hash("yzbqklnj", 6))