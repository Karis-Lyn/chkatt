// I will encryption, verify and decryption features in future.
#define PCRE2_CODE_UNIT_WIDTH 8
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include "../../public/global.h"
#include "../../public/pcre2.h"
// --------------------------------------------------------
const int SALT_LEN = 16;
const int ITER_COUNT = 100000;
const int HASH_LEN = 32;
typedef void (*outputer)(const char*);
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
	const int SHA256_ITER_COUNT = 100000;
	return PKCS5_PBKDF2_HMAC(
			pwd, strlen(pwd), 
			(const unsigned char*)salt,
		  	strlen(salt), SHA256_ITER_COUNT, 
			EVP_sha256(), HASH_LEN, res) == 1;
}

// 0 for success, 1 for error
bool verify_pwd(const char* pwd, const char* salt, 
		unsigned char* stored_hash) {
	char* calcu[HASH_LEN];
	if (!pwd_hash(pwd, salt, stored_hash)) return 0;
	return  CRYPTO_memcmp(calcu, stored_hash, HASH_LEN);
}

bool recheck_usr_data(
		char* usr_info,
	  	char* verify_usri,
	  	outputer output) {

	int err_code = 0;
	PCRE2_UCHAR8 buf[256];
	PCRE2_SIZE err_off = 0;
	pcre2_match_data_8* md = NULL;
	pcre2_code_8* reg_ret = NULL;

	reg_ret = pcre2_compile_8( // compile regexc
			(PCRE2_SPTR8)verify_usri,
		  	PCRE2_ZERO_TERMINATED, // meet until character '\0'
		  	0,  &err_code, &err_off, NULL); // 0 for options, NULL for context 

	if (!reg_ret) {
		pcre2_get_error_message_8(err_code, buf, sizeof(buf));	
		fprintf(stderr, "[Err: compile failed for %s\n]", buf);
		return 1;
	}
	// match whole statement
	md = pcre2_match_data_create_from_pattern_8(reg_ret, NULL);

	PCRE2_SIZE offset = 0; // match for 0 or head
	err_code = pcre2_match_8( // exec regexc
			reg_ret, (PCRE2_SPTR8)usr_info,
		  	strlen(usr_info), offset,
		  	0, md, // match option and data block of storing
		  	NULL); // context

	// greater than 0 for success plus less than 0 for wrong
	if (err_code < 0) { 
		pcre2_get_error_message_8(err_code, buf, sizeof(buf));	
		// the function can be executed based on the passed function,
		// as long as the types match
		if (!output) { //if output is 'pwd_err_output, then output is it.
			fprintf(stderr, "match error: %s\n", buf);
		} else {
			output((const char*)buf);
		}
		return 1;
	}
	
	fprintf(stderr, "match successfull\n");
	pcre2_code_free_8(reg_ret);
	return 0;
}
