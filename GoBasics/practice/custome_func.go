// Add custom functions

package practice

import (
	"fmt"
)

type Person struct {
	name string
	age  int
}

func CheckCoustomFuction() {
	doNothing()
	sum := addValues(12, 23)
	fmt.Println("Toatl sum : ", sum)

	multiSum, multiCount := addMultiValues(21, 321, 3, 21, 22)
	fmt.Println("Total sum of multi val : ", multiSum)
	fmt.Println("Toatl val count : ", multiCount)
	ParseMultiValues(1, Person{
		"arun",
		21,
	}, "Great")
}

// Custom functions
func doNothing() {
	fmt.Println("I am not doing anything.")
}

// func <function-name>(<args-name> <type>, <a> <t>, ..) (<return-type>, <r-t>) {}
func addValues(val1, val2 int) int {
	return val1 + val2
}

// ... like *args in pyhton. Handle more values with one arg
// values is slices
// all args will be in int type only
func addMultiValues(values ...int) (int, int) {
	total := 0
	for _, val := range values {
		total += val
	}
	return total, len(values)
}

// Args will be any type
func ParseMultiValues(args ...interface{}) {
	fmt.Println("Args will be any type (Interface)")
	for _, arg := range args {
		fmt.Printf("Type of arg is %T and value is %v \n", arg, arg)
	}

}

/*
I am not doing anything.
Toatl sum :  35
Total sum of multi val :  388
Toatl val count :  5
Args will be any type (Interface)
Type of arg is int and value is 1
Type of arg is practice.Person and value is {arun 21}
Type of arg is string and value is Great
*/
