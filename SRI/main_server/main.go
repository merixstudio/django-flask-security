package main

import (
	"html/template"
	"log"
	"net/http"
)

// Data is page data structure.
type Data struct {
	Name string
}

func rootHandler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Path[1:]
	if name == "" {
		name = "Anonymous"
	}
	data := &Data{Name: name}
	t, _ := template.ParseFiles("index.html")
	t.Execute(w, data)
}

func errorHandler(w http.ResponseWriter, r *http.Request, status int) {
	w.WriteHeader(status)
	w.Write([]byte("Page not found."))
}

func main() {
	http.HandleFunc("/", rootHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
