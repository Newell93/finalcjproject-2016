#Elevator Pitch

**VaccinationRateMapper**

Have you ever wanted to know whether the vaccination rate of a school in your neighborhood? Maybe you're concerned since you're about to put your children in kindergarten, or you could be looking to identify schools where there aren't enough vaccinations to provide herd immunity against measles, mumps or rubella? Do you want the information to be individualized, as oppposed to being plotted on a giant map?

This application **will allow users to quickly type in the name of a nearby K-8 school to determine its vaccination rate.** This personalized app is easier to use than similar ones made by organizations like The New York Times and Hollywood Reporter. Using this app can help educate parents or curious neighbors as to whether their local schools have met their seal of approval when it comes to vaccination rates. It's also a look at the most current data from the 2015-16 school year.


#Prior Examples

*1. The Hollywood Reporter* 

http://www.hollywoodreporter.com/features/los-angeles-vaccination-rates/fusion/

This does a great job of mapping all the available schools in Los Angeles, coloring them based on their vaccination-rate percentages.

It's a bit of an eyesore, and the app only contains info on Los Angeles County, not the entire state.


*2. The New York Times*

http://www.nytimes.com/interactive/2015/02/06/us/california-measles-vaccines-map.html?_r=0


#Data
**1.** My primary source of data comes from the California Department of Health.

https://www.cdph.ca.gov/programs/immunize/Pages/ImmunizationLevels.aspx

https://www.cdph.ca.gov/programs/immunize/Documents/2015-2016%20CA%20Child%20Care%20Data.xlsx

https://www.cdph.ca.gov/programs/immunize/Documents/2015-2016%20CA%207th%20Grade%20Data_021816.xls


The site has .xls files of vaccination rates for students enrolled in kindergarten and seventh-grade. The data contains unique identifiers like school code, county, school name, vaccination rate and the percentage of students with a belief or medical exemption from vaccines. I plan on *adding* the two .xls files together to get one master list of rates in kindergartens and middle schools across the state.

**2.** My secondary source of data comes from the California Department of Education. 

http://www.cde.ca.gov/ds/si/ds/pubschls.asp

ftp://ftp.cde.ca.gov/demo/schlname/pubschls.xls

This contains more information about each school, and it can be joined with the first dataset on the school code field. This dataset lists the entire school code, roughly 14 characters, while the prior set does not. I can write a **--RIGHT--** function to strip the last five school code characters in the first dataset to join it with this one. It isn't very hard to do.

This dataset also contains coordinates, which I could use to plot points on a map if I choose. It might be nice to feed these coordinates into a Google Maps API to get a screenshot of each school that the user asks about.

The **new categorial variable** will be a 'Yes' or 'No.' This will refer to whether the school has herd immunity, which is based on whether its vaccination rate is high enough to prevent an epidemic from spreading amongst the kids.

I'm having trouble identifying what the **new continuous variable** could be in this case.

#Filtering Options

My goal for this project is to allow users to pick a school by including its partial name, let the app identify a match, and then present pertinent info about the school **[name, location, vaccination rate, belief-exemption rate and other factors]** and a satellite or streetview image.


I could also allow them to find schools by looking at a drop-down county menu that could also let them find a list of schools in their area.

Users can **sort** the data by vaccination rate or belief exemption rate as percentages, ascending or descending. 

#Views and Routes

Not much to say about these at this point. I will include screenshots when the app is built.


#Visualizations

Same as **Views and Routes.**

#Deployment

Same as **Views and Routes.**
