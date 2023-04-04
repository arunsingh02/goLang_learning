package main

import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gorilla/mux"
)

// Model in go - file
type Product struct {
	Name       string       `json:"name"`
	Company    string       `json:"brand"`
	Price      float32      `json:"price"`
	ProdID     string       `json:"productID"`
	Contractor *Constructor `json:"constructor"`
}

// Model - file
type Constructor struct {
	Name       string `json:"name`
	Speciality string `json:"speciality"`
	ContractID string `json:"ContractID"`
	Tenure     int    `json:"tenure,omitempty"`
}

// fake DB - file
var products []Product

// Helper or Middleware - file
func (p *Product) IsValid() bool {
	return p.Company == ""
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
	json.NewEncoder(w).Encode(products)
}

func GetOneProduct(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get one products")
	w.Header().Set("Content-type", "application/json")
	// collect the params from request
	params := mux.Vars(r)

	// Iterate slice and match with ID to get the product
	for _, prod := range products {
		if prod.ProdID == params["id"] {
			json.NewEncoder(w).Encode(prod)
			return
		}
	}
	json.NewEncoder(w).Encode("No Product found with given ID")
	return
}

// write add new product function
func AddNewProduct(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Add one products")
	w.Header().Set("Content-type", "application/json")
	// Check request Body
	// Should not be empty
	if r.Body == nil {
		json.NewEncoder(w).Encode("Please provide the body JSON")
		return
	}

	// Should not be {}
	var product Product
	_ = json.NewDecoder(r.Body).Decode(&product)
	if !product.IsValid() {
		json.NewEncoder(w).Encode("No data inside JSON")
		return
	}

	// Generate new prodID
	rand.Seed(time.Now().UnixNano())
	product.ProdID = strconv.Itoa(rand.Intn(100))
	products = append(products, product)
	json.NewEncoder(w).Encode(product)
	return

}

// Update the product details
func UpdateOneProduct(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get one products")
	w.Header().Set("Content-type", "application/json")
	params := mux.Vars(r)
	// Not required (already model will take care)
	// if params["id"] == "" {
	// 	json.NewEncoder(w).Encode("Update value is not present")
	// 	return
	// }
	for index, prod := range products {
		if prod.ProdID == params["id"] {
			products = append(products[:index], products[index+1:]...)
			var updateProd Product
			_ = json.NewDecoder(r.Body).Decode(&updateProd)
			updateProd.ProdID = params["id"]
			products = append(products, updateProd)
			json.NewEncoder(w).Encode(updateProd)
			return
		}
	}
	json.NewEncoder(w).Encode("Product not exists.")
	return
}

// Delete the asked product
func DeleteOneProduct(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get one products")
	w.Header().Set("Content-type", "application/json")
	params := mux.Vars(r)
	for index, prod := range products {
		if prod.ProdID == params["id"] {
			products = append(products[:index], products[index+1:]...)
			json.NewEncoder(w).Encode("Deleted the given product entry.")
			break
		}
	}
}

func main() {
	fmt.Println("Building API in Go")
	r := mux.NewRouter()
	// Seeding
	products = append(products, Product{
		"Parle G", "Parle", 5.0, "12", &Constructor{"Bpvt", "Food", "321", 4},
	})
	products = append(products, Product{
		"Gallant", "TMT", 1000, "32", &Constructor{"Spvt", "Building", "345", 1},
	})
	products = append(products, Product{
		"FaceWash", "Nivia", 345, "65", &Constructor{"Bpvt", "Beauty", "54", 12},
	})

	// model
	r.HandleFunc("/", serveHome).Methods("GET")
	r.HandleFunc("/products", GetAllProducts).Methods("GET")
	r.HandleFunc("/product/{id}", GetOneProduct).Methods("GET")
	r.HandleFunc("/updateprod/{id}", UpdateOneProduct).Methods("PUT")
	r.HandleFunc("/delprod/{id}", DeleteOneProduct).Methods("DELETE")
	r.HandleFunc("/addprod", AddNewProduct).Methods("POST")
	log.Fatal(http.ListenAndServe(":4000", r))
}

/*
ERROR:
func GetOneProduct(w http.ResponseWriter, r *http.Request) (index int, product Product) {}
╰─ go build .               ─╯
# github.com/arunsingh02/BuildAPI
./main.go:153:32: cannot use GetOneProduct (value of type func(w http.ResponseWriter, r *http.Request) (index int, product Product)) as func(http.ResponseWriter, *http.Request) value in argument to r.HandleFunc

Runnig Step :-
go build .
go run .
Use Postman or thunder client (vscode extension) to run the APIs
Ex: GET http://localhost:4000/products (I am using 4000 port)
*/
