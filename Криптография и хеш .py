#Криптография (хеширование и расшифровка)

#Хешированный Дайджест

import hashlib
hashlib.md5.update(b'Python rocks!')
result = hashlib.md5.digest()
print(result)


#Трассировка данного хеша

print(md5.hexdigest())

#Создание хеша sha521

import hashlib.sha1(b'Hello Python').hexdigest()
print(sha)

#Вывод ключа

import binascii
dk = hashlib.pbkdf2_hmac(hash_name = 'Sha256', password = b'bad_password34', salt = b'bad_salt', iteration = 100000)
result = binascii.hexlify(dk)
print(result)
