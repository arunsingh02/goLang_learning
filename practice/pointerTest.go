package main

import "fmt"

func main() {
	var ptr *int
	fmt.Println("Value in ptr", ptr)

	myNum := 10
	var newPtr = &myNum
	fmt.Println("myNum address : ", newPtr)
	fmt.Println("myNum value : ", *newPtr)

	*newPtr = *newPtr * 10
	fmt.Printf("updated myNum value 10 * 10 : %d \n", *newPtr)
}

/*
Value in ptr <nil>
myNum address :  0xc0000b2008
myNum value :  10
updated myNum value 10 * 10 : 100
*/
