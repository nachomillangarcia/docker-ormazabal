FROM gcc AS build

WORKDIR /app

RUN apt update && apt install -y cmake

COPY CMakeLists.txt CMakeLists.txt 

COPY main.cpp main.cpp

RUN cmake . && make


FROM ubuntu

COPY --from=build /app/helloworld ./helloworld

CMD ["./helloworld"]
