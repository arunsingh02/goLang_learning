package main

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

// Model in go - file
type Product struct {
	Name       string      `json:"name"`
	Company    string      `json:"brand"`
	Price      float32     `json:"price"`
	ProdID     string      `json:"productID"`
	Contractor *Contractor `json:"contractor"`
}

// Model - file
type Constructor struct {
	Name       string `json:"name`
	Speciality string `json:"speciality"`
	ContractID string `json:"ContractID"`
	Tenure     int    `json:"tenure,omitempty"`
}

// fake DB - file
var product []Product

// Helper or Middleware - file
func (p *Product) IsValid() bool {
	return p.ProdID != "" || p.Company != ""
}

// Helper - file
func (c *Constructor) IsContractValid() bool {
	return c.ContractID != "" && c.Tenure != 0
}

// Controllers
func serveHome(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Welcome in Build API Project</h1>"))
}

// Controllers
func GetAllProducts(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get all the products")
	w.Header().Set("Content-type", "application/json")
	json.NewEncoder(w).Encode(product)
}

func GetOneProduct(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get one products")
	w.Header().Set("Content-type", "application/json")
	// collect the params from request
	params := mux.Vars(r)

	// Iterate slice and match with ID to get the product
	for _, prod := range product {
		if prod.ProdID == params["id"] {
			json.NewEncoder(w).Encode(prod)
			return
		}
	}
	json.NewEncoder(w).Encode("No Product found with given ID")
	return
}

// write add new product function

func main() {
	fmt.Println("Building API in Go")
}
