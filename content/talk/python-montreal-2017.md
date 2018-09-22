+++
title = "Domo arigato, Mr. Roboto: Calibrating Robots with Python"
date = 2017-10-01T06:00:00-04:00  # Schedule page publish date.
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2017-10-01T06:00:00-04:00  

# Abstract and optional shortened version.
abstract = ""
abstract_short = ""

# Name of event and optional event URL.
event = "Montréal-Python 67: Ultramodern Vintage - PyCon Canada Special"
event_url = "https://montrealpython.org/en/2017/10/mp67/"

# Location of event.
location = "Montréal, QC"

# Is this a selected talk? (true/false)
selected = false

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter your project's filename without extension.
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
#   Otherwise, set `projects = []`.
projects = []

# Tags (optional).
#   Set `tags = []` for no tags, or use the form `tags = ["A Tag", "Another Tag"]` for one or more tags.
tags = ["python","robotics","mechanical"]

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = "https://youtu.be/wgKoGA69YXQ"
url_code = ""

# Does the content use math formatting?
math = false

# Does the content use source code highlighting?
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++

This talk was presented at [Montréal-Python 67: Ultramodern Vintage - PyCon Canada Special](https://montrealpython.org/2017/10/mp67/)

Modern robotic applications often rely on offline programming to reduce process downtime. In a virtual environment, robot application specialists may program, visualize, and test their robotic application before uploading it to the real production environment, saving time and costs. However, to achieve a high level of fidelity between virtual and production environments, the robot system must be accurate.

Unfortunately, even though most industrial robots are inherently precise (i.e., repeatable), they are not necessarily very accurate. One cost-effective approach to obtaining a more accurate robot is through calibration, where the actual kinematic and non-kinematic parameters of the robot model are identified and improved upon when compared to the nominal model. This talk introduces [`pybotics`](https://github.com/nnadeau/pybotics), an open-source Python toolbox for robot kinematics and calibration. The talk will feature the following topics:

- An introduction to modern industrial robotics
- Spatial descriptions and transformations
- Robot kinematics
- Robot calibration with `pybotics` + `NumPy` + `SciPy`

<iframe width="560" height="315" src="https://www.youtube.com/embed/wgKoGA69YXQ" frameborder="0" allowfullscreen></iframe>
