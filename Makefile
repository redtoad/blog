
all: clean build

build:
	hugo

clean:
	rm -rf public/

publish: clean build
	rsync -avz public/ redtoad.de:/var/www/redtoad.de
	#scp blog/html/sitemap.xml redtoad.de:/var/www/redtoad.de/

