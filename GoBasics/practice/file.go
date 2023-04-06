// File read and write

package practice

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func FilePlay() {
	content := "My name is Arun Singh!"
	var fileName string = "./namefile.txt"
	// file create
	file, err := os.Create(fileName)
	CheckNilError(err)

	length, err := io.WriteString(file, content)
	CheckNilError(err)
	fmt.Println("Total length of file is : ", length)
	defer file.Close() // Using defer is recommended (Not neccessary)
	writeFile(fileName, file)
	defer file.Close()
	defer readFile(fileName)
}

func readFile(fileName string) {
	// open ./ss.txt: no such file or directory
	// panic: File error
	// data, err := ioutil.ReadFile("./ss.txt")
	data, err := ioutil.ReadFile(fileName)
	CheckNilError(err)
	// converting string is imp, else will get data bytes
	fmt.Println("File content is :\n", string(data))
}

func writeFile(fileName string, file *os.File) {
	new_content := "\nI am software engineer."
	_, err := io.WriteString(file, new_content)
	CheckNilError(err)
}

func CheckNilError(err error) {
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
