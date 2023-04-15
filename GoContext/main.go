// https://golangbyexample.com/using-context-in-golang-complete-guide/

package main

import (
	"fmt"

	"github.com/arunsingh02/GoContext/contexttype"
)

func main() {
	fmt.Println("Context in GoLang")
	// contexttype.ContextCaller()
	// contexttype.ContextWithCancle()
	// contexttype.ContextWithTimeout()
	contexttype.ContextWithDeadline()
}
