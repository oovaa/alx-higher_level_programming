CC = gcc
CFLAGS = -Wall -Werror -Wextra -pedantic -std=c99
LDFLAGS = -shared -fPIC
LIBS = -I/usr/include/python3.10

TARGET = libPython.so
SOURCE = 103-python.c

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) $(LDFLAGS) $(LIBS) -o $@ $<

clean:
	rm -f $(TARGET)

.PHONY: all clean
