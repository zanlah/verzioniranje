#!/bin/bash

hash="fd79657161253e076c8be6b87631449d1a4234e4"
sudo docker pull zanlah/filtriapp:${hash}

sudo docker run -ti zanlah/filtriapp:${hash}

