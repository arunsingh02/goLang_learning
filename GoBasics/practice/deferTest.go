// Using defer
// Last In First Out

package practice

import "fmt"

func Defer() {
	defer fmt.Println("World")
	fmt.Println("One")
	defer fmt.Println("\nTwo")
	fmt.Println("Hello")
	// this is execute after Hello because
	// currently it will not aware about defer in function
	CheckDefer()
}

// Output should be
// One Hello Two World

func CheckDefer() {
	for i := 0; i < 5; i++ {
		defer fmt.Print(i)
	}
}

// Output should be
// One Hello 43210 Two World

/*
One
Hello
43210
Two
World
*/
