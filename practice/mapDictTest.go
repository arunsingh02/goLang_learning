package main

import "fmt"

func main() {
	// maps in golang
	// Un-Ordered dictonaries

	languages := make(map[int]string)
	languages[1] = "Python"
	languages[2] = "Ruby"
	languages[3] = "JS"
	languages[13] = "JS20"
	languages[32] = "JS1"
	languages[23] = "JS2"
	languages[33] = "JS3"
	languages[43] = "JS4"
	languages[35] = "JS5"
	languages[34] = "JS6"
	languages[36] = "JS7"

	fmt.Println("Languages : ", languages)

	fmt.Println("JS : ", languages[3])

	delete(languages, 23)

	for key, value := range languages {
		fmt.Printf("For key %v the value is %v\n", key, value)
	}
}

/*
Languages :  map[1:Python 2:Ruby 3:JS 13:JS20 23:JS2 32:JS1 33:JS3 34:JS6 35:JS5 36:JS7 43:JS4]
JS :  JS
For key 36 the value is JS7
For key 2 the value is Ruby
For key 3 the value is JS
For key 32 the value is JS1
For key 35 the value is JS5
For key 43 the value is JS4
For key 34 the value is JS6
For key 1 the value is Python
For key 13 the value is JS20
For key 33 the value is JS3
*/
