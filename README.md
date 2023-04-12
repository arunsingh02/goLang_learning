# GoLang Learning

## Clone golang code from github :
[GoLang Github Link](https://github.com/arunsingh02/goLang_learning.git)

## Run Commad : 
```
go run <file-name>
go run --race <file-name> // to check the race condition (GoRoutines)
```

## OS dependent
### Create build file for mac
```
go build <file-name> // It will create exc file
```

### Create build file for windows
```
GOOS="windows" go build <file-name>
ex.  
 GOOS="windows" go build MyFirstGo.go
```
It will create MyFirstGo.exe buildfile

### Create build file for linux
```
GOOS="linux" go build <file-name>
ex.  
 GOOS="linux" go build MyFirstGo.go 
```
It will create MyFirstGo build file

## Get go evnironment 
```
go env
```

## mod init
```
The go mod init command creates a go.mod file to track your code's dependencies
Ex. 
   go mod init github.com/arunsingh02/<module-name>

https://go.dev/doc/tutorial/create-module#:~:text=Open%20a%20command%20prompt%20and%20cd%20to%20your%20home%20directory.&text=Create%20a%20greetings%20directory%20for%20your%20Go%20module%20source%20code.&text=Start%20your%20module%20using%20the,use%20example.com%2Fgreetings%20.
```

## mod init commands
```
go mod init [module-path] (The go mod init command initializes and writes a new go.mod file in the current directory, in effect creating a new module rooted at the current directory. The go.mod file must not already exist.)
go mod tidy (go mod tidy ensures that the go.mod file matches the source code in the module.)
Refrence: https://go.dev/ref/mod#go-mod-init

go mod init / Module Example:
    |- greetings
       |- greetings.go
       |- go.mod
    |- hello
       |- hello.go
       |- go.mod
(Inside the hello directory)
>> go run .
>> Hi, Gladys. Welcome!

Check some initial mod commands example : mymodule/main.go
```

## Mongo Atlas DB
```
https://cloud.mongodb.com/
Create Cluster
Add User and IP address
Dump dummy data and play around.
Please check goLang_learning/mongoAPI module to get more info about mongo BD usage.
```

## References
```
https://pkg.go.dev/
https://golangbyexample.com//
https://github.com/mongodb/mongo-go-driver (Mongo Go Driver referencne)
https://github.com/dlsniper/gopherconuk (Go micro-service / GCUK)
https://github.com/smartystreets/goconvey (Testing)
https://www.youtube.com/watch?v=bM6N-vgPlyQ&list=PLy-NDN51bIDVUNrl5KpfdHqkHfpFEFvWW&index=1
```
