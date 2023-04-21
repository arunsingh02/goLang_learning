/*
Function closures are nothing but an anonymous function that can access variables
declared outside the function and also retain the current value of those variables
between different function calls. Anonymous functions are functions that are not named.
*/

package practice

import (
	"fmt"
)

func ClosureCaller() {
	fmt.Println("Clousre in Go")
	modulus := calc_mod()
	modulus(-1)
	modulus(3)
	modulus(-5)
}

func calc_mod() func(int) int {
	count := 0
	return func(i int) int {
		if i < 0 {
			i = i * -1
		}
		count++
		fmt.Printf("modulus function called %d times\n", count)
		return i
	}
}

// IIF (Immediately Invoked function)
// IIF or Immediately Invoked Function are those function which can be defined and executed at the same time.
// A function can be invoked immediately by appending a () after the end brace of the function.

func CalcSquare() {
	squareof2 := func() int {
		return 2 * 2
	}()
	val := squareof2
	fmt.Println(val)
}
