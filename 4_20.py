#今天从第十题开始写SQL
#找某列中一类的最小或最大时，使用>=all(select...)，找某列中这一类以外的比这一类小或大时，可以大于max或min，也可以大于或小于all
#where在聚合前使用，having在聚合后

#（1）Some countries have populations more than three times that of any of their neighbours (in the same continent).
# Give the countries and continents.

# select name, continent from world x
# where population >= all(select 3*population from world y where y.continent = x.continent and y.name <> x.name)

# （2）Find the continents where all countries have a population <= 25000000.
# Then find the names of the countries associated with these continents. Show name, continent and population.

# select name, continent,population from world x
# where 25000000 >= all(select population from world y where y.continent = x.continent )

# （3）List each continent and the name of the country that comes first alphabetically.

# SELECT continent, name FROM world x
#   WHERE name =
#     (SELECT name FROM world y
#         WHERE y.continent=x.continent
#           order by name limit 1)

# (4)Find the largest country (by area) in each continent, show the continent, the name and the area:
#又可以叫做correlated/synchronized sub-query

# SELECT continent, name, area FROM world x
#   WHERE area >= ALL
#     (SELECT area FROM world y
#         WHERE y.continent=x.continent
#           AND area > 0)

#