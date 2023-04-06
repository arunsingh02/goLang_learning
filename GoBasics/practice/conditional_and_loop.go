// conditional (if else, switch case) and loop example

package practice

import (
	"fmt"
	"math/rand"
	"time"
)

func CheckConditionWithLoop() {
	number := 42
	if number < 40 {
		fmt.Println("This is small number")
	} else if number == 40 {
		fmt.Println("This is equal number")
	} else {
		fmt.Println("This is greater number")
	}
	fmt.Println("Time in unix : ", time.Now().UnixNano())
	rand.Seed(time.Now().Unix())
	// dow := rand.Intn(7) + 1
	// fmt.Println("Day ", dow)

	switch dow := rand.Intn(7) + 1; dow {
	case 1:
		fmt.Println("Today is monday!")
		// fallthrough
	case 2:
		fmt.Println("Today is sunday!")
		// fallthrough
	case 5:
		fmt.Println("Today is Friday!")
		// fallthrough
	default:
		fmt.Println("Some another day!")
	}
	// Array
	colors := [5]string{"red", "blue", "pink", "choco", "white"}
	for i := 0; i < len(colors); i++ {
		fmt.Println(colors[i])
	}

	for i := range colors {
		fmt.Println(colors[i])
	}

	value := 1
	for value < 10 {
		fmt.Println(value)
		value++
		if value > 8 {
			goto theFinish
		}
	}

	// If we right this goto func at the end so in-middle functions/statements will skip.
theFinish:
	fmt.Println("This is the end of for loop era.")

	for _, color := range colors {
		fmt.Println(color)
	}

}
