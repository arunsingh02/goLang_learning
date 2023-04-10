package practice

import (
	"fmt"
	"sync"
)

func HandleRaceCondition() {
	fmt.Println("Handle Race condition in golang")

	var counter = []int{0}

	wg := &sync.WaitGroup{}
	mt := &sync.Mutex{}

	wg.Add(3)
	// syntax of anonymous function in golang
	// func(args..){body...}(params...)

	go func(wg *sync.WaitGroup, m *sync.Mutex) {
		fmt.Println("First Goro")
		m.Lock()
		counter = append(counter, 1)
		m.Unlock()
		defer wg.Done()
	}(wg, mt)

	go func(wg *sync.WaitGroup, m *sync.Mutex) {
		fmt.Println("Second Goro")
		m.Lock()
		counter = append(counter, 2)
		m.Unlock()
		defer wg.Done()
	}(wg, mt)

	go func(wg *sync.WaitGroup, m *sync.Mutex) {
		fmt.Println("Third Goro")
		m.Lock()
		counter = append(counter, 3)
		m.Unlock()
		defer wg.Done()
	}(wg, mt)
	wg.Wait()

	mt.Lock()
	fmt.Println(counter)
	mt.Unlock()
}

/*
Without Mutex :

WARNING: DATA RACE
Read at 0x00c00020c198 by goroutine 6:
  runtime.growslice()
      /usr/local/go/src/runtime/slice.go:157 +0x0
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition.func1()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:21 +0xe4
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition.func4()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:23 +0x58

Previous write at 0x00c00020c198 by goroutine 8:
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition.func3()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:33 +0x10d
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition.func6()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:35 +0x58

Goroutine 6 (running) created at:
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:19 +0x304
  main.main()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/main.go:32 +0x6c

Goroutine 8 (finished) created at:
  github.com/arunsingh02/GoBasics/practice.HandleRaceCondition()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/practice/race_condition.go:31 +0x5ce
  main.main()
      /Users/arunsingh/Desktop/goLang_learning/GoBasics/main.go:32 +0x6c
==================
Found 2 data race(s)
exit status 66

*/

/*
With Mutex :

Caller function for all practice set
Handle Race condition in golang
Second Goro
Third Goro
First Goro
[0 2 3 1]
*/
