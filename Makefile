
all: clean publish

clean:
	rm blog/html -r
	rm blog/doctrees -r

publish: blog/html/index.html
	rsync -avz blog/html/ redtoad.de:/var/www/redtoad.de/blog 
	scp blog/html/sitemap.xml redtoad.de:/var/www/redtoad.de/

blog/html/index.html:
	tinker --build

