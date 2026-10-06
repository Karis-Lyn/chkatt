/*
 * process user data malipulation
 * for example query a user, insert user data
 * */
#include <mysql.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../../public/global.h"

MYSQL* g_db_handle;

bool create_acount() {

	return 1;
}

bool drop_acount() {
  	return 1;
}


bool user_add(char* nam, char* pwd_hash, char* salt) {
	MYSQL_BIND bind[3];
	MYSQL_STMT* stmt_obj;
	const char* stmt_errors;
	const char* addtion = "insert into usr_info(usr_name, pwd_hash, salt, last_seen, created_at) "
		"values (?, ?, ?, now(), now())";

	while (mysql_next_result(g_db_handle) == 0) {
		MYSQL_RES* res = mysql_store_result(g_db_handle);
		if (res) mysql_free_result(res);
	}

	stmt_obj = mysql_stmt_init(g_db_handle);
	if (!stmt_obj) {
		fprintf(stderr, "stmt_init failed: %s\n", mysql_error(g_db_handle));
		return 0;
	}

	if (mysql_stmt_prepare(stmt_obj, addtion, strlen(addtion))) {
		fprintf(stderr, "stmt_prepare failed: %s\n", mysql_stmt_error(stmt_obj));
		mysql_stmt_close(stmt_obj);
		return 0;
	}

	memset(bind, 0, sizeof(bind));

	bind[0].buffer = nam;
	bind[0].buffer_type = MYSQL_TYPE_STRING;
	bind[0].buffer_length = strlen(nam);

	bind[1].buffer = pwd_hash;
	bind[1].buffer_type = MYSQL_TYPE_STRING;
	bind[1].buffer_length = strlen(pwd_hash);

	bind[2].buffer = salt;
	bind[2].buffer_type = MYSQL_TYPE_STRING;
	bind[2].buffer_length = strlen(salt);

	if (mysql_stmt_bind_param(stmt_obj, bind)) {
		fprintf(stderr, "stmt_bind_param failed: %s\n", mysql_stmt_error(stmt_obj));
		mysql_stmt_close(stmt_obj);
		return 0;
	}

	if (mysql_stmt_execute(stmt_obj)) {
		stmt_errors = mysql_stmt_error(stmt_obj);
		fprintf(stderr, "add is acount failed [%s]\n", stmt_errors);
		mysql_stmt_close(stmt_obj);
		return 0;
	}

	mysql_stmt_close(stmt_obj);
	return 1;
}

bool destory_mysql() {
	if (g_db_handle) {
		mysql_close(g_db_handle);
		g_db_handle = NULL;
		return 1;
	}
	return 0;
}

bool run_mysql(
		char* host,
	  	char* user,
	  	char* pwd,
		char* db,
		uint64_t port
		) {

	const int8_t MAX_RETRIES = 10;

	g_db_handle = mysql_init(NULL);

	my_bool reconnect = 1;
	mysql_options(g_db_handle, MYSQL_OPT_RECONNECT, &reconnect);

	unsigned int ssl_enforce = 0;
	mysql_options(g_db_handle, MYSQL_OPT_SSL_ENFORCE, &ssl_enforce);

	mysql_options(g_db_handle, MYSQL_SET_CHARSET_NAME, "utf8mb4");

	for (int8_t i = 0; i < MAX_RETRIES; i++) {
		if (mysql_real_connect(
				g_db_handle,
				host,
				user,
				pwd,
				db,
				port,
				NULL,
				CLIENT_MULTI_STATEMENTS)) {
			return 1;
		}
		fprintf(stderr, "Connection attempt %d failed: %s\n", i + 1, mysql_error(g_db_handle));
		sleep(1);
	}

	fprintf(stderr, "connectting database failed after %d retries: %s\n", MAX_RETRIES, mysql_error(g_db_handle));
	return 0;
}
