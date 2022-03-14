Feature: Practice Karate

Scenario: getting users from the site
Given url 'https://jsonplaceholder.typicode.com'
And path 'users'
When method GET
Then status 200
And print response
* def first = response[1]
Given path 'users', first.id
When method get
Then status 200
Then print response