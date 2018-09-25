CC = gcc
EXEC_NAME = exec

execute: $(EXEC_NAME)
	./$(EXEC_NAME)

$(EXEC_NAME): script.o
	$(CC) script.c -o $(EXEC_NAME)

script.o: script.c
	$(CC) -c script.c

clean:
	rm -r __pycache__ .pytest_cache *.o $(EXEC_NAME)
