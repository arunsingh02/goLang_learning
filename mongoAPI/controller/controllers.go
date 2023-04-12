// Need to update the password of Mongo Atlas to access DB

package controller

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/arunsingh02/mongoAPI/model"
	"github.com/gorilla/mux"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const connectionString = "mongodb+srv://arunsingh02:<password>@cluster0.tkqh4up.mongodb.net/?retryWrites=true&w=majority"
const dbName = "disney"
const colName = "watchlist"

// MOST IMPORTANT
var collection *mongo.Collection

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

	collection = client.Database(dbName).Collection(colName)

	// collection instance
	fmt.Println("Collection instance is ready")
}

// Check error
func CheckError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

// MongoDB Helper
func collectAllMovies() []primitive.M {
	cur, err := collection.Find(context.Background(), bson.D{})
	CheckError(err)

	var movies []primitive.M

	defer cur.Close(context.Background())

	for cur.Next(context.Background()) {
		var movie bson.M
		err := cur.Decode(&movie)
		CheckError(err)
		movies = append(movies, movie)
	}
	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}
	return movies
}

func collectOneMovie(movieID string) primitive.M {
	var movie bson.M
	id, _ := primitive.ObjectIDFromHex(movieID)
	err := collection.FindOne(context.Background(), bson.M{"_id": id}).Decode(&movie)
	if err != nil {
		fmt.Println(err)
	}
	/*
		Getting error
		if err == mongo.ErrNoDocuments {
			fmt.Println("record does not exist")
		}
	*/
	return movie
}

func insertOneMovie(movie model.Disney) {
	insertResult, err := collection.InsertOne(context.Background(), movie)
	CheckError(err)
	fmt.Println("Inserted ID: ", insertResult.InsertedID)
}

func updateOneMovie(movieID string) {
	id, _ := primitive.ObjectIDFromHex(movieID)
	filter := bson.M{"_id": id}
	update := bson.M{"$set": bson.M{"watched": true}}

	updated, err := collection.UpdateOne(context.Background(), filter, update)
	CheckError(err)
	fmt.Println("Updated count : ", updated.ModifiedCount)
}

func deleteOneMovie(movieID string) {
	id, _ := primitive.ObjectIDFromHex(movieID)
	filter := bson.M{"_id": id}
	result, err := collection.DeleteOne(context.Background(), filter)
	CheckError(err)
	fmt.Println("Deleted count : ", result.DeletedCount)
}

func deleteAllMovie() int64 {
	result, err := collection.DeleteMany(context.Background(), bson.M{})
	CheckError(err)
	fmt.Println("Deleted count : ", result.DeletedCount)
	return result.DeletedCount
}

// collections

func ServeHome(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Welcome in Build API Project"))
}

func GetAllMovies(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	json.NewEncoder(w).Encode("These are all movies list")
	movies := collectAllMovies()
	json.NewEncoder(w).Encode(movies)
}

func GetOneMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	json.NewEncoder(w).Encode("This is the asked movie list")
	params := mux.Vars(r)
	movie := collectOneMovie(params["id"])
	json.NewEncoder(w).Encode(movie)
}

func CreateOneMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	w.Header().Set("Allow-Control-Allow-Methods", "POST")

	var movie model.Disney
	err := json.NewDecoder(r.Body).Decode(&movie)
	CheckError(err)
	insertOneMovie(movie)
	json.NewEncoder(w).Encode("Movie Inserted successfully")
	json.NewEncoder(w).Encode(movie)
}

func UpdateAsWatched(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	w.Header().Set("Allow-Control-Allow-Methods", "PUT")

	params := mux.Vars(r)
	updateOneMovie(params["id"])
	json.NewEncoder(w).Encode("Asked movie is added in watchlist")
}

func DeleteOneMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	w.Header().Set("Allow-Control-Allow-Methods", "DELETE")

	params := mux.Vars(r)
	deleteOneMovie(params["id"])
	json.NewEncoder(w).Encode("Asked movie is deleted")
}

func DeleteAllMovie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/x-www-form-urlencode")
	w.Header().Set("Allow-Control-Allow-Methods", "DELETE")

	count := deleteAllMovie()
	json.NewEncoder(w).Encode(count)
}
