CC=g++
CFLAGS= -g -std=c++11 -Wall -lwiringPi
SDIR = .
ODIR = .
BIN = .
SOURCES = LPD8806.cpp testLPD8806.cpp transitionLEDs.cpp
OBJS = $(patsubst %.cpp, $(ODIR)/%.o, $(SOURCES) )
EXECUTABLE = $(BIN)/testLPD8806 $(BIN)/transitionLEDs

all: $(EXECUTABLE)

testLPD8806: testLPD8806.o LPD8806.o 
	$(CC) $(CFLAGS) $^ -o $@

transitionLEDs: transitionLEDs.o LPD8806.o
	$(CC) $(CFLAGS) $^ -o $@

$(ODIR)/%.o: $(SDIR)/%.cpp 
	$(CC) $(CFLAGS) -c $< -I$(SDIR) -o $@

.PHONY: all clean 

clean:
	rm -rf $(EXECUTABLE) $(OBJS)
