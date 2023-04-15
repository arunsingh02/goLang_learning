package contexttype

import (
	"context"
	"fmt"
	"log"
	"time"
)

func ContextWithCancle() {
	ctx := context.Background()                     // Empty Context, no deadline and never cancelled
	cancelCtx, canclFunc := context.WithCancel(ctx) // ctx is the parent context
	go task(cancelCtx)
	time.Sleep(time.Second * 3)
	canclFunc()
	time.Sleep(time.Second * 1)
}

func task(ctx context.Context) {
	i := 1
	for {
		select {
		//It retures a channel when a context is cancelled, timesout (either when deadline is reached or timeout time has finished)
		case <-ctx.Done():
			fmt.Println("Exited gracefully WithCancel")
			log.Fatal(ctx.Err())
		default:
			fmt.Println(i)
			i++
			time.Sleep(time.Second * 1)
		}
	}
}

/*
Context in GoLang
1
2
3
Exited gracefully WithCancel
2023/04/15 12:35:20 context canceled
exit status 1
*/
