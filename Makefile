.PHONY : clean all
LIST_SRC = src/user.c src/bits.c src/dbctrl.c
LIST_SRC := $(sort $(LIST_SRC))
LIBS = $(patsubst src/%.c, lib/lib%.so, $(LIST_SRC))
OBJS_C = $(LIST_SRC:.c=.o)
LINK_OBJ = mariadb
MARIADB_HEAD_PATH = /usr/include/mariadb

all :  $(LIBS)

$(LIBS) : lib/lib%.so : src/%.o
	gcc -shared -o $@ $< -l${LINK_OBJ}

$(OBJS_C): %.o : %.c
	gcc -c -fPIC -o $@ $< -I${MARIADB_HEAD_PATH}

cp_libs:
	sudo cp -v $(LIBS) /usr/local/lib

ldconfig:
	@sudo ldconfig

start_client:
	@python3 src/client.py
start_server:
	@python3 src/server.py

clean:
	@rm -fv src/*.o #*.c
