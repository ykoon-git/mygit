CC = gcc 

prog = main.o foo.o
	&(CC) -o $@ main.o foo.o

%.o : %.c
	&(CC) -c -o $@ ${CFLAG} $<


clean :
	rm -f prog main.o foo.o
