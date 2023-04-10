package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

/*
Goroutines can be thought of as a lightweight thread that has a separate independent execution and which
can execute concurrently with other goroutines. (GoRoutines thread block size 8kb and Java thread block size ~1Mb)
It is a function or method that is executing concurrently with other goroutines.
It is entirely managed by the GO runtime. Golang is a concurrent language.
Each goroutine is an independent execution.  It is goroutine that helps achieve concurrency in golang
*/

var wg sync.WaitGroup

var mt sync.Mutex

var signals []string

var links = [3]string{
	"https://netapp.com",
	"https://go.dev",
	"https://google.com",
}

func main() {
	fmt.Println("Start Go Routines")
	go print_string("Hello")
	// Add adds delta, which may be negative, to the WaitGroup counter.
	// If the counter becomes zero, all goroutines blocked on Wait are released.
	// If the counter goes negative, Add panics.
	wg.Add(1)

	for _, link := range links {
		go Caller(link)
		wg.Add(1)
	}

	// time.Sleep(1 * time.Second)
	fmt.Println("Done Go Routines")
	wg.Wait()
	fmt.Println(signals)
}

func print_string(word string) {
	fmt.Println(word)
	defer wg.Done()
}

func Caller(url string) {
	defer wg.Done()
	resp, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	} else {
		mt.Lock()
		signals = append(signals, url)
		mt.Unlock()
		fmt.Printf("URL %s and Status is %d \n", url, resp.StatusCode)
	}
}

/*
Start Go Routines
Done Go Routines
Hello
URL https://go.dev and Status is 200
URL https://google.com and Status is 200
URL https://netapp.com and Status is 200
[https://go.dev https://google.com https://netapp.com]
*/
