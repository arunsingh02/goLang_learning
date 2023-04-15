package contexttype

import (
	"context"
	"fmt"
	"log"
	"time"
)

func ContextWithDeadline() {
	ctx := context.Background()                                                   // Empty Context, no deadline and never cancelled
	cancelCtx, cancel := context.WithDeadline(ctx, time.Now().Add(time.Second*5)) // ctx is the parent context
	defer cancel()
	go data_counter(cancelCtx)
	time.Sleep(time.Second * 7)
}

func data_counter(ctx context.Context) {
	i := 1
	for {
		select {
		//It retures a channel when a context is cancelled, timesout (either when deadline is reached or timeout time has finished)
		case <-ctx.Done():
			fmt.Println("Exited gracefully WithDeadline")
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
4
5
Exited gracefully WithDeadline
2023/04/15 12:44:57 context deadline exceeded
exit status 1
*/
