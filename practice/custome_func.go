// Add custom functions

package main

import "fmt"

func main() {
	doNothing()
	sum := addValues(12, 23)
	fmt.Println("Toatl sum : ", sum)

	multiSum, multiCount := addMultiValues(21, 321, 3, 21, 22)
	fmt.Println("Total sum of multi val : ", multiSum)
	fmt.Println("Toatl val count : ", multiCount)
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
func addMultiValues(values ...int) (int, int) {
	total := 0
	for _, val := range values {
		total += val
	}
	return total, len(values)
}

/*
I am not doing anything.
Toatl sum :  35
Total sum of multi val :  388
Toatl val count :  5
*/
