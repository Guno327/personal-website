FROM alpine:latest

WORKDIR /app
COPY . .

RUN apk update
RUN apk add make go ts

RUN go build website.go

EXPOSE 8080
CMD ["/app/website"]
