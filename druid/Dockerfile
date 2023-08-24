FROM openjdk:8

ARG DRUID_VERSION=24.0.1
ENV DRUID_VERSION ${DRUID_VERSION}
ENV LOG_LEVEL info

RUN apt-get update \
      && apt-get install -y curl

# Install druid
RUN curl https://archive.apache.org/dist/druid/${DRUID_VERSION}/apache-druid-${DRUID_VERSION}-bin.tar.gz > /opt/druid-${DRUID_VERSION}-bin.tar.gz \
      && tar -xvf /opt/druid-${DRUID_VERSION}-bin.tar.gz -C /opt/ \
      && rm -f /opt/druid-${DRUID_VERSION}-bin.tar.gz \
      && mv /opt/apache-druid-${DRUID_VERSION} /opt/druid \
      && mkdir -p /var/log/druid \
      && mkdir -p /opt/druid/data \
      && rm -rf /opt/druid/conf /opt/druid/conf-quickstart

ARG MAVEN_REPO=https://repo1.maven.org/maven2
ENV MAVEN_REPO ${MAVEN_REPO}
RUN curl ${MAVEN_REPO}/org/postgresql/postgresql/42.4.3/postgresql-42.4.3.jar > /opt/druid/extensions/postgresql-metadata-storage/postgresql-42.4.3.jar

COPY conf /opt/druid/conf/
COPY druid-start.sh /usr/bin/
COPY druid-service-checker.sh /usr/bin/
COPY druid-pull-deps.sh /usr/bin/

RUN chmod +x /usr/bin/druid-start.sh \
     && chmod +x /usr/bin/druid-service-checker.sh \
     && chmod +x /usr/bin/druid-pull-deps.sh

WORKDIR /opt/druid

CMD druid-start.sh
