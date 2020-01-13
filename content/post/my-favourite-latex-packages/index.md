+++
title = "My Favourite LaTeX Packages"
date = 2018-06-25T22:13:30
tags = ['latex', 'phd']
categories = ["resources"]
summary = " "
+++


```latex
% english hyphenation
\usepackage[english]{babel}

% for accented characters, load before csquotes
\usepackage[utf8]{inputenc}

% recommended with babel; \enquote{}
\usepackage{csquotes}

% for \graphicspath
\usepackage{graphicx}
\graphicspath{{./fig/}}

% \toprule, \midrule, \multicolumn
\usepackage{booktabs}

% unit formatting
\usepackage[per-mode=symbol]{siunitx}

% siunitx match IEEE font weight
\sisetup{detect-weight=true, detect-family=true}

% \FloatBarrier for stopping floats in REFERNCES section
\usepackage{placeins}

% linked references
\usepackage{hyperref}

% citations
% https://www.sharelatex.com/learn/Bibliography_management_in_LaTeX
\usepackage[
style=ieee,
doi=false,
isbn=false,
url=false,
]{biblatex}
\addbibresource{kuka-collaborative-poke.bib}

% easy referencing, must be loaded last!
\usepackage[capitalise]{cleveref}
```