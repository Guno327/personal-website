package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
	"regexp"
	"strings"
)

var templates = template.Must(template.ParseFiles(
	"templates/base.html",
	"templates/markdown.html",
))

var validPage = regexp.MustCompile("^/(class|project)/([a-zA-Z0-9_/]+)/$")
var validStaticPage = regexp.MustCompile("^/(about|contact)/$")
var titleFromPath = regexp.MustCompile("^([a-zA-Z0-9_]+).([a-zA-Z]+)$")
var validIndex = regexp.MustCompile("^/(projects|classes)((/)|([a-zA-Z0-9_/]*))/$")

type Page struct {
	Title string
	Body  template.HTML
}

type Index struct {
}

func loadPage(title string) *Page {
	filename := "data/" + title + ".md"
	log.Printf("LOADING: %s\n", filename)
	body, err := os.ReadFile(filename)
	if err != nil {
		log.Printf("Could not load %s (%s)\n", filename, err.Error())
		return nil
	}
	return &Page{Title: strings.ToUpper(strings.ReplaceAll(title, "_", " ")), Body: template.HTML(body)}
}

func pageHandler(w http.ResponseWriter, r *http.Request) {
	m := validStaticPage.FindStringSubmatch(r.URL.Path)
	if m == nil {
		m = validPage.FindStringSubmatch(r.URL.Path)
		if m == nil {
			log.Printf("404: No substring match for page (%s)\n", r.URL.Path)
			http.ServeFile(w, r, "static/pages/404.html")
			return
		}
	}

	log.Printf("FETCHING: %s", r.URL.Path)
	var p *Page
	switch m[1] {
	case "class":
		p = loadPage("classes/" + m[2])
	case "project":
		p = loadPage("projects/" + m[2])
	case "contact":
		p = loadPage("contact")
	case "about":
		p = loadPage("about")
	default:
		log.Printf("404: substring match unexpected in page (%s)\n", m[1])
		http.ServeFile(w, r, "static/pages/404.html")
		return
	}

	if p == nil {
		log.Print("404: Page not found")
		http.ServeFile(w, r, "static/pages/404.html")
		return
	}

	err := templates.ExecuteTemplate(w, "markdown.html", p)
	if err != nil {
		log.Printf("404: Error executing template in page (%s)\n", err.Error())
		http.ServeFile(w, r, "static/pages/404.html")
	}
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	m := validIndex.FindStringSubmatch(r.URL.Path)

	path := "data/" + m[1] + m[2]

	log.Printf("FETCHING: %s\n", path)
	entries, err := os.ReadDir(path)
	if err != nil {
		log.Printf("404: Could not read dir (%s)", path)
		http.ServeFile(w, r, "static/pages/404.html")
	}

	if len(entries) == 0 {
		err = templates.ExecuteTemplate(w, "base.html", &Page{Title: strings.ToUpper(path), Body: template.HTML("<p>Empty...<p>")})
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
	}

	body := "<ul>\n"
	for _, entry := range entries {
		log.Printf("BUILDING: entry for %s", entry.Name())

		isClass := m[1] == "classes"
		isProject := m[1] == "projects"

		if entry.IsDir() {
			body += fmt.Sprintf("<li><a href=\"%s%s/\">%s</a></li>\n", r.URL.Path, entry.Name(), strings.ToUpper(strings.ReplaceAll(entry.Name(), "_", " ")))
		} else {
			title := titleFromPath.FindStringSubmatch(entry.Name())

			if isClass {
				body += fmt.Sprintf("<li><a href=\"/class%s/%s/\">%s</a></li>\n", m[2], title[1], strings.ToUpper(strings.ReplaceAll(title[1], "_", " ")))
			} else if isProject {
				body += fmt.Sprintf("<li><a href=\"/project%s/%s/\">%s</a></li>\n", m[2], title[1], strings.ToUpper(strings.ReplaceAll(title[1], "_", " ")))
			} else {
				log.Printf("404: Not project or class (%s)", r.URL.Path)
				http.ServeFile(w, r, "static/pages/404.html")
				return
			}
		}
	}
	body += "</ul>\n"
	p := &Page{Title: "PROJECTS", Body: template.HTML(body)}

	err = templates.ExecuteTemplate(w, "base.html", p)
	if err != nil {
		http.ServeFile(w, r, "static/pages/404.html")
	}

}

func rootHandler(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/about/", http.StatusFound)
}

func main() {
	http.HandleFunc("/classes/", indexHandler)
	http.HandleFunc("/projects/", indexHandler)
	http.HandleFunc("/class/", pageHandler)
	http.HandleFunc("/project/", pageHandler)
	http.HandleFunc("/about/", pageHandler)
	http.HandleFunc("/contact/", pageHandler)
	http.HandleFunc("/", rootHandler)

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

	log.Fatal(http.ListenAndServe(":8080", nil))
}
