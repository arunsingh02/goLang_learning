// Read the online file

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
)

const link string = "http://services.explorecalifornia.org/json/tours.php"

func main() {
	// var link string = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
	resp, err := http.Get(link)
	CheckError(err)

	fmt.Printf("Type of content %T\n", resp)
	fmt.Println("Status : ", resp.Status)
	fmt.Println("Status Code : ", resp.StatusCode)
	defer resp.Body.Close() // Caller's responsibility to close the connection

	// ioutil.ReadAll is deprecated from Go 1.16 (calls internally io.ReadAll)
	byte, err := io.ReadAll(resp.Body)
	CheckError(err)
	content := string(byte)
	// fmt.Print(content)

	tours := toursFromJson(content)
	// fmt.Println("Tours : ", tours)
	for _, tour := range tours {
		fmt.Println(tour.Name, ":::", tour.Region, "::::", tour.TourId)
	}
}

func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

func toursFromJson(content string) []Tour {
	tours := make([]Tour, 0, 20)

	decoder := json.NewDecoder(strings.NewReader(content))
	_, err := decoder.Token()
	CheckError(err)

	var tour Tour
	// More reports whether there is another
	// element in the current array or object being parsed.
	for decoder.More() {
		err := decoder.Decode(&tour)
		CheckError(err)
		tours = append(tours, tour)
	}
	return tours
}

type Tour struct {
	// tourId (small t) will not include toureID
	Name, Region, TourId string
}

/*
Type of content *http.Response
Status :  200 OK
Status Code :  200

2 Days Adrift the Salton Sea ::: Southern California :::: 14
A Week of Wine ::: Napa/Sonoma Counties :::: 26
Amgen Tour of California Special ::: Northern California :::: 11
Avila Beach Hot springs ::: Central Coast :::: 9
Big Sur Retreat ::: Central Coast :::: 1
Channel Islands Excursion ::: Southern California :::: 5
Coastal Experience ::: Central Coast :::: 20
Cycle California: My Way ::: Varies :::: 13
Day Spa Package ::: Southern California :::: 6
Endangered Species Expedition ::: Central Coast :::: 18
Fossil Tour ::: Varies :::: 19
Hot Salsa Tour ::: Southern California :::: 25
Huntington Library and Pasadena Retreat Tour ::: Southern California :::: 8
In the Steps of John Muir ::: Northern California :::: 2
Joshua Tree: Best of the West Tour ::: Southern California :::: 16
Kids L.A. Tour ::: Southern California :::: 17
Mammoth Mountain Adventure ::: Southern California :::: 21
Matilija Hot springs ::: Central Coast :::: 10
Mojave to Malibu ::: Southern California :::: 15
Monterey to Santa Barbara Tour ::: Varies :::: 12
Mountain High Lift-off ::: Southern California :::: 22
Olive Garden Tour ::: Southern California :::: 23
Oranges & Apples Tour ::: Southern California :::: 24
Restoration Package ::: Varies :::: 7
The Death Valley Survivor's Trek ::: Inland Empire :::: 3
The Mt. Whitney Climbers Tour ::: Northern California :::: 4
*/
