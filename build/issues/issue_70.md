## TL;DR
Difference between statis and class method for class

### Article Link
https://julien.danjou.info/guide-python-static-class-abstract-methods/

## Key Takeaways
*  Static method and class method are useful when we don't want to instantiate the class
* Static method does not use attributes or methods of the class
* @staticmethod function is nothing more than a function defined inside a class. It is callable without instantiating the class first. It’s definition is immutable via inheritance.
* Class method uses attributes or methods of the class but does not need the class to be instantiated. 
* Classmethod is especially useful when you move your function to other class, you don't have to rename the class reference
* Static methods should not rely on such attributes which require initialization of the object itself