# 성공!!
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

# 패스워드 크래킹 함수
def crack_passwords(target_hash_file, password_file):
    # 목표 해시가 저장된 파일을 읽어옵니다.
    with open(target_hash_file, 'r') as target_file:
        target_hashes = target_file.read().splitlines()

    # 패스워드 파일을 읽어옵니다.
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    cracked_count = 0  # 크래킹에 성공한 패스워드 수를 추적하는 변수

    # 각 패스워드 해시에 대해 크래킹을 시도합니다.
    for target_hash in target_hashes:
        for password in passwords:
            salt = find_salt(target_hash, password)  # 원본 패스워드와 해시를 사용하여 salt를 찾습니다.

            if salt:
                # salt를 찾았으면 원본 패스워드와 함께 해시를 다시 계산하여 확인합니다.
                hashed_password = hashlib.md5((password + salt).encode()).hexdigest()

                if hashed_password == target_hash:
                    # 저장된 해시 값과 일치하는 해시를 찾으면 원본 패스워드를 출력하고 크래킹 성공 카운트를 증가시킵니다.
                    cracked_count += 1
                    print(f"{cracked_count}/{len(target_hashes)} password has been cracked, hashed: {target_hash}, cracked: {password}")
                    
                    break  # 이미 해시가 일치하면 다음 해시로 이동합니다.

if __name__ == "__main__":
    target_hash_file = "1MillionPassword_hashed.txt"  # 목표 해시가 저장된 파일 경로
    password_file = "1MillionPassword_wordlist.txt"  # 패스워드 목록 파일 경로

    # 패스워드 크래킹 함수 호출
    crack_passwords(target_hash_file, password_file)
