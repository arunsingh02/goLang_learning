// struct type in go

package practice

import "fmt"

// This is Dog struct and here we can add different types of data
// Capital C in Dog, to make this struct public. So we can use through out this file.
// Dog is struct
type Dog struct {
	weight int
	breed  string
	color  string
}

func CheckStructTyped() {
	// Struct obj initialization (constructor)
	bombay_dog := Dog{6, "Bombay", "Brown"}
	fmt.Println(bombay_dog)

	fmt.Printf("%+v\n", bombay_dog)

	fmt.Printf("My dog color is %v\n", bombay_dog.color)
	bombay_dog.weight = 7
	fmt.Printf("color: %v\nweight: %v\nbreed: %v\n\n",
		bombay_dog.color, bombay_dog.weight, bombay_dog,
	)
	// Initializing new object with same struct types
	birman_dog := Dog{4, "Birman", "White"}
	fmt.Println(birman_dog)

	fmt.Printf("%+v\n", birman_dog)

	fmt.Printf("My dog color is %v\n", birman_dog.color)
	birman_dog.weight = 5
	fmt.Printf("color: %v\nweight: %v\nbreed: %v\n",
		birman_dog.color, birman_dog.weight, birman_dog.breed,
	)
}

/*
{6 Bombay Brown}
{weight:6 breed:Bombay color:Brown}
My dog color is Brown
color: Brown
weight: 7
breed: Bombay

{4 Birman White}
{weight:4 breed:Birman color:White}
My dog color is White
color: White
weight: 5
breed: Birman
*/
