package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/arunsingh02/mongoAPI/router"
)

func main() {
	fmt.Println("Play with mongo DB")
	r := router.Router()
	log.Fatal(http.ListenAndServe(":4000", r))
}

// mongodb+srv://arunsingh02:<password>@cluster0.tkqh4up.mongodb.net/?retryWrites=true&w=majority
