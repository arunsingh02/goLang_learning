package practice

import "fmt"

func StructLearn() {
	// struct in GoLang
	// No class concept, no inheritence and no super/parent

	fmt.Println("Learning struct")

	vivaan := User{"Vivaan", 01, "vivaan@google.ceo", true}

	fmt.Printf("User vivaan details : %+v\n", vivaan)
	fmt.Printf("Name %v and Email %v of vivaan user.\n", vivaan.Name, vivaan.Email)

	fmt.Println("Status : ", vivaan.Status)

	vivaan.SetStatus(&vivaan.Status)

	fmt.Println("Updated Status : ", vivaan.Status)
}

// Basic struct definition
// ** Caps U in User struct type means User is the public type.
type User struct {
	Name   string // Caps N in Name
	Age    int
	Email  string
	Status bool
}

// Status is not upadting
// not the refrence, only copy of the object
func (u User) SetStatus(Status *bool) {
	u.Status = false
	fmt.Println("Set Status : ", u.Status)
}

/*
Learning struct
User vivaan details : {Name:Vivaan Age:1 Email:vivaan@google.ceo Status:true}
Name Vivaan and Email vivaan@google.ceo of vivaan user.
Status :  true
Set Status :  false
Updated Status :  true
*/
