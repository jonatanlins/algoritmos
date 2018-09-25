CC = gcc
EXEC_NAME = exec

execute: compile
	./$(EXEC_NAME)

compile: script.o
	$(CC) script.c -o $(EXEC_NAME)

script.o: script.c
	$(CC) -c script.c

clean:
	rm -r __pycache__ .pytest_cache *.o $(EXEC_NAME)
