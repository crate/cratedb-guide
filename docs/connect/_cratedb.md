---
orphan: true
---
Start CrateDB using Docker or Podman, then invoke the example program.
```shell
docker run --rm --publish=5432:5432 docker.io/crate '-Cdiscovery.type=single-node'
```
