package main

import "fmt"

/*
Interface
Interface is a type in Go which is a collection of method signatures.
These collections of method signatures are meant to represent certain behaviour.
The interface declares only the method set and any type which implements all methods of the interface is of that interface type.
*/

type taxCalculator interface {
	CalculateTax() int
}

type IndiaTax struct {
	TaxPercentage int
	Income        int
}

type USATax struct {
	TaxPercentage int
	Income        int
}

type UKTax struct {
	TaxPercentage int
	Income        int
}

func (i *IndiaTax) CalculateTax() int {
	tax := (i.TaxPercentage * i.Income) / 100
	return tax
}

func (u *USATax) CalculateTax() int {
	tax := (u.TaxPercentage * u.Income) / 100
	return tax
}

func (uk *UKTax) CalculateTax() int {
	tax := (uk.TaxPercentage * uk.Income) / 100
	return tax
}

// Embedding interface in other interface
type payee1 struct {
	// If the embedded interface is unnamed/anonymous field then interface methods can be referred directly or via the interface name
	taxCalculator
	name string
}

type payee2 struct {
	// If the embedded interface is a named field, then interface methods has to be called via the named interface name
	t    taxCalculator
	name string
}

type payee3 struct {
	t    taxCalculator
	name string
}

func main() {
	fmt.Println("Interface in GoLang")
	var india = &IndiaTax{
		TaxPercentage: 10,
		Income:        10000,
	}
	var usa = &USATax{
		TaxPercentage: 20,
		Income:        30000,
	}
	var uk = &UKTax{
		TaxPercentage: 25,
		Income:        100000,
	}

	// Embadded
	p1 := payee1{
		name:          "Arun",
		taxCalculator: india,
	}

	p2 := payee2{
		name: "Ravi",
		t:    usa,
	}

	p3 := payee3{
		name: "Ragini",
		t:    uk,
	}

	// 1st
	taxSystems1 := []taxCalculator{
		india,
		usa,
		uk,
	}
	calculateTotalTax(taxSystems1)

	// 2nd
	taxSystems2 := []taxCalculator{
		p1,
		p2.t,
		p3.t,
	}
	calculateTotalTax(taxSystems2)

}

func calculateTotalTax(taxContries []taxCalculator) {
	var totalTax int
	for _, country := range taxContries {
		// Type Switch (type assertion in series)
		switch v := country.(type) {
		case payee1:
			fmt.Println("Type: Payee1")
		case taxCalculator:
			fmt.Println("Type: taxCalculator interface")
			// fmt.Println(country.(taxCalculator))
		default:
			fmt.Println(v)
		}
		totalTax += country.CalculateTax() // run time polymorphism happens
	}
	fmt.Println("Total Tax should pay: ", totalTax)
}

/*
Interface in GoLang
Type: taxCalculator interface
Type: taxCalculator interface
Type: taxCalculator interface
Total Tax should pay:  32000
Type: Payee1
Type: taxCalculator interface
Type: taxCalculator interface
Total Tax should pay:  32000
*/
