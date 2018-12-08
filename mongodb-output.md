## Query 1 - List All Model SC Juggernaut Scooters
```
> db.scooters.find({"scooter_type":"SC Juggernaut"})

{ "_id" : ObjectId("5c0b7815005b567f0fb45c7a"), "acquired_date" : "2017-03-13", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c7b"), "acquired_date" : "2017-11-03", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c7c"), "acquired_date" : "2016-12-16", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c8c"), "acquired_date" : "2014-10-28", "retired" : true, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c8f"), "acquired_date" : "2017-08-28", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c90"), "acquired_date" : "2014-01-05", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c91"), "acquired_date" : "2016-10-21", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c96"), "acquired_date" : "2014-03-20", "retired" : false, "scooter_type" : "SC Juggernaut", "max_speed" : 50, "weight" : 100, "manufacturer" : "Special Company", "website" : "vspecial.com" }
```

## Query 2 - Include Only Acquire Date, Retired and Model
```
> db.scooters.find({}, {_id:0, "scooter_type":1, "acquired_date":1, "retired":1}).limit(10)

{ "acquired_date" : "2017-03-13", "retired" : false, "scooter_type" : "SC Juggernaut" }
{ "acquired_date" : "2017-11-03", "retired" : false, "scooter_type" : "SC Juggernaut" }
{ "acquired_date" : "2016-12-16", "retired" : false, "scooter_type" : "SC Juggernaut" }
{ "acquired_date" : "2014-03-28", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2016-03-24", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-01-15", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-09-17", "retired" : true, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2015-11-25", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2017-09-21", "retired" : true, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2017-04-14", "retired" : false, "scooter_type" : "SC Sonic" }
```

## Query 3 - Non-Retired Scooters Acquired After 2018 (No \_id)
```
> db.scooters.find(
... {"$and": [{"acquired_date":{"$gte":'2018-01-01'}},
... {"retired":false}]},
... {_id:0, "acquired_date":1, "retired":1, "scooter_type":1})

{ "acquired_date" : "2018-01-15", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-03-11", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-09-03", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-03-17", "retired" : false, "scooter_type" : "GC Boring" }
{ "acquired_date" : "2018-01-22", "retired" : false, "scooter_type" : "GC Generic" }
{ "acquired_date" : "2018-11-13", "retired" : false, "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-01-16", "retired" : false, "scooter_type" : "GC Generic" }
{ "acquired_date" : "2018-05-28", "retired" : false, "scooter_type" : "GC Generic" }
{ "acquired_date" : "2018-07-17", "retired" : false, "scooter_type" : "GC Boring" }
{ "acquired_date" : "2018-07-15", "retired" : false, "scooter_type" : "GC Boring" }
{ "acquired_date" : "2018-05-05", "retired" : false, "scooter_type" : "FC Mk.1" }
{ "acquired_date" : "2018-05-08", "retired" : false, "scooter_type" : "GC Coma Inducing" }
{ "acquired_date" : "2018-09-14", "retired" : false, "scooter_type" : "FC Pro" }
{ "acquired_date" : "2018-12-02", "retired" : false, "scooter_type" : "FC Pro" }
{ "acquired_date" : "2018-08-17", "retired" : false, "scooter_type" : "FC Mk.1" }
{ "acquired_date" : "2018-01-02", "retired" : false, "scooter_type" : "FC Mk.1" }
```

## Query 4 - Scooters with Max Speed <= 35
```
> db.scooters.find({"max_speed":{"$lte":35}})

{ "_id" : ObjectId("5c0b7815005b567f0fb45c99"), "acquired_date" : "2016-09-23", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c9a"), "acquired_date" : "2017-02-20", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c9b"), "acquired_date" : "2016-11-25", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c9c"), "acquired_date" : "2015-02-02", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c9d"), "acquired_date" : "2016-08-08", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45c9e"), "acquired_date" : "2017-06-04", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45ca3"), "acquired_date" : "2017-08-18", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cad"), "acquired_date" : "2018-04-20", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cb1"), "acquired_date" : "2018-05-08", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cb2"), "acquired_date" : "2015-11-26", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cb3"), "acquired_date" : "2014-08-14", "retired" : false, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cb4"), "acquired_date" : "2016-10-14", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
{ "_id" : ObjectId("5c0b7815005b567f0fb45cb5"), "acquired_date" : "2016-07-14", "retired" : true, "scooter_type" : "GC Coma Inducing", "max_speed" : 20, "weight" : 30, "manufacturer" : "Generic Company", "website" : "genco.com" }
```

## Query 5 - All Scooters Acquired Before June 1, 2014 or After June 1, 2018
```
> db.scooters.find(
... {"$or": [{"acquired_date":{"$gte":'2018-06-01'}}, 
... {"acquired_date":{"$lte":'2014-06-01'}}]},
... {_id:0, "acquired_date":1, "scooter_type":1})

{ "acquired_date" : "2014-03-28", "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-09-17", "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2018-09-03", "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2014-03-12", "scooter_type" : "GC Generic" }
{ "acquired_date" : "2018-11-13", "scooter_type" : "SC Sonic" }
{ "acquired_date" : "2014-01-05", "scooter_type" : "SC Juggernaut" }
{ "acquired_date" : "2014-03-07", "scooter_type" : "GC Generic" }
{ "acquired_date" : "2014-03-20", "scooter_type" : "SC Juggernaut" }
{ "acquired_date" : "2018-07-17", "scooter_type" : "GC Boring" }
{ "acquired_date" : "2014-02-17", "scooter_type" : "GC Boring" }
{ "acquired_date" : "2018-07-25", "scooter_type" : "GC Boring" }
{ "acquired_date" : "2018-07-15", "scooter_type" : "GC Boring" }
{ "acquired_date" : "2014-02-10", "scooter_type" : "FC Pro" }
{ "acquired_date" : "2018-09-14", "scooter_type" : "FC Pro" }
{ "acquired_date" : "2018-12-02", "scooter_type" : "FC Pro" }
{ "acquired_date" : "2018-08-17", "scooter_type" : "FC Mk.1" }
```