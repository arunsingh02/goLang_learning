package main

import "fmt"

const MAX int = 5

func main() {
	var ptr *int
	fmt.Println("Value in ptr", ptr)

	myNum := 10
	var newPtr *int = &myNum
	fmt.Println("myNum address : ", newPtr)
	fmt.Println("myNum value : ", *newPtr)

	*newPtr = *newPtr * 10
	fmt.Printf("updated myNum value 10 * 10 : %d \n", *newPtr)

	// passing pointers in function
	fmt.Println("** Passing pointers in function **")
	a := 10
	b := 20
	fmt.Println("Before swap a, b: ", a, b)
	// call by refrence
	swap(&a, &b)
	fmt.Println("After swap a, b: ", a, b)

	// pointer to pointer
	fmt.Println("** Pointer of Pointer **")
	data := 10
	var sptr *int

	sptr = &data
	// double pointer
	// |address| --> |address| --> |value|
	var pptr **int
	pptr = &sptr
	fmt.Printf("ptr address value: %x \n", sptr)
	fmt.Printf("pptr address value: %x \n", pptr)
	fmt.Printf("ptr address value: %d \n", **pptr)

	// Array of pointer
	var arr = [MAX]int{1, 2, 3, 4, 5}
	var arrPtr [MAX]*int // declaration of array of pointer
	fmt.Println("** Array of pointers **")
	for i := 0; i < MAX; i++ {
		arrPtr[i] = &arr[i] // storing the address
		fmt.Printf("Address for index %d : %x and value is %d \n", i, arrPtr[i], *arrPtr[i])
	}

}

// call by refrence
func swap(x *int, y *int) {
	temp := *x
	*x = *y
	*y = temp
}

/*
Value in ptr <nil>
myNum address :  0xc000122008
myNum value :  10
updated myNum value 10 * 10 : 100
** Passing pointers in function **
Before swap a, b:  10 20
After swap a, b:  20 10
** Pointer of Pointer **
ptr address value: c000122020
pptr address value: c00011a020
ptr address value: 10
** Array of pointers **
Address for index 0 : c000126030 and value is 1
Address for index 1 : c000126038 and value is 2
Address for index 2 : c000126040 and value is 3
Address for index 3 : c000126048 and value is 4
Address for index 4 : c000126050 and value is 5
*/
