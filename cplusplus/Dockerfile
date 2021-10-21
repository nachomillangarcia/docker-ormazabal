FROM gcc

WORKDIR /app

RUN apt update && apt install -y cmake

COPY CMakeLists.txt CMakeLists.txt 

COPY main.cpp main.cpp

RUN cmake . && make

CMD ["./helloworld"]
