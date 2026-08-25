CXX = g++
CXXFLAGS = -O3 -std=c++20 -pthread -Wall -Wextra

TARGET = vacuum_phase_engine.exe
SRC = vacuum_phase_engine.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

smoke: $(TARGET)
	./$(TARGET) --smoke-test

clean:
	rm -f $(TARGET) *.csv
