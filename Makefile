CC=g++
CFLAGS= -g -std=c++11 -Wall -lwiringPi
SDIR = .
ODIR = .
BIN = .
SOURCES = LPD8806.cpp testLPD8806.cpp
OBJS = $(patsubst %.cpp, $(ODIR)/%.o, $(SOURCES) )
EXECUTABLE = $(BIN)/testLPD8806

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

$(ODIR)/%.o: $(SDIR)/%.cpp 
	$(CC) $(CFLAGS) -c $< -I$(SDIR) -o $@

.PHONY: all clean 

clean:
	rm -rf $(EXECUTABLE) $(OBJS)
