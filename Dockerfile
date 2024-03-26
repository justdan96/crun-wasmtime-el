# syntax=docker/dockerfile:1
ARG TAG=9.3
FROM almalinux:$TAG as builder
ARG TAG=9.3
ENV TAG=${TAG}
MAINTAINER Dan Bryant (daniel.bryant@linux.com)

RUN dnf update  -y --nogpgcheck
RUN dnf upgrade -y --nogpgcheck

RUN dnf --enablerepo='*' install -y autoconf automake gcc git libcap-devel libseccomp-devel libselinux-devel \
    libtool make systemd-devel bsdtar rpmdevtools yajl-devel glibc-static glib2-devel python3

# install wasmtime
RUN curl -sLo /tmp/wasmtime.tar.xz https://github.com/bytecodealliance/wasmtime/releases/download/v19.0.0/wasmtime-v19.0.0-x86_64-linux.tar.xz
RUN cd /usr/bin/ && bsdtar --strip-components=1 -xf /tmp/wasmtime.tar.xz
RUN curl -sLo /tmp/wasmtime-c-api.tar.xz https://github.com/bytecodealliance/wasmtime/releases/download/v19.0.0/wasmtime-v19.0.0-x86_64-linux-c-api.tar.xz
RUN cd /usr/local && bsdtar --strip-components=1 --exclude README.md --exclude LICENSE -xf /tmp/wasmtime-c-api.tar.xz

# make sure to alter the dist macro to explicitly mention the exact EL version
COPY alter-dist /usr/local/bin/alter-dist
RUN alter-dist
RUN mkdir -p /root/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN curl -sLo /root/rpmbuild/SOURCES/crun-1.14.4.tar.xz https://github.com/containers/crun/releases/download/1.14.4/crun-1.14.4.tar.xz
COPY crun.spec /root/rpmbuild/crun.spec
RUN rpmbuild -bb /root/rpmbuild/crun.spec
RUN curl -sLo /root/rpmbuild/SOURCES/v2.1.10.tar.gz https://github.com/containers/conmon/archive/refs/tags/v2.1.10.tar.gz
COPY conmon.spec /root/rpmbuild/conmon.spec
RUN rpmbuild -bb /root/rpmbuild/conmon.spec
RUN rm -f /root/rpmbuild/RPMS/x86_64/*debug*

# copy all the created RPMs to the host
FROM scratch AS export
COPY --from=builder /root/rpmbuild/RPMS/x86_64/*.rpm .
