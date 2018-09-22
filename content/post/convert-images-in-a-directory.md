+++
title = "Convert Images in a Directory"
date = 2018-06-14T00:00:00
tags = ['bash']
categories = ["resources"]
+++


```bash
for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done
```
- `convert`: convert between image formats using ImageMagick

A simple bash for-loop for convert many images at once.
