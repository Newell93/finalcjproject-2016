#Elevator Pitch

**VaccinationRateMapper**

Have you ever wanted to know the vaccination rate of a school in your neighborhood? Maybe you're concerned since you're about to put your children in kindergarten, or you could be looking to identify schools where there aren't enough vaccinations to provide herd immunity against measles, mumps or rubella? Do you want the information to be individualized, as oppposed to being plotted on a giant map?

This application **will allow users to quickly type in the name of a nearby kindergarten to determine its vaccination rate.** This personalized app is easier to use than similar ones made by organizations like The New York Times and Hollywood Reporter. Using this app can help educate parents or curious neighbors as to whether their local schools have met their seal of approval when it comes to vaccination rates. It's also a look at the most current data from the 2015-16 school year.


#Prior Examples

**1. The Hollywood Reporter**

http://www.hollywoodreporter.com/features/los-angeles-vaccination-rates/fusion/

This does a great job of mapping all the available schools in Los Angeles, coloring them based on their vaccination-rate percentages.

It's a bit of an eyesore, and the app only contains info on Los Angeles County, not the entire state.


**2. The New York Times**

http://www.nytimes.com/interactive/2015/02/06/us/california-measles-vaccines-map.html?_r=0

A great visualization that highlights trends in where schools of high exemption rates are located, this example is the best use of mapping I have seen on vaccines.

**THERE IS NO SEARCH BAR.** It's a pain to find a school in your area.


**3. The Los Angeles Times**

http://www.latimes.com/local/california/la-me-measles-20150418-story.html

This is a good story describing how California may experience another measles outbreak in some areas because the vaccination rates there are so low. 

It also suggests that a measles outbreak could occur where a school's vaccination rate is below **86 percent.** This may be a good threshold to determine whether the schools in the dataset have built-in herd immunity.

**4. The San Jose Mercury News**

http://www.mercurynews.com/health/ci_28936729/california-vaccine-law-opponents-repeal-effort-fails-but

This is a good context story since it shows Gov. Brown signed a bill banning religious or personal belief exemptions from vaccines.

I don't think it's taken effect yet, so it's difficult to track whether the debate around the bill prompted more parents to vaccinate their children.

**5. Centers for Disease Control**

http://www.cdc.gov/measles/cases-outbreaks.html

After the measles outbreak near Disneyland (667 cases in 2014, 189 cases in 2015), the number of cases has decreased rapidly. Only 10 cases of measles have been cited this year.

This is good context because it shows measles paranoia/fear has subsided, though there are people who still want to know their school's average vaccination rate.


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

#Data Cleaning

**Oh boy.**

The data cleaning process took some time. I will do a breakdown the process below.

**1.** I started with **raw_kinder_data.xls**. It's a renamed version of the original file  from *https://www.cdph.ca.gov/programs/immunize/Documents/2015-16_CA_Kindergarten_Data.xls*.

**2.** Since the first four rows of the *.xls* file contain unnecessary text, I deleted them so the fifth row would become the first. I then re-named the columns with much simpler names. I made sure the corresponding columns still matched with the same data from the original *.xls* file.

**3.** I re-named this new file **clean_kinder.xls**. I would later make another copy called **clean_kinder.csv** so that I could make a join in SQLite.

**4.** I then started with **raw_school_codes.xls**. It's a renamed version of the original file from *ftp://ftp.cde.ca.gov/demo/schlname/pubschls.xls*.

**5.** I then created a new column called *school_code*. This was created by pulling the last seven digits from the much-larger school code. I need to perform this **-RIGHT** function so this school code could be joined with the seven-digit school code in **clean_kinder.xls**. Once completed, I named this **clean_school_codes.xls**.

**6.** Aaaaaaaaaaaaaaaand then I used SQLite to join both of my clean files.

**7.**This should be the SQL command I used, but you should be aware some of the imported file names are different than the .csv names.

**SELECT * 
FROM clean_kinder_kinder
JOIN clean_school_code
ON clean_kinder_kinder.school_code = clean_school_code.school_code
WHERE clean_kinder_kinder.enrollment != ''**


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
