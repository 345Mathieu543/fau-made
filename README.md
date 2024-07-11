# Project Plan

## Title

<!-- Give your project a short title. -->

Weather Impact on Pedestrian Traffic.

## Main Question

<!-- Think about one main question you want to answer based on the data. -->

Do temperature and rainfall negatively correlate with the number of people walking through the pedestrian zone in Erlangen?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

This data science project focuses on the relationship between weather conditions and pedestrian traffic in Erlangen's pedestrian zone. The primary question is whether temperature and rainfall have a negative correlation with the number of people walking in the area.

This analysis uses historical weather data, including temperature and rainfall measurements, along with pedestrian traffic data from yesterday to 550 days in the past. The data is collected, filtered, and prepared through Python and Jayvee pipelines before being displayed in graphs and analyzed. Since there is no public weather data source directly in Erlangen, an average between the two surrounding locations 'Möhrendorf-Kleinseebach' and 'Nürnberg Airport' is calculated to determine the weather in Erlangen.

The significance of this project lies in understanding how weather affects pedestrian behavior, with implications for urban planning, traffic management, and retail strategies. Uncovering these relationships could potentially optimize urban layouts, improve infrastructure, and enhance the overall pedestrian experience. Ultimately, the goal is to contribute to more informed decision-making processes and create more resilient and adaptable urban environments.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: [opendata.dwd.de](https://opendata.dwd.de)

"The German Meteorological Service (DWD) is a higher federal authority within the portfolio of the Federal Ministry for Digital and Transport Affairs. It is responsible for meeting the meteorological requirements of all economic and social sectors in Germany. \[Their] tasks are based on a statutory information and research mandate, the German Weather Service Act." (translated citation from: [https://www.dwd.de/DE/derdwd/derdwd_node.html](https://www.dwd.de/DE/derdwd/derdwd_node.html))

The required data (rainfall per day and average temperature per day) is split into two different ZIP archives per weather station. As mentioned above, the weather stations 'Möhrendorf-Kleinseebach' (ID: 01279) and 'Nürnberg Airport' (ID: 03668) are used. The average of the data is taken as the weather data for Erlangen, since it is geographically located in the middle.

### Datasource 2: [hystreet.com](https://www.hystreet.com)

"Thanks to the laser technology used, we as a service provider are able to determine the exact pedestrian frequency in real time and make it available immediately. We attach great importance to absolute transparency and a clearly understandable methodology that is 100% data protection compliant." (translated citation from: [https://www.hystreet.com/](https://www.hystreet.com/))

This data source also provides some weather data, but we prefer to use the weather data from the German Weather Service. Furthermore, this project needs at least two data sources. So this data source will only be used to extract the number of pedestrians per day in the pedestrian zone of Erlangen.

# Exercise Badges

![](https://byob.yarr.is/345Mathieu543/fau-made/score_ex1) ![](https://byob.yarr.is/345Mathieu543/fau-made/score_ex2) ![](https://byob.yarr.is/345Mathieu543/fau-made/score_ex3) ![](https://byob.yarr.is/345Mathieu543/fau-made/score_ex4) ![](https://byob.yarr.is/345Mathieu543/fau-made/score_ex5)

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
