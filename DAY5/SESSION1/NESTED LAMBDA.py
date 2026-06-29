
multiply=lambda x:lambda y:x*y#first lamda after x is para, then inside def there is another lambda
double= multiply(2)
print(double(10))
