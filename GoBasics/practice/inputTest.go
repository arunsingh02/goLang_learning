package practice

import (
	"bufio"
	"fmt"
	"os"
)

func TakeInput() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter Text : ")
	input, _ := reader.ReadString('\n')
	fmt.Print("Your input is : ", input)

}
