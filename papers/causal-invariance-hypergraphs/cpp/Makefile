CXX = g++
CXXFLAGS = -O3 -std=c++20 -pthread -Wall -Wextra -march=native

TARGET = causal_invariance_engine.exe
SRC = causal_invariance_engine.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

smoke: $(TARGET)
	./$(TARGET) --smoke-test

benchmark: $(TARGET)
	./$(TARGET) --benchmark

clean:
	rm -f $(TARGET) *.csv
