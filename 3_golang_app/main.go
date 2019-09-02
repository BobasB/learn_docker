package main

import (
	"fmt"
	"os"
)

var message string

func main() {
	message = os.Getenv("message")
	fmt.Println(message)
}
