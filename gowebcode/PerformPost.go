package PerformGet

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

func PerformPost() {
	fmt.Println("Performing POST")
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

func main() {
	fmt.Println("Web POST call : arunsingh02")
	PerformPost()
}

/*
Web POST call : arunsingh02
Performing POST
Content :  {"name":"arun singh","address":"Karnataka"}
*/
