package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
)

// Check error
func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

func PerformPostForm() {
	const URL string = "http://localhost:8000/postform"

	requestBody := url.Values{}
	requestBody.Add("name", "Arun Singh")
	requestBody.Add("add", "Karnataka")
	requestBody.Add("designation", "SSW")

	// requestBody should be in url.Values format
	resp, err := http.PostForm(URL, requestBody)
	CheckError(err)

	defer resp.Body.Close()

	content, err := io.ReadAll(resp.Body)
	fmt.Printf("%s\n", content)

}

func main() {
	fmt.Println("Performing Post Form")
	PerformPostForm()

}

/*
Performing Post Form
{"add":"Karnataka","designation":"SSW","name":"Arun Singh"}
*/
