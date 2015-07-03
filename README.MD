# Annabe - Simple site test

Annabe is simple site test that output a har file.

### Idea

At the moment, Annabe doesn't work. So, it's a fun idea to collect a web browser and analyze.


### How to work

The main idea is two scripts, the first call the container that it makes the tests. The second script run in container inside using selenium.


#### Building container

$docker built -t annabe .

#### Running container

$docker run -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/shm:/dev/shm -e DISPLAY=${DISPLAY} -it annabe /bin/bash  


## Author

Annabe was Leandro Cassiano idea and the initial version.
