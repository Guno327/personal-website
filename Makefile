build: static/script/typewriter.js
	sudo docker build --tag personal-website:latest --file Dockerfile .

run: build
	sudo docker run -p 8080:8080 personal-website

static/script/typewriter.js: static/script/typewriter.ts
	tsc --lib dom,es2015 static/script/typewriter.ts
	

clean:
	rm -f static/script/typewriter.js
	rm -f website


