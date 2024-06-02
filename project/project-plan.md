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

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Download Data [#1][i1]
2. Analyze Data [#2][i2]
3. Import Data to a SQLite Database [#3][i3]
4. Calculate Average Temp and Rain [#4][i4]
5. Plot meaningful Graphs [#5][i5]
6. Analyze Graphs [#6][i6]
7. Write Final Report [#7][i7]
8. Prepare Presentation of the Results [#8][i8]

[i1]: https://github.com/345Mathieu543/fau-made/issues/1
[i2]: https://github.com/345Mathieu543/fau-made/issues/2
[i3]: https://github.com/345Mathieu543/fau-made/issues/3
[i4]: https://github.com/345Mathieu543/fau-made/issues/4
[i5]: https://github.com/345Mathieu543/fau-made/issues/5
[i6]: https://github.com/345Mathieu543/fau-made/issues/6
[i7]: https://github.com/345Mathieu543/fau-made/issues/7
[i8]: https://github.com/345Mathieu543/fau-made/issues/8
