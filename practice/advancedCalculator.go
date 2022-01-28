// Advanced calculator for Mac

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Value 1 : ")
	inp1, _ := reader.ReadString('\n')
	val1, err := strconv.ParseFloat(strings.TrimSpace(inp1), 64)
	checkErr(err)

	fmt.Print("Value 2 : ")
	inp2, err := reader.ReadString('\n')
	val2, err := strconv.ParseFloat(strings.TrimSpace(inp2), 64)
	checkErr(err)

	fmt.Print("Select an operator (+, -, *, /) : ")
	inp3, _ := reader.ReadString('\n')
	checkErr(err)

	switch strings.TrimSpace(inp3) {
	case "+":
		Add(val1, val2)
	case "-":
		Substract(val1, val2)
	case "*":
		Multiply(val1, val2)
	case "/":
		Division(val1, val2)
	default:
		fmt.Println("Please provide correct sign.")

	}
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func Add(val1, val2 float64) {
	sum := math.Round((val1+val2)*100) / 100
	fmt.Printf("Sum of %v and %v is %v\n", val1, val2, sum)
}

func Substract(val1, val2 float64) {
	subtract := math.Round((val1-val2)*100) / 100
	fmt.Printf("Substraction from %v to %v is %v\n", val1, val2, subtract)
}

func Multiply(val1, val2 float64) {
	mul := math.Round((val1*val2)*100) / 100
	fmt.Printf("Multiply of %v and %v is %v\n", val1, val2, mul)
}

func Division(val1, val2 float64) {
	div := math.Round((val1/val2)*100) / 100
	fmt.Printf("Division of %v from %v is %v\n", val1, val2, div)
}
