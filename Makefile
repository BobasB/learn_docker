FOLDERS := 1_Create_Dockerfile
DOCKER_REPO := bobas/learn_docker

.PHONY: $(FOLDERS)

$(FOLDERS):
	@docker build --no-cache -t ${DOCKER_REPO}:$(@) ./$(@)/ \
	&& docker push ${DOCKER_REPO} \
	&& docker run -it --rm --name test_it ${DOCKER_REPO}:$(@)