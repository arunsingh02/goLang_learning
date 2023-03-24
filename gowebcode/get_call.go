package main

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

// Check error
func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

// Perform GET call
func PerformGet() {
	const url string = "http://localhost:8000/get"
	resp, err := http.Get(url)
	CheckError(err)

	defer resp.Body.Close()
	fmt.Println("response status code : ", resp.StatusCode)
	if resp.StatusCode != 200 {
		panic("Get call failed")
	}

	content, err := io.ReadAll(resp.Body)
	CheckError(err)
	fmt.Println("Total lent of content : ", resp.ContentLength)
	if len(content) < 100 {
		var responsefactory strings.Builder
		byteCount, _ := responsefactory.Write(content)

		// We can add string
		// b, _ := responsefactory.WriteString("Hi I am arunsingh")

		fmt.Println("Total byte count : ", byteCount)

		fmt.Println(responsefactory.String())

		//fmt.Println(string(content))
	} else {
		fmt.Println("Please try again..")
	}
}

// Main function
func main() {
	fmt.Println("Web GET caller - arunsingh02")
	PerformGet()
}

/*
Web GET caller - arunsingh02
response status code :  200
Total lent of content :  52
Total byte count :  52
{"message":"Hello from arunsingh02 github account."}
*/
