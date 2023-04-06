package collection

import (
	"context"
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const connectionString = "mongodb+srv://arunsingh02:doNotDisturb@cluster0.tkqh4up.mongodb.net/?retryWrites=true&w=majority"
const dbName = "disney"
const colName = "watchlist"

// Special function, called before main
// we can add more than one init in sigle file, called in order they added
// we can add in diff files, called in lexicographic filename order (Alphabetical Order)
func init() {
	//client option
	clientOption := options.Client().ApplyURI(connectionString)

	// Connect to mongo
	client, err := mongo.Connect(context.TODO(), clientOption)
	CheckError(err)
	fmt.Println("Mongo DB connects successfully")

	collection := client.Database(dbName).Collection(colName)

	// collection instance
	fmt.Println("Collection instance is ready")
}

// Check error
func CheckError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
