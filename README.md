```
                     ________                            
M               M   /_  __/ /  ___                       
M M           M M    / / / _ \/ -_)                      
M M M       M M M   /_/_/_//_/\__/         __        ____
M M M M   M M M M     /  |/  /__ ________ / /  ___ _/ / /
M M M M M M M M M    / /|_/ / _ `/ __(_-</ _ \/ _ `/ / / 
M M M M M M M M M   /_/__/_/\_,_/_/ /___/_//_/\_,_/_/_/  
M M M M M M M M M     / _ \_______    (_)__ ____/ /_     
M M M M M M M M M    / ___/ __/ _ \  / / -_) __/ __/     
M M M M M M M M M   /_/  /_/  \___/_/ /\__/\__/\__/     
                                 |___/  
```

#The Pentagon's 1033 program data

For more than 20 years, the Pentagon program that distributes surplus weapons, aircraft and vehicles to police departments nationwide received little attention or scrutiny. Defense Department officials closely guarded the details of which agencies across the country received which items.

Then, events in Ferguson, Mo. propelled the 1033 program, as the surplus distribution is called, into the public eye. Flooded with calls for greater transparency, in late November, 2014, the Pentagon quietly released data that details the tactical equipment it tracks through the program, and for the first time identified the agencies that received items. The data is a national [gift list](https://www.themarshallproject.org/2014/12/05/a-department-of-defense-gift-guide-2014) of high-caliber weapons, armored vehicles, aircraft and similar military equipment, all delivered for the price of shipping and often with little civilian oversight.

[The Marshall Project](https://www.themarshallproject.org/) and [MuckRock](https://www.muckrock.com/) worked together to produce [ stories](https://www.themarshallproject.org/2014/12/03/the-pentagon-finally-details-its-weapons-for-cops-giveaway) on the DoD's first release of agency-level data for tactical equipment.

Here, The Marshall Project is sharing the data we used in those stories, along with several other snapshots of the data that the Pentagon has put out since the summer of 2014. In this repository, you'll find the original Excel workbooks from the DoD, along with a script to combine a directory of these Excel files into a csv for analysis.

##Data sources
This data was downloaded from the website of the Department of Defense's Defense Logistics Agency's [Disposition Services](http://www.dispositionservices.dla.mil/EFOIA-Privacy/Pages/ereadingroom.aspx), which oversees the 1033 program distributions.

##Getting started
If you want to download everything from scratch, start here. Otherwise, jump to the Walkthrough section below.

In the ```data/dod_releases``` directory, you will find dated directories of the agency-level tactical data that the Pentagon has released.

You must have [make](https://www.gnu.org/software/make/), Python and [virtualenv](https://virtualenv.pypa.io/en/latest/) installed on your machine. If you do, clone this repo from Github and then type two commands.

```
make download
make csv
```

After a bunch of messages scroll across your screen as packages are installed and scripts run, you'll end up with a csv file that begins with today's date in the working directory.

##Walkthrough
In addition to helping you download the most current snapshot of the 1033 data, which updates roughly on a quarterly basis, we also include other releases at varying levels of granularity. In the ```data/dodreleases``` directory, you'll find two subdirectories, ```countylev``` and ```agencylev```. In the first, you'll find two snapshots of the data with separate tabs for "General" equipment that went to specific agencies and "Tactical" equipment and the counties it went to (read more in this [great guide to 1033](https://github.com/SCPR/kpcc-data-team/blob/master/guides/primer-on-defense-logistics-agencys-1033-program-data.md) about the differences between those categories). Starting in November, 2014, the Pentagon started releasing agency-level records for both types of equipment. That snapshot and subsequent releases are in the ```agencylev``` directory. Each data snapshot is in a directory named for the date it was released.

Our ```dodcombine.py``` script can combine spreadsheets in any of the directories. The script's defaults will look to combine spreadsheets in the ```data/current``` directory (presumably downloaded from the website today). For instance, if you already have your own virtualenv with pandas installed and you've downloaded the spreadsheets from DoD into your ```data/current``` directory, you can run the script directly with ```python dodcombine.py```

If you want to look at the older releases, use the -d flag and give it the directory where those csvs live, like this:

```python dodcombine.py -d 'data/dod_releases/agencylev/2014-11-21'```

By default, the script will create a file with today's date followed by ''-dod-snapshot.csv'. If you want to name your file something different, particularly if you're using one of the older releases, use the -o flag with the script.

```python dodcombine.py -o 'november.csv'```

##Working with the data and caveats
Now that you have a handy csv of the 1033 release you prefer, you may want to do some analysis to see what your local police departments have received from the program.

Before you do anything, you *must read* this [handy guide to the pitfalls of 1033 data](https://github.com/SCPR/kpcc-data-team/blob/master/guides/primer-on-defense-logistics-agencys-1033-program-data.md), by our friends at KPCC.

This passage is especially important to keep in mind:
>The data released by the Defense Logistics Agency on Nov. 21 is current as of Nov. 13, 2014, but is not a historical record. With some caveats, it could be thought of as a snapshot of controlled items still in the possession of law enforcement agencies over the life of the program.

>For example, the data doesn't allow us to say whether the amount equipment acquired by an agency has increased over time. We can only say when the equipment that is currently at an agency arrived there.

>If a law enforcement agency returns, transfers or discards an item it simply no longer appears in data for that agency.

That said, the collected data releases in this repository could provide journalists and other researchers the means to analyze how weapons are distributed to individual police departments over time. We hope others will take up the challenge.

##Contributors
Tom Meagher, [The Marshall Project](https://www.themarshallproject.org/)

##Bugs
If you have questions or see any problems with the data or the scripts, please file a [Github issue](https://github.com/themarshallproject/dod1033/issues), or email Tom at ```tmeagher@themarshallproject.org```
