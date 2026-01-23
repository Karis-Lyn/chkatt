#ifndef GLOBAL_H
#define GLOBAL_H

#define USRA_LEN 16
#define PWDA_LEN 18
#ifdef _WIN32
	#include <windows.h>
	typedef HINSTANCE LibHandle;
	#define LOAD_LIB(path) LoadLibrary(path)
	#define GET_FUNC(lib, name) GetProcAddress(lib, name)
	#define FREE_LIB(lib) FreeLibrary(lib)
#else
	#include <dlfcn.h>
	typedef void* LibHandle;
	#define LOAD_LIB(path) dlopen(path, RTLD_LAZY)
	#define GET_FUNC(lib, name) dlsym(lib, name)
	#define FREE_LIB(lib) dlclose(lib)
#endif

typedef struct {
	char usr_nam[USRA_LEN];
	char usr_pwd[PWDA_LEN];
	int stat;
} User;

typedef struct {
	User* usr;
	int8_t sid: 4;
} Client;

#endif
