package main

import "fmt"

func main() {
	// struct in GoLang
	// No class concept, no inheritence and no super/parent

	fmt.Println("Learning struct")

	vivaan := User{"Vivaan", 01, "vivaan@google.ceo", true}

	fmt.Printf("User vivaan details : %+v\n", vivaan)
	fmt.Printf("Name %v and Email %v of vivaan user.\n", vivaan.Name, vivaan.Email)
}

// Basic struct definition
// ** Caps U in User struct type means User is the public type.
type User struct {
	Name   string // Caps N in Name
	Age    int
	Email  string
	Status bool
}
