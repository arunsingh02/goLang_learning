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

func EncodeJson() {
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

func DecodedJson() {
	JsonWebData := []byte(`
	{
		"coursename": "Pyshics",
        "Price": 0,
        "channel": "youtube",
        "indexs": ["a", "b"]
	}
	`)

	var youtubeCourse Course
	checkValid := json.Valid(JsonWebData)
	if checkValid {
		fmt.Println("JSON was valid")
		json.Unmarshal(JsonWebData, &youtubeCourse)
		// %#v
		fmt.Printf("%#v\n", youtubeCourse)
	} else {
		fmt.Println("JSON WAS NOT VALID")
	}

	// key value (key is string and value will be any type)
	var onlineData map[string]interface{}

	json.Unmarshal(JsonWebData, &onlineData)

	for k, v := range onlineData {
		fmt.Printf("Key is %s and value is %s and type is %T\n", k, v, v)
	}

}

func main() {
	fmt.Println("Welcome JSON conversion in go")
	EncodeJson()
	fmt.Println("\n==================================\n")
	DecodedJson()
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


==================================

JSON was valid
main.Course{Name:"Pyshics", Price:0, Plateform:"youtube", Password:"", Indexs:[]string{"a", "b"}}
Key is coursename and value is Pyshics and type is string
Key is Price and value is %!s(float64=0) and type is float64
Key is channel and value is youtube and type is string
Key is indexs and value is [a b] and type is []interface {}
*/
