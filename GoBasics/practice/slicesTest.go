package practice

import (
	"fmt"
	"sort"
)

func SlicePlay() {
	fmt.Println("Welcome in slices")

	var fruitList = []string{}
	fmt.Printf("Type of fruitList : %T\n", fruitList)

	var fruits = []string{"apple", "banana", "mango"}
	fmt.Println(fruits)

	fruits = append(fruits[1:])
	fmt.Println(fruits)

	var scores = make([]int, 4)
	scores[0] = 10
	scores[1] = 230
	scores[2] = 300
	scores[3] = 140
	// scores[4] = 90

	fmt.Println(scores)

	scores = append(scores, 80, 342, 298)

	fmt.Println(scores)

	sort.IntsAreSorted(scores)
	sort.Ints(scores)
	sort.IntsAreSorted(scores)
	fmt.Println(scores)

	// How to remove a value from slices with index
	var index int = 2
	/*
			Without use ...
			# command-line-arguments
		./slicesTest.go:40:17: cannot use scores[index + 1:] (type []int) as type int in append
	*/
	scores = append(scores[:index], scores[index+1:]...)
	fmt.Println(scores)
}

/*
Welcome in slices
Type of fruitList : []string
[apple banana mango]
[banana mango]
[10 230 300 140]
[10 230 300 140 80 342 298]
[10 80 140 230 298 300 342]
[10 80 230 298 300 342]
*/
