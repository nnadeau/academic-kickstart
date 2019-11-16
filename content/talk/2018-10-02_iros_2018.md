+++
title = "Evolutionary Motion Control Optimization in Physical Human-Robot Interaction"
date = 2018-10-02T14:30:00
draft = false

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
time_start = 2018-10-02T14:30:00
time_end = 2018-10-02T15:00:00

# Abstract and optional shortened version.
abstract = "Given that the success of an interaction task depends on the capability of the robot system to handle physical contact with its environment, pure motion control is often insufficient. This is especially true in the context of medical freehand ultrasound where the human body is a deformable surface and an unstructured environment, representing both a safety concern and a challenge for trajectory planning and control. The systematic tuning of practical high degree-of-freedom physical human-robot interaction (pHRI) tasks is not trivial and there are many parameters to be tuned. While traditional tuning is generally performed ad hoc and requires knowledge of the robot and environment dynamics, we propose a simple and effective online tuning framework using differential evolution (DE) to optimize the motion parameters for parallel force/impedance control in a pHRI and medical ultrasound motion application. Through real-world experiments with a KUKA LBR iiwa 7 R800 collaborative robot, the DE framework tuned motion control for optimal and safe trajectories along a human leg phantom. The optimization process was able to successfully reduce the mean absolute error of the motion contact force to 0.537 N through the evolution of eight motion control parameters."
summary = ""

# Name of event and optional event URL.
event = "2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)"
event_url = "https://ras.papercept.net/conferences/conferences/IROS18/program/IROS18_ContentListWeb_2.html"

# Location of event.
location = "Madrid, Spain"

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
tags = ["robotics","phd","conference"]

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
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

![Evolutionary Motion Control](https://res.cloudinary.com/nicholasnadeau/image/upload/v1549748468/kuka-evo_1.gif)

![Evolutionary Motion Control](https://res.cloudinary.com/nicholasnadeau/image/upload/v1549748471/kuka-evo_4.gif)
