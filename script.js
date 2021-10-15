// Artist, Title, Year
for (let i = 0; i < 200; i++) {
    title = document.getElementsByClassName("c-gallery-vertical-album__title")[i].innerHTML
	year = document.getElementsByClassName("rs-list-item--year")[i].innerHTML
	console.log(title + ", " + year)
}