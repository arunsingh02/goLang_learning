// Calculator for Mac

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
	fmt.Println("This is Mac calculator.")
	// explicit variable type (with var and without :)
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	fmt.Print("First Value : ")
	input1, _ := reader.ReadString('\n')
	float1, err := strconv.ParseFloat(strings.TrimSpace(input1), 64)

	if err != nil {
		fmt.Println(err)
		panic("Please provide correct value.")
	}

	fmt.Print("Second Value : ")
	input2, _ := reader.ReadString('\n')
	float2, err := strconv.ParseFloat(strings.TrimSpace(input2), 64)

	if err != nil {
		fmt.Println(err)
		panic("Please provide correct value.")
	}

	sum := float1 + float2
	sum = math.Round(sum*100) / 100

	fmt.Printf("The sum of %v and %v is %v\n", float1, float2, sum)
}

/*
This is Mac calculator.
First Value : 12312.33232
Second Value : 21312.2312
The sum of 12312.33232 and 21312.2312 is 33624.56
*/
