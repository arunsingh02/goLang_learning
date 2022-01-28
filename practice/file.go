// File read and write

package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func main() {
	content := "My name is Arun Singh!"
	var fileName string = "./namefile.txt"
	// file create
	file, err := os.Create(fileName)
	CheckError(err)

	length, err := io.WriteString(file, content)
	CheckError(err)
	fmt.Println("Total length of file is : ", length)
	defer file.Close()
	writeFile(fileName, file)
	defer file.Close()
	defer readFile(fileName)
}

func readFile(fileName string) {
	// open ./ss.txt: no such file or directory
	// panic: File error
	// data, err := ioutil.ReadFile("./ss.txt")
	data, err := ioutil.ReadFile(fileName)
	CheckError(err)
	fmt.Println("File content is :\n", string(data))
}

func writeFile(fileName string, file *os.File) {
	new_content := "\nI am software engineer."
	_, err := io.WriteString(file, new_content)
	CheckError(err)
}

func CheckError(err error) {
	if err != nil {
		fmt.Println(err)
		panic("File error")
	}
}

/*
Total length of file is :  22
File content is :
 My name is Arun Singh!
I am software engineer.
*/
