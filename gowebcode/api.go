package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

// Check error
func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

// Perform GET call - Controller
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
	fmt.Println("Total length of content : ", resp.ContentLength)
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

// Perform Post call - Controller
func PerformPost() {
	const URL string = "http://localhost:8000/post"

	/*
		This will not work as a POST requestBody, because there io.Reader obj is required
		data := make(map[string]string)
		data["name"] = "Arun Singh"
		data["add"] = "Karnataka"
		userData, err := json.MarshalIndent(data, "", "\t") // userData is in byte format
		fmt.Printf("DATA:  %s\n\n", userData)
	*/

	// Best way to prepare JSON data
	responseBody := strings.NewReader(`
		{
			"name":"arun singh",
			"address":"Karnataka"
		}
	`)

	resp, err := http.Post(URL, "application/json", responseBody)
	CheckError(err)

	defer resp.Body.Close()

	content, err := io.ReadAll(resp.Body)

	CheckError(err)

	fmt.Println("Content : ", string(content))

}

// Perform Post call with Form data as input - Controller
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

// Main function
func main() {
	fmt.Println("Performing Get")
	PerformGet()
	fmt.Println("Performing Post")
	PerformPost()
	fmt.Println("Performing PostForm")
	PerformPostForm()
}

/*
Performing Get
response status code :  200
Total length of content :  52
Total byte count :  52
{"message":"Hello from arunsingh02 github account."}
Performing Post
Content :  {"name":"arun singh","address":"Karnataka"}
Performing PostForm
{"add":"Karnataka","designation":"SSW","name":"Arun Singh"}
*/
