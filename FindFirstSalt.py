import hashlib
import itertools

# 원본 패스워드와 목표 해시를 입력으로 받아, 가능한 salt 값을 조합하여 검사하는 함수
def find_salt(target_hash, original_password):
    salt_chars = "abcdefghijklmnopqrstuvwxyz0123456789"  # 소문자와 숫자로만 구성된 salt 문자열
    salt_length = 3  # 세 자릿수의 salt를 찾아야 함

    # 가능한 모든 salt 값 조합을 시도
    for salt in itertools.product(salt_chars, repeat=salt_length):
        salt = ''.join(salt)  # 튜플을 문자열로 변환
        hashed_password = hashlib.md5((original_password + salt).encode()).hexdigest()

        if hashed_password == target_hash:
            return salt  # 일치하는 salt를 찾으면 반환

    return None  # 일치하는 salt를 찾지 못한 경우 None을 반환

if __name__ == "__main__":
    target_hash = "fed044f7261b788e590d2dbc590616e5"  # 주어진 해시 값
    original_password = "123456"  # 주어진 원본 패스워드

    found_salt = find_salt(target_hash, original_password)

    if found_salt:
        print(f"Found salt: {found_salt}")
    else:
        print("Salt not found.")
