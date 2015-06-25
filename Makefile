DOCKER = docker --tlsverify=false

test:
	$(DOCKER) run -it --rm -v $(shell pwd):/python-misc python-misc

build:
	$(DOCKER) build -t python-misc .

all: build test
