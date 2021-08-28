# 🚧 Practice: Area Codes

{download}`Download starter code </module-2-data-structures-and-files/lesson-5-data-structures-tuple-set-dict/practice-area-codes.zip>`

Write a function called `area_codes` that takes a `list` of `str` as input where each `str` in the list is a phone number and returns the number of unique area codes found in those phone numbers. Each phone number will be of the format `'123-456-7890'` and the area code is the first three characters in the `str` .  

For example, if we were to call  

```text
area_codes([
    '123-456-7890',
    '206-123-45676',
    '123-000-0000',
    '425-999-9999'
])
````

This call would return 3 because there are 3 unique area-codes in these phone numbers ( `123` , `206` , `425` ).  

You may assume that each `str` in the list is a valid phone number. However, you should not assume anything about the number of elements in the `list` .  

*Hint: Try solving an easier version of this problem that just prints all the area codes for the provided phone numbers.*   

##  Requirements  

-  Your solution should use a structure that can solve this problem efficiently, even if there are a large number of phone numbers  


