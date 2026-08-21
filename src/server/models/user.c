// I will encryption, verify and decryption features in future.
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
// --------------------------------------------------------
const int SALT_LEN = 16;
const int ITER_COUNT = 100000;
const int HASH_LEN = 32;
// --------------------------------------------------------
bool gen_salt(char* hex_out) {
	unsigned char raw[SALT_LEN];
  	// fill the random number into raw, length is SALT_LEN
	if (RAND_bytes(raw, SALT_LEN) != 1) return 0;
	for (int i = 0; i < SALT_LEN; i++)
		// Every single character in raw[i] is converted into a 2-digit hex string
		sprintf(hex_out + i * 2, "%02x", raw[i]);
	return 1;
}

bool pwd_hash(const char* pwd, const char* salt,
	  	unsigned char* res) {
	return PKCS5_PBKDF2_HMAC(
			pwd, strlen(pwd), 
			(const unsigned char*)salt,
		  	strlen(salt), 100000, 
			EVP_sha256(), HASH_LEN, res) == 1;
}

bool verify_pwd(const char* pwd, const char* salt, 
		unsigned char* stored_hash) {
	char* calcu[HASH_LEN];
	if (!pwd_hash(pwd, salt, stored_hash)) return 0;
	return  CRYPTO_memcmp(calcu, stored_hash, HASH_LEN);
}
