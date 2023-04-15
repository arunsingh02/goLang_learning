package contexttype

import (
	"context"
	"log"
	"net/http"
)

func ContextCaller() {
	helloWorldHandler := http.HandlerFunc(HelloWorld)
	http.Handle("/welcome", injectMsgID(helloWorldHandler))
	log.Fatal(http.ListenAndServe(":4000", nil))
}

func HelloWorld(w http.ResponseWriter, r *http.Request) {
	var msgID string = ""
	if m := r.Context().Value("msgId"); m != nil {
		if value, ok := m.(string); ok {
			msgID = value
		}
	}
	w.Header().Add("msgId", msgID)
	w.Write([]byte("Hello, world"))
}

func injectMsgID(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		msgID := "123123412341341234"
		ctx := context.WithValue(r.Context(), "msgId", msgID)
		req := r.WithContext(ctx)
		next.ServeHTTP(w, req)
	})
}

/*
curl -v http://localhost:4000/welcome
*   Trying 127.0.0.1:4000...
* Connected to localhost (127.0.0.1) port 4000 (#0)
> GET /welcome HTTP/1.1
> Host: localhost:4000
> User-Agent: curl/7.86.0
> Accept:
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Msgid: 123123412341341234                  // Your MsgID
< Date: Fri, 14 Apr 2023 12:36:09 GMT
< Content-Length: 12
< Content-Type: text/plain; charset=utf-8
<
* Connection #0 to host localhost left intact
Hello, world%
*/
