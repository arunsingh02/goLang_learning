// Array, Slices example

package practice

import (
	"fmt"
	"sort"
)

func MemPlay() {
	// Array example (memory is fixed)
	var colors [3]string
	colors[0] = "choco"
	colors[1] = "orange"
	colors[2] = "brown"
	fmt.Println(colors)

	pages := [5]int{2, 3, 4, 5, 6}
	fmt.Println("array : ", pages)
	//./memory.go:19:16: first argument to append must be slice; have [5]int
	// pages = append(pages, 23)

	// slices (memory not fixed)
	slice_pages := []int{54, 32, 76, 54, 6876, 42, 4}
	fmt.Println("slice : ", slice_pages)
	slice_pages = append(slice_pages, 23)
	fmt.Println(slice_pages)
	// No return
	sort.Ints(slice_pages)
	fmt.Println("Sorted value : ", slice_pages)

	// make object for memory creation and intilize
	// panic: runtime error: index out of range [0] with length 0
	// (2nd input in make function)
	// number := make([]string, 0, 5)
	names := make([]string, 5)
	names[0] = "aa"
	names[1] = "bb"
	names[2] = "aaa"
	names[3] = "bbb"
	fmt.Println(names)

	names = append(names, "el")
	names = append(names, "elf")
	names = append(names, "eld")
	names = append(names, "elff")
	fmt.Println(names)
	// indexing
	fmt.Println(names[5])
}

/*
[choco orange brown]
array :  [2 3 4 5 6]
slice :  [54 32 76 54 6876 42 4]
[54 32 76 54 6876 42 4 23]
Sorted value :  [4 23 32 42 54 54 76 6876]
[aa bb aaa bbb ]
[aa bb aaa bbb  el elf eld elff]
el
*/
