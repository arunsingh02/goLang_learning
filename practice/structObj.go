// struct type in go

package main

import "fmt"

// This is Cat struct and here we can add different types of data
// Capital C in Cat, to make this struct public. So we can use through out this file.
// Cat is struct
type Cat struct {
	weight int
	breed  string
	color  string
}

func main() {
	// Struct obj initialization (constructor)
	bombay_cat := Cat{6, "Bombay", "Brown"}
	fmt.Println(bombay_cat)

	fmt.Printf("%+v\n", bombay_cat)

	fmt.Printf("My cat color is %v\n", bombay_cat.color)
	bombay_cat.weight = 7
	fmt.Printf("color: %v\nweight: %v\nbreed: %v\n\n",
		bombay_cat.color, bombay_cat.weight, bombay_cat.breed,
	)
	// Initializing new object with same struct types
	birman_cat := Cat{4, "Birman", "White"}
	fmt.Println(birman_cat)

	fmt.Printf("%+v\n", birman_cat)

	fmt.Printf("My cat color is %v\n", birman_cat.color)
	birman_cat.weight = 5
	fmt.Printf("color: %v\nweight: %v\nbreed: %v\n",
		birman_cat.color, birman_cat.weight, birman_cat.breed,
	)
}

/*
{6 Bombay Brown}
{weight:6 breed:Bombay color:Brown}
My cat color is Brown
color: Brown
weight: 7
breed: Bombay

{4 Birman White}
{weight:4 breed:Birman color:White}
My cat color is White
color: White
weight: 5
breed: Birman
*/
