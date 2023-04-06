// Variable in Go Lang
package practice

import "fmt"

const myConst int = 64

func VarPlay() {
	var myString string = "This is string"
	fmt.Println(myString)
	fmt.Printf("The variable's type is %T\n", myString)

	// explicit type
	var myInt int = 40
	fmt.Println(myInt)
	fmt.Printf("The variable's type is %T\n", myInt)

	fmt.Println(myConst)
	fmt.Printf("The variable's type is %T\n", myConst)

	// implicit type
	aString := "This is an another string"
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString)
}
