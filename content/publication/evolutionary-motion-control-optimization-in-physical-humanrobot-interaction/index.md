+++
title = "Evolutionary Motion Control Optimization in Physical Human-Robot Interaction"
date = 2018-10-01T21:30:09-04:00
draft = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Nicholas A. Nadeau, Ilian A. Bonev"]

# Publication type.
# Legend:
# 0 = Uncategorized
# 1 = Conference paper
# 2 = Journal article
# 3 = Manuscript
# 4 = Report
# 5 = Book
# 6 = Book section
publication_types = ["1"]

# Publication name and optional abbreviated version.
publication = "IEEE/RSJ International Conference on Intelligent Robots and Systems"
publication_short = "IROS"

# Abstract and optional shortened version.
abstract = "Given that the success of an interaction task depends on the capability of the robot system to handle physical contact with its environment, pure motion control is often insufficient. This is especially true in the context of medical freehand ultrasound where the human body is a deformable surface and an unstructured environment, representing both a safety concern and a challenge for trajectory planning and control. The systematic tuning of practical high degree-of-freedom physical human-robot interaction (pHRI) tasks is not trivial and there are many parameters to be tuned. While traditional tuning is generally performed *ad hoc* and requires knowledge of the robot and environment dynamics, we propose a simple and effective online tuning framework using differential evolution (DE) to optimize the motion parameters for parallel force/impedance control in a pHRI and medical ultrasound motion application. Through real-world experiments with a KUKA LBR iiwa 7 R800 collaborative robot, the DE framework tuned motion control for optimal and safe trajectories along a human leg phantom. The optimization process was able to successfully reduce the mean absolute error of the motion contact force to 0.537N through the evolution of eight motion control parameters."
abstract_short = ""

# Featured image thumbnail (optional)
image_preview = ""

# Is this a selected publication? (true/false)
selected = false

# Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's filename without extension.
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
#   Otherwise, set `projects = []`.
projects = []

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = []

# Links (optional).
url_pdf = ""
url_preprint = ""
url_code = ""
url_dataset = ""
url_project = ""
url_slides = ""
url_video = ""
url_poster = ""
url_source = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{name = "Custom Link", url = "http://example.org"}]

# Does this page contain LaTeX math? (true/false)
math = false

# Does this page require source code highlighting? (true/false)
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

![Evolutionary Motion Control](/img/kuka-evo (1).gif)

![Evolutionary Motion Control](/img/kuka-evo (4).gif)