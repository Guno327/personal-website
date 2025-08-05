build: website static/script/typewriter.js

run: website static/script/typewriter.js
	./website

static/script/typewriter.js: static/script/typewriter.ts
	tsc --lib dom,es2015 static/script/typewriter.ts

website: website.go
	go build website.go

clean:
	rm -f website
	rm -f static/script/typewriter.js
