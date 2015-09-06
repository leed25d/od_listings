##Heroku Service:

[Heroku Link](https://still-island-5342.herokuapp.com/)

##Database

The listing.csv file was uploaded into a prostgres database for persistance

##Using the API

The API a single endpoint:
    GET /listings : returns a json coded list of entries from the database

These query args are accepted:
	min_price: Minimum price.
	max_price: Maximum price.
	min_bed: Minimum bedrooms.
	max_bed: Maximum bedrooms.
	min_bath: Minimum bathrooms.
	max_bath: Maximum bathrooms.

I added the 'status' field to the output properties even though it was not in the spec.

##Other features
    - add filtering on status (sold, pending, etc)
	- some kind of aggregating / sorting functionality
    - DRY up the filtering
    - Unit testing
