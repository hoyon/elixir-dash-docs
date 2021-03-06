#!/bin/bash

set -eo pipefail

if [ "$#" -ne 1 ]
then
    echo "package name required"
    exit 1
fi

package=$1

package_json=$(curl -H "Accept: application/json" https://hex.pm/api/packages/"$package")

package_version=$(echo "$package_json" | jq -r "[.releases[] | select( .has_docs == true )] | first .version")

wget https://repo.hex.pm/docs/"$package"-"$package_version".tar.gz -O docs.tar.gz

rm -rf ./docs
mkdir ./docs

tar xzf docs.tar.gz -C docs

rm docs.tar.gz

cp logo.png docs/logo.png
cp dashing.json docs/dashing.json

rm docs/404.html

sed -i "s/NAME/${package^}/" docs/dashing.json
sed -i "s/PACKAGE/$package/" docs/dashing.json

python3 process_html.py

pushd docs
dashing build
popd

mkdir -p docsets
rm -rf docsets/"$package".docset
mv docs/"$package".docset docsets
