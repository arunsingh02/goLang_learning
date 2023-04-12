package main

import (
	"fmt"

	"example.com/greetings"
)

func main() {
	// Get a greeting message and print it.
	message := greetings.Hello("Arun")
	fmt.Println(message)
}

/*
go run .                                                          ─╯
Hi, Arun. Welcome!
*/
