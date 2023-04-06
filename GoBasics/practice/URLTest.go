package practice

import (
	"fmt"
	"net/url"
)

const Url string = "https://netapp.com:3000/profile?name=Arun&level=MTS3"

func URLPlay() {
	fmt.Println("Handlling URLs in golang")

	//parsing
	url_obj, _ := url.Parse(Url)
	fmt.Printf("URL type %T\n", url_obj)

	fmt.Println(url_obj.Scheme) // protocol
	fmt.Println(url_obj.Host)
	fmt.Println(url_obj.Port())
	fmt.Println(url_obj.Path)
	fmt.Println(url_obj.RawQuery)

	params := url_obj.Query()

	for key, val := range params {
		fmt.Println(key, " : ", val[0])
	}

	// prepare the URL
	// Don't forgot & before url
	prepUrl := &url.URL{
		Scheme:   "NFS",
		Host:     "netapp.com",
		Path:     "/data",
		RawQuery: "project=ABC",
	}

	// Values maps a string key to a list of values.
	// It is typically used for query parameters and form values
	partsOfUrls := url.Values{}
	partsOfUrls.Add("firstname", "Arun")
	partsOfUrls.Add("lastname", "Singh")
	partsOfUrls.Add("age", "13")
	partsOfUrls.Add("address", "Bengaluru")
	fmt.Println("Parts of Urls : ", partsOfUrls)

	partsOfUrls.Del("age")
	fmt.Println("Parts of Urls : ", partsOfUrls)

	NewUrl := prepUrl.String()
	fmt.Println("New URL: ", NewUrl)

}

/*
Handlling URLs in golang
URL type *url.URL
https
netapp.com:3000
3000
/profile
name=Arun&level=MTS3
name  :  Arun
level  :  MTS3
New URL:  NFS://netapp.com/data?project=ABC
*/
