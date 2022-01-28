package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter Text : ")
	input, _ := reader.ReadString('\n')
	fmt.Print("Your input is : ", input)

}
