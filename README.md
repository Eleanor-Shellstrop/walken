# More Cowbell

Analysis between various statistics of Christopher Walken's film career and popular music that utilizes the cowbell.

![Fever](images/walken.gif)

## About

### Concept
The Saturday Night Live sketch "More Cowbell" aired on April 8, 2000.[^1] It quickly because a pop culture sensation.  Will Ferrell, an SNL cast member and writer, was responsibile for penning the famous sketch.[^2] On *The Tonight Show Starring Jimmy Fallon* in 2019, Ferrell recounted a conversation (with tongue-in-cheek) that he had backstage with Walken after a play:

> “You know, you’ve ruined my life. People, during the curtain call, bring cowbells and ring them. The other day I went for an Italian food lunch, and the waiter asked if I wanted more cowbell with my pasta bolognese.”[^3]

I am curious to see if there is any correlation with Walken's film career (ratings, number of films per year, etc.) and popular songs that incorporate cowbell into the percussion instruments used in recording. 

### Methodology

**Walken Data**

I accessed www.RottenTomatoes.com for Walken's films. Since the list was fairly short, it was easiest to copy/paste the data into a spreadsheet and create a CSV.

**Cowbell Data**

I made three webscrapers to collect song data:
1. `cowbell.py` This scraper ran through 4247 pages of UltimateCowbell.com[^4] to extract song information and wrote a CSV of the dataframe.
2. `script.js` This was a manual scraper. RollingStone.com[^5] had a list of "The 500 Greatest Songs of All Time," which I wanted to cross-check against the UltimateCowbell list. Rolling Stone's site is a dynamically loaded website, so the python scraper couldn't read the contents of the HTML. I only needed to run the scraper on 10 pages, so I made a JavaScript code to run in the console and copy/pasted the output into a spreadsheet. 
3. `billboard.py` This scraper ran through Wikipedia's lists of the Billboard's Hot 100 Singles[^6] between 1970 and 2020 and wrote a CSV. This list includes any single that reached a #1 position on the charts during this time, with pages separated by decades.  

I also copy/pasted a couple smaller lists of "best cowbell songs" and placed in another CSV to add to my cowbell sample size.[^7][^8] 

Overall, over 5,600 songs were taken into the data and analyzed. The final list came to 131 cowbell songs that are popular/mainstream, with release dates ranging from 1964 to 2017, and genres such as Rock, Country, R&B, Pop and more.

[^1]: [More Cowbell - SNL](https://www.youtube.com/watch?v=cVsQLlk-T0s), *Saturday Night Live*, YouTube
[^2]: [Recording Session (More Cowbell)](https://www.rollingstone.com/tv/tv-lists/my-favorite-saturday-night-live-sketch-119386/recording-session-more-cowbell-121088/), interview with Will Ferrell, *Rolling Stone Magazine.* 
[^3]: [Will Ferrell Ruined Christopher Walken's Life with SNL's More Cowbell Sketch](https://www.youtube.com/watch?v=j8kIzOr6DP8), *The Tonight Show Starring Jimmy Fallon*, YouTube
[^4]: [UltimateCowbell](http://ultimatecowbell.com)
[^5]: [Rolling Stone](https://www.rollingstone.com/music/music-lists/best-songs-of-all-time-1224767/kanye-west-stronger-1224837/)
[^6]: [List of Billboard Hot 100 Singles by Decade](https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1970s)
[^7]: [A to Z Songs that were Made Great by the Cowbell](https://medium.com/@s3605546/a-to-z-songs-that-were-made-great-by-the-cowbell-3734dd3a3535)
[^8]: [Friday Top: 25 Best Songs with Cowbell](https://www.ultimate-guitar.com/articles/features/friday_top_25_best_songs_with_cowbell-112673)