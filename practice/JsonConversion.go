package main

import (
	"encoding/json"
	"fmt"
)

// Adding aliases in struct
type Course struct {
	Name      string `json:"coursename"` // Name will override with coursename after json formatting
	Price     int
	Plateform string   `json:"channel"`
	Password  string   `json:"-"`                // Password will not visible after json formatting
	Indexs    []string `json:"indexs,omitempty"` // omit in case of nil value (no extra space in between indexs , and omitempty)
}

func main() {
	fmt.Println("Welcome JSON conversion in go")

	youtubeCourses := []Course{
		{"Math", 0, "youtube", "abc123", nil},
		{"Pyshics", 0, "youtube", "def123", []string{"a", "b"}},
		{"Chemistry", 0, "youtube", "ghi123", []string{"1", "2"}},
	}

	// MarshalIndent(data, prefix, indent)
	// return type byte
	JsonData, _ := json.MarshalIndent(youtubeCourses, "", "\t")
	fmt.Printf("JSON data : %s\n", JsonData)

}

/*
Welcome JSON conversion in go
JSON data : [
        {
                "coursename": "Math",
                "Price": 0,
                "channel": "youtube"
        },
        {
                "coursename": "Pyshics",
                "Price": 0,
                "channel": "youtube",
                "indexs": [
                        "a",
                        "b"
                ]
        },
        {
                "coursename": "Chemistry",
                "Price": 0,
                "channel": "youtube",
                "indexs": [
                        "1",
                        "2"
                ]
        }
]
*/
