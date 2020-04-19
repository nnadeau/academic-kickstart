+++
title = "Count the Number of Words in a LaTeX Document"
date = 2018-06-14T00:00:00
tags = ["bash", "byte", "character", "command", "count", "log", "number", "output", "record", "resources", "word","latex"]
categories = ["resources"]
+++


```bash
detex my-document.tex | wc -w
```

- `detex`: a filter to strip TeX commands from a .tex file
- `wc`: word, line, character, and byte count
    - `-w`: The number of words in each input file is written to the standard output
