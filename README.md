Script to create dash/zeal docsets for Elixir packages.

### Requirements: 
* [dashing](https://github.com/technosophos/dashing)
* python3 with beautiful soup and html5lib installed
* jq
* curl
* wget

### Running:

```
cd elixir-dash-docs
./build.sh PACKAGE
```

The docsets will be created in `./docsets` and should then be copied into your docsets directory
