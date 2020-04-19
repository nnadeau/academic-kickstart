+++
title = "Stop LaTeX Floats and Figures from Appearing in References Section"
date = 2018-06-25T22:13:30
tags = ["document", "figure", "phd", "placein", "printbibliography", "refernces", "resources", "usepackage"]
categories = ["resources"]
summary = " "
+++


```latex
% \FloatBarrier for stopping floats in REFERNCES section
\usepackage{placeins}

...
...
...

\FloatBarrier
\printbibliography
\end{document}
```
