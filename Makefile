
all: publish

clean:
	rm blog/html -r
	rm blog/doctrees -r

publish: blog/html/index.html
	rsync -avz blog/html/ redtoad.de:/var/www/redtoad.de/blog 

blog/html/index.html:
	tinker --build

