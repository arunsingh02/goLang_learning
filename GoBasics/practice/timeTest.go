package practice

import (
	"fmt"
	"time"
)

func TimePlay() {
	// explicit type for Time
	var n time.Time = time.Now()
	fmt.Println("Current time is ", n)

	t := time.Date(2020, time.March, 31, 13, 45, 0, 0, time.UTC)
	fmt.Println(t)
	fmt.Println(t.Format(time.ANSIC))

	parsedTime, _ := time.Parse(time.ANSIC, "Tue Mar 31 13:45:00 2020")
	fmt.Printf("Parsed time type is %T\n", parsedTime)
}

/*
Current time is  2022-01-27 01:31:52.501606 +0530 IST m=+0.000069326
2020-03-31 13:45:00 +0000 UTC
Tue Mar 31 13:45:00 2020
Parsed time type is time.Time
*/
