# Personal Website

That is where you are right now!

## Description

This project is the personal website that you are visiting right now. It serves
as a place for me to coalesce my portfolio as well as talk about things that I
find interesting or am working on currently.

## Stack

- Backend: Go
- Frontend: CSS and TypeScript

## Detailed Write-Up

I originally had my personal website hosted a static page on GitHub pages using
Jekyll as the static site generator. I was not happy with it overall and wanted
an excuse to learn Go and thought rewriting would server as a good opportunity.

The backend is pretty simple and follows a general approach of pages and
indexes. A page is anything that is, for the most part, text or other content
elements and an index is a list of pages. This is an example of a page and if
you came here from the projects tab, that would be an index. For the pages I
have a single request handler that just takes the URL argument, ensures it is
valid, loads a markdown file stored in the `data` path, converts it to HTML and
sends that page wrapped in a template for some nice styling.

The glitch and scan-line effects were made using CSS keyframes and the
typewriter effect you see when a page loads is a simple TypeScript script.

The service is hosted on Google App Cloud for CI and connected into my personal
domain managed on Cloudflare.

## Links

[Code on GitHub](https://github.com/Guno327/personal-website)
