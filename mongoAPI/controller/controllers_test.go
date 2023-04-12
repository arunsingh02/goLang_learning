package controller

import (
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

// Test the total entry in DB
func TestCollectAllMovies(t *testing.T) {
	Convey("Getting the all movies from Disney plateform", t, func() {
		Convey("with the valid function", func() {
			totalMovies := 4
			movies := collectAllMovies()
			So(len(movies), ShouldEqual, totalMovies)
		})
	})
}

// Test the single entry with correct _id from DB
func TestCollectOneMoviesWithCorrectID(t *testing.T) {
	Convey("Getting the all movies from Disney plateform", t, func() {
		Convey("with the valid function", func() {
			id := "643012d7855cdbb378bb8f87"
			movie := collectOneMovie(id)
			So(movie["movie"], ShouldEqual, "Bahubali")
			So(movie["watched"], ShouldBeFalse)
		})
	})
}

// Test the single entry with correct _id from DB
func TestCollectOneMoviesWithWrongID(t *testing.T) {
	Convey("Getting the all movies from Disney plateform", t, func() {
		Convey("with the valid function", func() {
			id := "643012d7855cdbb378bb8hty"
			movie := collectOneMovie(id) //map[]
			So(movie, ShouldBeEmpty)
		})
	})
}
