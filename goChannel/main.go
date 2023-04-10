/*
Channel is a data type in Go which provides synchrounization and communication between goroutines.
They can be thought of as pipes which is used by goroutines to communicate.
This communication between goroutines doesn’t require any explicit locks.
Locks are internally managed by channel themselves.
Channel along with goroutine makes the go programming language concurrent
*/

package main

import (
	"fmt"
	"sync"
)

func main() {
	fmt.Println("Channel in go lang")

	wg := &sync.WaitGroup{}
	// Declare channel
	var ch = make(chan int)

	// val := ch
	// fmt.Println(val)
	wg.Add(2)
	go func(ch <-chan int, wg *sync.WaitGroup) {
		fmt.Println("Reciever")
		fmt.Println(<-ch) // <-ch means reciever
		// A very important point to note about the receive operation is that a particular
		// value sent to the channel can only be received once in any of the goroutine
		// fmt.Println(<-ch)
		defer wg.Done()
	}(ch, wg)

	go func(ch chan<- int, wg *sync.WaitGroup) {
		fmt.Println("Sender") // chan<- means sender
		ch <- 5
		defer wg.Done()
	}(ch, wg)
	wg.Wait()
}

/*
Common Error:
Chennel in go lang
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan send]:
main.main()
        /Users/arunsingh/Desktop/goLang_learning/goChannel/main.go:18 +0x76
exit status 2
*/

/*
Passed:
Channel in go lang
Sender
Reciever
5
*/
