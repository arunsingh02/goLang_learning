// prepare un-ordered map (key : value pair)

package main

import (
	"fmt"
	"sort"
)

func main() {
	// declaration of map (un-ordered dict)
	dict := make(map[string]string)
	dict["firstname"] = "Arun"
	dict["lastname"] = "Singh"
	dict["address"] = "Basti"
	dict["pin"] = "272001"
	fmt.Println(dict)
	// Collecting value from map
	State := dict["address"]
	fmt.Println(State)
	// deleting key value pair in map
	delete(dict, "pin")
	fmt.Println(dict)

	// Reading key and value of map
	for key, value := range dict {
		fmt.Printf("%v : %v\n", key, value)
	}
	// Collecting all keys in slice object
	keys := make([]string, len(dict)) // allocates mem and init (slices)
	i := 0
	// Iterating for loop
	for key := range dict {
		keys[i] = key // putting values on gven mem
		i++
	}

	for i := range keys {
		fmt.Println(dict[keys[i]]) // printing values
	}

	sort.Strings(keys)
	fmt.Println(keys)
}

/*
map[address:Basti firstname:Arun lastname:Singh pin:272001]
Basti
map[address:Basti firstname:Arun lastname:Singh]
firstname : Arun
lastname : Singh
address : Basti
Arun
Singh
Basti
[address firstname lastname]
*/
