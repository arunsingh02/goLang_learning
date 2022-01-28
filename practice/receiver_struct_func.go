// receiver struct function

package main

import "fmt"

// Cat is struct
type Cat struct {
	weight int
	breed  string
	color  string
	sound  string
}

func main() {
	// Struct obj initialization (constructor)
	bombay_cat := Cat{6, "Bombay", "Brown", "Meow!"}
	fmt.Println(bombay_cat)

	fmt.Printf("%+v\n", bombay_cat)

	fmt.Printf("My cat color is %v\n", bombay_cat.color)

	bombay_cat.weight = 7
	fmt.Printf("color: %v\nweight: %v\nbreed: %v\n",
		bombay_cat.color, bombay_cat.weight, bombay_cat.breed,
	)
	bombay_cat.Speak()
	bombay_cat.SpeakLouder()
}

// Speak is how cat will sound
func (c Cat) Speak() {
	fmt.Println(c.sound)
}

// SpeakLouder is how the cat speaks louder
func (c Cat) SpeakLouder() {
	// Running with "non-name c.sound on left side of :=" error
	// c.sound := fmt.Sprintf("%v %v %v", c.sound, c.sound, c.sound)
	fmt.Printf("%v %v %v\n", c.sound, c.sound, c.sound)
}

/*
{6 Bombay Brown Meow!}
{weight:6 breed:Bombay color:Brown sound:Meow!}
My cat color is Brown
color: Brown
weight: 7
breed: Bombay
Meow!
Meow! Meow! Meow!
*/
