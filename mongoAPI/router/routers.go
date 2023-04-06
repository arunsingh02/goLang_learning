package router

import (
	"github.com/arunsingh02/mongoAPI/controller"
	"github.com/gorilla/mux"
)

func Router() *mux.Router {
	r := mux.NewRouter()
	r.HandleFunc("/", controller.ServeHome)
	r.HandleFunc("/api/movies", controller.GetAllMovies).Methods("GET")
	r.HandleFunc("/api/movie", controller.CreateOneMovie).Methods("POST")
	r.HandleFunc("/api/movie/{id}", controller.UpdateAsWatched).Methods("PUT")
	r.HandleFunc("/api/movie/{id}", controller.DeleteOneMovie).Methods("DELETE")
	r.HandleFunc("/api/deleteallmovie", controller.DeleteAllMovie).Methods("DELETE")
	return r

}
