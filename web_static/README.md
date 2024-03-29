## AirBnb clone - Web static
A static web page for the AirBnB application. A prototype for the actual website.

#### Task 0: Inline styling
[0-index.html](0-index.html) is a HTML page that displays a header and footer styled with inline styling.

#### Task 1: Head styling
[1-index.html](1-index.html) is a HTML page that creates the same exact layout as [0-index.html](0-index.html) using the `style` tag in the `head` tag.

#### Task 2: CSS files
[2-index.html](2-index.html) is a HTML page that creates the same exact layout as [0-index.html](0-index.html) using the CSS files [styles/2-common.css](styles/2-common.css), [styles/2-header.css](styles/2-header.css) and [styles/2-footer.css](styles/2-footer.css).

#### Task 3: Zoning done!
[3-index.html](3-index.html) is HTML page that displays a header and footer styled using CSS files.
Layout:
- Common (stylesheet: [styles/3-common.css](styles/3-common.css)):
	- no margin
	- no padding
	- font color: #484848
	- font size: 14px
	- font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
	- [images/icon.png](images/icon.png) in the browser tab
- Header (stylesheet: [styles/3-header.css](styles/3-header.css)):
	- color: white
	- height: 70px
	- width: 100%
	- border bottom 1px #CCCCCC
	- [images/logo.png](images/logo.png) align on left and center vertically (20px space at the left)
- Footer (stylesheet: [styles/3-footer.css](styles/3-footer.css)):
	- color white
	- height: 60px
	- width: 100%
	- border top 1px #CCCCCC
	- text `Best School` center vertically and horizontally
	- always at the bottom at the page

#### Task 4: Search!
[4-index.html](4-index.html) is a HTML page that displays a header, footer and a filters box with a search button.
Layout: (based on [3-index.html](3-index.html))
- Container (styled in [styles/4-common.css](styles/4-common.css)):
	- A `div` between `header` and `footer` tags:
		- class: `container`
		- max width 1000px
		- margin top and bottom 30px
		- center horizontally
- Filter section (styled in [styles/4-filters.css](styles/4-filters.css)):
	- tag `section`
	- class: `filters`
	- inside the `.container`
	- color white
	- height 70px
	- width 100% of `container`
	- border 1px #DDDDDD with radius 4px
- Button search:
	- tag `button`
	- text `Search`
	- font size: 18px
	- inside `.filters`
	- background color #FF5A5F
	- text color #FFFFFF
	- height 48px
	- width 20% of `.filters`
	- no borders
	- border radius 4px
	- center vertically at 30px of the right border
	- change opacity to 90% when the mouse is over the button

#### Task 5: More filters
[5-index.html](5-index.html) is a HTML page that displays a header, footer and a filters box.
Layout: (based on [4-index.html](4-index.html)
- Locations and Amenities filters (styled in [styles/5-filters.css](styles/5-filters.css)):
	- tag: `div`
	- classname: `locations` for location tag and `amenities` for the other
	- inside the section `filters` (same level as the `button` Search)
	- height: 100% of the section filters
	- width: 25% of the section filters
	- border right #DDDDDD 1px only for the first left filter
	- contains a title:
		- tag: `h3`
		- font weight: 600
		- text `States` or `Amenities`
	- contains a subtitle:
		- tag: `h4`
		- font weight: 400
		- font size: 14px
		- text with fake contents

#### Task 6: It's (h)over
[6-index.html](6-index.html) is a HTML page that displays a header, footer and a filters box with dropdown.
Layout: (based on [5-index.html](5-index.html))
- Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
	- tag `ul`
	- classname `popover`
	- text should be fake now
	- inside each `div`
	- not displayed by default
	- color #FAFAFA
	- width same as the `div` filter
	- border #DDDDDD 1px with border radius 4px
	- no list display
	- Location filter has 2 levels of `ul`/`li`:
		- state -> cities
		- state name must be display in a `h2` tag (font size 16px)

#### Task 7: Display results
[7-index.html](7-index.html) is a HTML page that displays a header, footer, a filters box with dropdown and results.
Layout: (based on [6-index.html](6-index.html))
- Add Places section:
	- tag: `section`
	- classname: `places`
	- same level as the filters section, inside `.container`
	- contains a title:
		- tag: `h1`
		- text: `Places`
		- align in the top left
		- font size: 30px
	- contains multiple “Places” as listing (horizontal or vertical) describe by:
		- tag: `article`
		- width: 390px
		- padding and margin 20px
		- border #FF5A5F 1px with radius 4px
		- contains the place name:
			- tag: `h2`
			- font size: 30px
			- center horizontally

#### Task 8: More details
[8-index.html](8-index.html) is a HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Layout: (based on [7-index.html](7-index.html))
Add more information to a Place `article`:
- Price by night:
	- tag: `div`
	- classname: `price_by_night`
	- same level as the place name
	- font color: #FF5A5F
	- border: #FF5A5F 4px rounded
	- min width: 60px
	- height: 60px
	- font size: 30px
	- align: the top right (with space)
- Information section:
	- tag: `div`
	- classname: `information`
	- height: 80px
	- border: top and bottom #DDDDDD 1px
	- contains (align vertically):
		- Number of guests:
			- tag: `div`
			- classname: `max_guest`
			- width: 100px
			- fake text
			- [icon](images/icon_guest.png)
		- Number of bedrooms:
			- tag: `div`
			- classname: `number_rooms`
			- width: 100px
			- fake text
			- [icon](images.icon_bed.png)
		- Number of bathrooms:
			- tag: `div`
			- classname: `number_bathrooms`
			- width: 100px
			- fake text
			- [icon](images/icon_bath.png)
- User section:
	- tag: `div`
	- classname: `user`
	- text `Owner: <fake text>`
	- `Owner` text should be in bold
- Description section:
	- tag: `div`
	- classname: `description`


#### Task 9: Full details
[10-index.html](100-index.html) is a HTML page that displays a header, footer, a filters box with dropdown and results.
Layout: (based on [8-index.html](8-index.html))
Add more information to a Place article:
- List of Amenities:
	- tag `div`
	- classname `amenities`
	- margin top 40px
	- contains:
		- title:
			- tag `h2`
			- text `Amenities`
			- font size 16px
			- border bottom #DDDDDD 1px
		- list of amenities:
			- tag `ul` / `li`
			- no list style
			- icons on the left: [Pet friendly](images/icon_pets.png), [TV](images/icon_tv.png), [Wifi](images/icon_wifi.png), etc
- List of Reviews:
	- tag `div`
	- classname `reviews`
	- margin top 40px
	- contains:
		- title:
			- tag `h2`
			- text `Reviews`
			- font size 16px
			- border bottom #DDDDDD 1px
		- list of review:
			- tag `ul` / `li`
			- no list style
			- a review is described by:
				- `h3` tag for the user/date description (font size 14px).
				- `p` tag for the text (font size 12px)

#### Task 10: Flex
[101-index.html](101-index.html) is a HTML page that improves the Places section by using Flexible boxes for all Place articles (stylesheet: [styles/101-places.css](styles/101-paces.css)).

#### Task 11: Responsive design
Improves the page by adding resposive design to display correctly in mobile or small screens.
- no horizontal scrolling
- redesign search bar depending on the width
