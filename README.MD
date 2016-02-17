# Annabe - Simple site test

Annabe is simple site test that output a har file.

### Idea

At the moment, Annabe doesn't work. So, it's a fun idea to collect a web browser and analyze.


### How to work

The main idea is two scripts, the first call the container that it makes the tests. The second script run in container inside using selenium.


#### Building container

    $docker built -t annabe .

#### Running container

    $docker run --rm -v /tmp/har:/tmp/har -it annabe annabe http://www.fernandoike.com

##### Multiples URLS

    $for i in $(echo "http://www.fernandoike.com http://www.uol.com.br") 
    do 
      docker run -v /tmp/har:/tmp/har fike/annabe annabe $i 
    done

    $for i in $(cat url_list.txt)
    do
      docker run -v /tmp/har:/tmp/har fike/annabe annabe $i
    done 
 
## Author

Annabe was Leandro Cassiano idea and the initial version.
