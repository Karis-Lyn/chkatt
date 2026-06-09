.PHONY : clean all
#vpath %.py src/client
#vpath %.py src/server
#vpath %.py src/client/ui
#vpath %.py src/server/handlers
server := src.server.server
client := src.client.client
build:
	@meson compile -C build
	@meson install -C build

start_server : 
	python3 -m $(server)

start_client :
	python3 -m $(client)

clean:
	@rm -fv src/*.o #*.c
