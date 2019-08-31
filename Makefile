FOLDERS := 1_create_dockerfile 2_web_in_docker
DOCKER_REPO := bobas/learn_docker
PYTHON_VERSION := 3.7.4

.PHONY: $(FOLDERS) example_1 example_2

$(FOLDERS):
	@docker build --no-cache --build-arg image=${PYTHON_VERSION} -t ${DOCKER_REPO}:local ./$(@)/ \
	&& docker tag ${DOCKER_REPO}:local ${DOCKER_REPO}:$(@) \
	&& docker push ${DOCKER_REPO}:$(@) \

example_1:
	@docker run -it --rm --name test_it ${DOCKER_REPO}:local

example_2:
	@docker run -it --rm --name test_it --publish 5000:5000 --env message="It's in browser" ${DOCKER_REPO}:local

clean_docker:
	@docker rm $$(docker ps -a -q) || true && docker rmi $$(docker images -q) --force