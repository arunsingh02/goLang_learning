package greetings

import (
	"regexp"
	"testing"
)

// Testing with name
func TestHelloWithName(t *testing.T) {
	name := "Arun"
	want := regexp.MustCompile(`\b` + name + `\b`)
	msg := Hello("Arun")
	if !want.MatchString(msg) {
		t.Fatalf(`Hello("Gladys") = %q, want match for %#q, nil`, msg, want)
	}
}

// Testing with empty name
func TestHelloWithEmptyName(t *testing.T) {
	msg := Hello("")
	if msg != "Hi, . Welcome!" {
		t.Fatalf(`Hello("") = %q, want "", error`, msg)
	}
}
