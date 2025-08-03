package main

import (
	"github.com/gomarkdown/markdown"
	"github.com/gomarkdown/markdown/html"
	"github.com/gomarkdown/markdown/parser"

	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
	"regexp"
	"strings"
)

var templates = template.Must(template.ParseFiles("templates/base.html", "templates/typed.html"))

var validPage = regexp.MustCompile("^/(class|project)/([a-zA-Z0-9]+)/$")
var validStaticPage = regexp.MustCompile("^/(about|contact)/$")
var titleFromPath = regexp.MustCompile("^([a-zA-Z0-9]+).([a-zA-Z]+)$")

type Page struct {
	Title string
	Body  template.HTML
}

func mdToHTML(md []byte) []byte {
	// create markdown parser with extensions
	extensions := parser.CommonExtensions | parser.AutoHeadingIDs | parser.NoEmptyLineBeforeBlock
	p := parser.NewWithExtensions(extensions)
	doc := p.Parse(md)

	// create HTML renderer with extensions
	htmlFlags := html.CommonFlags | html.HrefTargetBlank
	opts := html.RendererOptions{Flags: htmlFlags}
	renderer := html.NewRenderer(opts)

	return markdown.Render(doc, renderer)
}

func loadPage(title string) *Page {
	filename := "data/" + title + ".md"
	log.Printf("LOADING: %s\n", filename)
	body, err := os.ReadFile(filename)
	if err != nil {
		log.Printf("Could not load %s (%s)\n", filename, err.Error())
		return nil
	}
	return &Page{Title: strings.ToUpper(strings.ReplaceAll(title, "_", " ")), Body: template.HTML(mdToHTML(body))}
}

func pageHandler(w http.ResponseWriter, r *http.Request) {
	m := validStaticPage.FindStringSubmatch(r.URL.Path)
	if m == nil {
		m = validPage.FindStringSubmatch(r.URL.Path)
		if m == nil {
			log.Printf("404: No substring match for page (%s)\n", r.URL.Path)
			http.NotFound(w, r)
			return
		}
	}

	log.Printf("FETCHING: %s", m[1])
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
		http.NotFound(w, r)
		return
	}

	if p == nil {
		log.Print("404: Page not found")
		http.NotFound(w, r)
		return
	}

	err := templates.ExecuteTemplate(w, "typed.html", p)
	if err != nil {
		log.Printf("404: Error executing template in page (%s)\n", err.Error())
		http.NotFound(w, r)
	}
}

func classesHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/classes/" {
		log.Printf("404: Path not found (%s)", r.URL.Path)
		http.NotFound(w, r)
		return
	}

	log.Print("FETCHING: /classes/")
	classes, err := os.ReadDir("data/classes")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	body := "<ul>\n"
	for _, class := range classes {
		m := titleFromPath.FindStringSubmatch(class.Name())
		title := m[1]
		body += fmt.Sprintf("<li><a href=\"/class/%s/\">%s</a></li>\n", title, strings.ToUpper(title))
	}
	body += "</ul>\n"
	p := &Page{Title: "CLASSES", Body: template.HTML(body)}

	err = templates.ExecuteTemplate(w, "base.html", p)
	if err != nil {
		http.NotFound(w, r)
	}
}

func projectsHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/projects/" {
		log.Printf("404: Path not found (%s)", r.URL.Path)
		http.NotFound(w, r)
		return
	}

	log.Print("FETCHING: /projects/")
	projects, err := os.ReadDir("data/projects")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	body := "<ul>\n"
	for _, project := range projects {
		m := titleFromPath.FindStringSubmatch(project.Name())
		title := m[1]
		body += fmt.Sprintf("<li><a href=\"/project/%s/\">%s</a></li>\n", title, strings.ToUpper(strings.ReplaceAll(title, "_", " ")))
	}
	body += "</ul>\n"
	p := &Page{Title: "PROJECTS", Body: template.HTML(body)}

	err = templates.ExecuteTemplate(w, "base.html", p)
	if err != nil {
		http.NotFound(w, r)
	}
}

func rootHandler(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/about/", http.StatusFound)
}

func main() {
	http.HandleFunc("/classes/", classesHandler)
	http.HandleFunc("/projects/", projectsHandler)
	http.HandleFunc("/class/", pageHandler)
	http.HandleFunc("/project/", pageHandler)
	http.HandleFunc("/about/", pageHandler)
	http.HandleFunc("/contact/", pageHandler)
	http.HandleFunc("/", rootHandler)

	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

	log.Fatal(http.ListenAndServe(":8080", nil))
}
