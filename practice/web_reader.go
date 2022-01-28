// Read the online file

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func main() {
	// var link string = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
	link := "http://services.explorecalifornia.org/json/tours.php"
	resp, err := http.Get(link)
	CheckError(err)

	fmt.Printf("Type of content %T\n\n", resp)
	defer resp.Body.Close()

	byte, err := ioutil.ReadAll(resp.Body)
	CheckError(err)
	content := string(byte)
	// fmt.Print(content)

	tours := toursFromJson(content)
	for _, tour := range tours {
		fmt.Println(tour.Name, ":::", tour.Region)
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
	for decoder.More() {
		err := decoder.Decode(&tour)
		CheckError(err)
		tours = append(tours, tour)
	}
	return tours
}

type Tour struct {
	Name, Region string
}

/*
Type of content *http.Response

2 Days Adrift the Salton Sea ::: Southern California
A Week of Wine ::: Napa/Sonoma Counties
Amgen Tour of California Special ::: Northern California
Avila Beach Hot springs ::: Central Coast
Big Sur Retreat ::: Central Coast
Channel Islands Excursion ::: Southern California
Coastal Experience ::: Central Coast
Cycle California: My Way ::: Varies
Day Spa Package ::: Southern California
Endangered Species Expedition ::: Central Coast
Fossil Tour ::: Varies
Hot Salsa Tour ::: Southern California
Huntington Library and Pasadena Retreat Tour ::: Southern California
In the Steps of John Muir ::: Northern California
Joshua Tree: Best of the West Tour ::: Southern California
Kids L.A. Tour ::: Southern California
Mammoth Mountain Adventure ::: Southern California
Matilija Hot springs ::: Central Coast
Mojave to Malibu ::: Southern California
Monterey to Santa Barbara Tour ::: Varies
Mountain High Lift-off ::: Southern California
Olive Garden Tour ::: Southern California
Oranges & Apples Tour ::: Southern California
Restoration Package ::: Varies
The Death Valley Survivor's Trek ::: Inland Empire
The Mt. Whitney Climbers Tour ::: Northern California
*/
