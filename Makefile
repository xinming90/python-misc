DOCKER = docker --tlsverify=false

test:
	find __pycache__ -type f | xargs rm -f
	$(DOCKER) run -it --rm -v $(shell pwd):/python-misc python-misc

build:
	$(DOCKER) build -t python-misc .

all: build test
