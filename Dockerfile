FROM fike/jessie-locale:pt_BR

MAINTAINER Fernando Ike <fike@midstorm.org>

ENV DEBIAN_FRONTEND noninteractive

RUN sed -i 's/jessie\ main/jessie\ main\ contrib\ non-free/g' /etc/apt/sources.list && \
      sed -i 's/jessie\-updates\ main/jessie\-updates\ main\ contrib\ non-free/g' \ 
      /etc/apt/sources.list

RUN echo deb http://mozilla.debian.net/ jessie-backports \
       iceweasel-release >> /etc/apt/sources.list.d/mozilla.list

RUN apt-get update -y && apt-get upgrade -y && apt-get install curl -y 

RUN curl -O http://mozilla.debian.net/pkg-mozilla-archive-keyring_1.1_all.deb \
      && dpkg -i pkg-mozilla-archive-keyring_1.1_all.deb && rm *.deb && \
      apt-get update -y

RUN apt-get install --no-install-recommends xfonts-100dpi \
      xfonts-75dpi xfonts-scalable xfonts-cyrillic xvfb python-pip -qq && \
      apt-get install -t jessie-backports --no-install-recommends iceweasel \ 
      iceweasel-l10n-pt-br ca-certificates -qq  && apt-get install \ 
      --no-install-recommends flashplugin-nonfree icedtea-plugin -qq

RUN mkdir /opt/annabe && cd /opt/annabe 

RUN DOWNLOAD=$(curl -s https://github.com/firebug/firebug/releases | sed -n -e 's/.*\(firebug\/firebug\/archive\/firebug\-[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}\.tar\.gz*\).*/\1/p' |head -n1) && curl -O https://github.com/$DOWNLOAD

RUN DOWNLOAD=$(curl -s https://github.com/firebug/netexport/releases | sed -n -e 's/.*\(firebug\/netexport\/archive\/netExport\-.*\.tar\.gz*\).*/\1/p' |head -n1) && curl -O https://github.com/$DOWNLOAD 

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /annabe


