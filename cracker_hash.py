import hashlib


class Hash:
    def __init__(self, password_list_path, hash_list_path):
        self.password_list = open(password_list_path)
        self.hash_list = open(hash_list_path)

    def hash_256(self):
        success_hash_list = list()
        passwords = self.password_list
        item_hash_list = [str(x).strip() for x in self.hash_list]
        for password in passwords:
            password_strip = str(password).strip()
            hash_str = hashlib.sha256(password_strip.encode('utf-8')).hexdigest()
            for item_hash in item_hash_list:
                if item_hash == hash_str:
                    success_hash_list.append(
                        {
                            password_strip: hash_str
                        }
                    )
        return success_hash_list


print(Hash(
    password_list_path='password_integer.txt',
    hash_list_path='hash_list.txt'
).hash_256())
