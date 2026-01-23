#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <regex.h>
#include <string.h>
#include <stdbool.h>
#include <stdarg.h>

// 定义迭代器状态结构
typedef struct {
	int32_t* data;
	bool     has_next;
	int32_t  curr;
	int32_t  count;  // 添加计数
	int32_t  index;  // 当前索引
} Iterator;

// 修改next函数使其接受迭代器指针
int32_t next(Iterator* it) {
	if (it->index < it->count) {
		int32_t result = it->data[it->index];
		it->index++;
		it->has_next = (it->index < it->count);
		return result;
	}
	it->has_next = false;
	return 0; // 表示没有更多元素
}

int16_t bits_add(
		const int16_t num,
		const uint8_t i) {
	return num | 1 << i;
}

int16_t bits_remove(
		const int16_t num,
		const uint8_t i) {
	return num & ~(1 << i);
}

int16_t bits_revert(
		const int16_t num,
		const uint8_t i) {
	return num ^ 1 << i;
}

bool bits_contain(
		const int16_t num,
		const uint8_t i) {
	return num >> i & 1 ? 1 : 0;
}

static int8_t calc_str_len(
		const char* restrict str) {
#define BIT_C 'b'
#define END_C '\0'

	regex_t reg;
	int8_t has_comp;
	char* pat = "";
	int8_t ret = 0;
	char* chr = "";

	// verify has correct format.
	pat = "^[0-9]+b([[:space:]]*[0-9]+b)*$";
	has_comp = regcomp(&reg, pat, REG_EXTENDED);
	// has_comp: 0 -> successful
	// has_comp: 1 -> faild
	if (has_comp) return 1;
	ret = regexec(&reg, str, 0, NULL, 0);
	// ret: 0 -> successful
	// ret: 1 -> faild
	if (ret) {
		printf("failed\n");
		return 1;
	}
	regfree(&reg);
	ret = 0;
	// get str len
	do {
		chr = strchr(str, BIT_C);
		ret++;
		chr += 1;
		str = chr;
	} while(*chr != END_C);
#undef BIT_C
	return ret;
}

char* duplict_str(const char* restrict str) {
#define SPACE_C ' '
#define END_C '\0'
#define RET_PREFIX_S "0b"

	int8_t len = strlen(str);
	char* ret = (char*) malloc(len + 1);
	int8_t j = 0;
	if (ret == NULL) return NULL;
	for (int8_t i = 0; i < len; i++) {
		if (str[i] != SPACE_C) {
			ret[j] = str[i];
			j++;
		}
	}
	ret[j] = END_C;
#undef SPACE_C
#undef END_C
#undef RET_PREFIX_S
	return ret;
}

int32_t bits_pack(
		const char* restrict field,
		...
		) {
#define FIELD_DELIM "b"

	va_list args;
	int32_t mix = 0;
	char* buf = duplict_str(field); // duplicted string
	int8_t len = calc_str_len(buf);
	char* it = strtok(buf, FIELD_DELIM); //split string
	int8_t bits = 0;
	int32_t num = 0;

	va_start(args, field);
	for (int8_t i = 0; i < len; i++) {
		num = va_arg(args, int);
		mix |= (num << bits); // bits: 0
		if (it == NULL) continue;
		bits += atoi(it);
		it = strtok(NULL, FIELD_DELIM);
	}
	va_end(args);
	free(buf);
	buf = NULL;
#undef FIELD_DELIM
	return mix;
}

void bits_unpack(
		int32_t mix, 
		char* restrict field,
		Iterator* it
		) {
	// 释放之前的数据
	if (it->data != NULL) {
		free(it->data);
	}

	char* buf = duplict_str(field);
	int8_t len = calc_str_len(buf);
	it->data = (int32_t*)malloc(len * sizeof(int32_t));
	it->count = len;

	char* it_field = strtok(buf, "b");
	int8_t bits = 0;
	int32_t mask = 0;

	// 计算每个字段的位数并提取对应的值
	for (int8_t i = 0; i < len; i++) {
		int field_bits = atoi(it_field);
		mask = (1 << field_bits) - 1;  // 创建掩码
		it->data[i] = (mix >> bits) & mask;  // 提取对应位的值
		bits += field_bits;
		it_field = strtok(NULL, "b");
	}

	// 初始化迭代器
	it->has_next = (len > 0);
	it->curr = 0;
	it->index = 0;

	free(buf);
	buf = NULL;
}

