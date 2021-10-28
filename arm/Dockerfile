ARG ARCH=
FROM ${ARCH}debian:buster-slim AS builder 
RUN apt update && apt install -y build-essential
WORKDIR /home
COPY hello.c .
RUN gcc "-DARCH=\"`uname -a`\"" hello.c -o hello



FROM ${ARCH}debian:buster-slim 
WORKDIR /home
COPY --from=builder /home/hello .
ENTRYPOINT ["./hello"] 