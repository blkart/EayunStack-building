project_name = eayuncenter-docker-image
version = $(shell grep "Version" $(project_name).spec | awk '{print $$2}')
image_repo = http://docker.wencst.com:5000
image_name = $(shell grep 'global image_name' $(project_name).spec | awk '{print $$3}')
image_download_url = "$(image_repo)/$(image_name)"
spec_file = eayuncenter-docker-image.spec

sources:
	rm -rf $(project_name)-$(version)
	mkdir $(project_name)-$(version)
	wget -O $(project_name)-$(version)/eayuncenter-image.tar $(image_download_url)
	cp $(spec_file) $(project_name)-$(version)
	tar -czf $(project_name)-$(version).tgz $(project_name)-$(version)
