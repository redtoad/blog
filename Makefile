
all: clean publish

clean:
	rm -rf public/

publish:
	hugo
	rsync -avz public/ redtoad.de:/var/www/redtoad.de
	#scp blog/html/sitemap.xml redtoad.de:/var/www/redtoad.de/

