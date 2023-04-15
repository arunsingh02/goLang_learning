package contexttype

import (
	"context"
	"fmt"
	"log"
	"time"
)

func ContextWithTimeout() {
	ctx := context.Background()                                  // Empty Context, no deadline and never cancelled
	cancelCtx, cancel := context.WithTimeout(ctx, time.Second*4) // ctx is the parent context
	go printer(cancelCtx)
	defer cancel()
	time.Sleep(time.Second * 6)
}

func printer(ctx context.Context) {
	i := 1
	for {
		select {
		//It retures a channel when a context is cancelled, timesout (either when deadline is reached or timeout time has finished)
		case <-ctx.Done():
			fmt.Println("Exited gracefully WithTimeout")
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
Exited gracefully WithTimeout
2023/04/15 12:36:05 context deadline exceeded
exit status 1
*/
