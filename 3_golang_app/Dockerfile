FROM golang:alpine AS builder
ENV GOOS=linux GOARCH=amd64

RUN apk update

WORKDIR /app
COPY main.go .
RUN go mod init go_print_message \
    && go mod download \
    && go build


FROM alpine:latest
LABEL author="Bohdan Buhyl"
LABEL version=1.0

ENV message="This message inside GO app!!"

RUN apk --no-cache add ca-certificates
COPY --from=builder /app/go_print_message /app/

ENTRYPOINT ["/app/go_print_message"]