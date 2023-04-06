package router

import (
	"github.com/gorilla/mux"
)

func Router() {
	r := mux.NewRouter()
	r.HandleFunc("/", "<h1>Welcome in Mongo API</h1>")

}
