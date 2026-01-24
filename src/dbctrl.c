#include <mysql.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "global.h"

MYSQL* g_db_handle;

bool create_acount() {

	return 1;
}

bool drop_acount() {
  	return 1;
}

bool check_acount() {
	return 1;
}


Client* user_add(char* nam, char* pwd_key, char* salt) {
	Client* client = (Client*) malloc(sizeof(Client));
	MYSQL_BIND bind[3];
	MYSQL_STMT* stmt_obj;
	const char* stmt_errors;
	const char* addtion = "insert into usr_info(usr_name, pwd_hash, salt, last_seen, created_at) "
		"values (?, ?, ?, now(), now())";


	stmt_obj = mysql_stmt_init(g_db_handle);
	mysql_stmt_prepare(stmt_obj, addtion, strlen(addtion));
	memset(bind, 0, sizeof(bind));

	bind[0].buffer = nam;
	bind[0].buffer_type = MYSQL_TYPE_STRING;
	bind[0].buffer_length = strlen(nam);

	bind[1].buffer = pwd_key;
	bind[1].buffer_type = MYSQL_TYPE_STRING;
	bind[1].buffer_length = strlen(pwd_key);

	bind[2].buffer = salt;
	bind[2].buffer_type = MYSQL_TYPE_STRING;
	bind[2].buffer_length = strlen(salt);

	mysql_stmt_bind_param(stmt_obj, bind);

	if (mysql_stmt_execute(stmt_obj)) {
		stmt_errors = mysql_stmt_error(stmt_obj);
		fprintf(stderr, "add is acount failed [%s]\n", stmt_errors);
		mysql_stmt_close(stmt_obj);
		stmt_obj = NULL;
	}
	
	//memcpy(, const void *restrict src, size_t n)
	// done
	mysql_stmt_close(stmt_obj);
	stmt_obj = NULL;
	
	return client;
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

	g_db_handle = mysql_init(NULL);

	mysql_real_connect(
			g_db_handle,
			host,
			user,
			pwd,
			db,
			port,
			NULL,
			0);

	if (g_db_handle == NULL) {
		fprintf(stderr, "connectting database failed\n");
		return 0;
	}

	return 1;
}
