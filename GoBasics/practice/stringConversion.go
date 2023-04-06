package practice

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func StringConvert() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a number : ")
	anInput, _ := reader.ReadString('\n')
	aFloat, err := strconv.ParseFloat(strings.TrimSpace(anInput), 64)

	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("This is your float number : ", aFloat)
	}

	fmt.Println("Code will not stop after recieving error in goLang.")
}
