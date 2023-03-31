package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func sayHello() {
	fmt.Println("Hello, how are you?")
}

func serveInfo(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1> Welcome in Arun's Page <h1>"))
}

func main() {
	fmt.Println("Module in GoLang")
	r := mux.NewRouter()
	sayHello()
	r.HandleFunc("/", serveInfo).Methods("GET")
	log.Fatal(http.ListenAndServe(":4000", r))
	// http.Handle("/", r)
}

/*
>> history
go mod init github.com/arunsingh02/mymodule
- Created go.mod file
go get -u github.com/gorilla/mux
- Updated the go.mod (require github.com/gorilla/mux v1.0.8 //indirect)
go build .
go run .
go mod tidy
- sync the module with dependencies
go mod verify
- verify the modules
go list
- show all dependent modules
go list -m all
- show only your modules
go mod graph
- show the modules graph
go list -m -versions github.com/gorilla/mux
- All published version of gorilla/mux
go mod why github.com/gorilla/mux
- Show where we are using this module
go mod vendor
- Download the module locally
go run -mod=vendor main.go
- dependencies will find out first in locally downloaded package and then go to web.

... Lot more, Please use this reference:
https://go.dev/ref/mod
*/
