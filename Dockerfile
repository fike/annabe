FROM fike/jessie-locale:pt_BR

MAINTAINER Fernando Ike <fike@midstorm.org>

ENV DEBIAN_FRONTEND noninteractive

ADD firefox_navigate.py /usr/local/bin/

ADD start.sh

RUN chmod +x /usr/local/bin/firefox_navigate.py start.sh && mkdir /opt/annabe

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

RUN pip install selenium

WORKDIR /opt/annabe

RUN curl -s --location -O $(curl -s --location https://addons.mozilla.org/firefox/addon/firebug/versions/ | \
      sed  -n -e 's/.*\(https\:\/\/addons\.mozilla\.org\/.*\/firebug\-2.0.11\-fx\.xpi*\).*/\1/p')

RUN curl -s --location -O $(curl -s --location http://getfirebug.com/releases/netexport/update.rdf | \
      sed -n -e 's/.*\(https\:\/\/getfirebug\.com\/.*\/netExport\-.*\.xpi*\).*/\1/p')

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD /bin/bash
