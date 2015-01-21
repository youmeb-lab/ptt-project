start:
	@docker run \
		-d --name nsqd \
		-p 4150:4150 \
		-p 4151:4151 \
		nsqio/nsqd

	@docker run \
		--name workspace \
		--rm -it \
		-v $(shell pwd):/workspace \
		-w /workspace \
		--link nsqd:nsqd \
		python:2.7.9 bash

stop:
	docker rm -f nsqd workspace
