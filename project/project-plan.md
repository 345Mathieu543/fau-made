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

This analysis will use historical weather data, including temperature and rainfall measurements, along with pedestrian traffic data from the beginning of 2024 through the end of May 2024. The data is filtered and prepared through a Jayvee pipeline before being displayed in graphs and analyzed. Since there is no public weather data source directly in Erlangen, an average between the two surrounding locations Möhrendorf-Kleinseebach and Nuremberg Airport is calculated to determine the weather in Erlangen.

The significance of this project lies in understanding how weather affects pedestrian behavior, with implications for urban planning, traffic management, and retail strategies. Uncovering these relationships could potentially optimize urban layouts, improve infrastructure, and enhance the overall pedestrian experience.

Through rigorous data analysis and interpretation, valuable insights can be provided to policymakers, urban planners, and businesses operating in pedestrian-heavy areas such as Erlangen's downtown. Ultimately, the goal is to contribute to more informed decision-making processes and create more resilient and adaptable urban environments.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: [wetterkontor.de](https://www.wetterkontor.de)

"WetterKontor GmbH, based in Ingelheim am Rhein, was founded by former senior employees of Weathernews Germany and deals with the needs and interests of people with regard to the weather on a daily basis. We are present in the media every day: we are one of the leading developers of weather information for the print media in Germany." (translated citation from: [https://www.wetterkontor.de/de/ueberuns.asp](https://www.wetterkontor.de/de/ueberuns.asp))

URLs, where data was downloaded from:

* [Möhrendorf-Kleinseebach (01.01.2024 - 13.05.2024)](https://www.wetterkontor.de/de/wetter/deutschland/rueckblick.asp?id=P257&datum0=01.01.2024&datum1=13.05.2024&jr=2024&mo=5&datum=13.05.2024&t=8&part=0)
* [Nuremberg Airport (01.01.2024 - 13.05.2024)](https://www.wetterkontor.de/de/wetter/deutschland/rueckblick.asp?id=124&datum0=01.01.2024&datum1=13.05.2024&jr=2024&mo=5&datum=13.05.2024&t=8&part=0)

### Datasource 2: [hystreet.com](https://www.hystreet.com)

"Thanks to the laser technology used, we as a service provider are able to determine the exact pedestrian frequency in real time and make it available immediately. We attach great importance to absolute transparency and a clearly understandable methodology that is 100% data protection compliant." (translated citation from: [https://www.hystreet.com/](https://www.hystreet.com/))

URL, where data was downloaded from: [Erlangen Hugenottenplatz (01.01.2024 - 13.05.2024)](https://hystreet.com/locations/142?from=2023-12-31T23%3A00%3A00.000Z&to=2024-05-13T23%3A00%3A00.000Z)

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
