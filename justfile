default:
  just --list

build:
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=8.7 . --output out
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=8.8 . --output out
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=8.9 . --output out
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=9.0 . --output out
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=9.1 . --output out
  DOCKER_BUILDKIT=1 docker build --target export -t crun --build-arg TAG=9.3 . --output out
