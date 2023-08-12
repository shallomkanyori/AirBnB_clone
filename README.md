## AirBnB clone - The console

### Description
Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

Each task is linked and will help you to:
- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### The console
#### How to start it
You can use the console works in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

You can also use the console in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Usage instructions
The console operates on the following classes:
- `BaseModel`
- `User`
- `State`
- `City`
- `Amenity`
- `Place`
- `Review`

The console provides the following commands to manage instances of the previous classes. Dot notation is supported for the `all`, `show`, `update`, `count` and `destory` commands:
- `create`: Creates a new instance of a class, saves it and prints the `id`.
	- Usage: `create <class name>`
	- Example:
	```
	(hbnb) create User
	49faff9a-6318-451f-87b6-910505c55907
	(hbnb) 
	```

- `show`: Prints the string representation of an instance.
	- Usage: `show <class name> <id>` or `<class name>.show(<id>)`
	- Example:
	```
	(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
	[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) 
	```
	- Note: The command shown is equivalent to `User.show(49faff9a-6318-451f-87b6-910505c55907)`

- `all`: Prints a list of all string representation of all instances based or not on the class name.
	- Usage: `all [<class name>]` or `<class name>.all()` (square brackets indicate optional arguments)
	- Example:
	```
	(hbnb) all
	[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293)    , 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) all User
	[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293)    , 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) all BaseModel
	[]
	(hbnb) 
	```
	- The previous commands commands can be written in dot notation as: `User.all()` and `BaseModel.all()`
	- Note: The dot notation of the `all` command requires the `<class name>`

- `destroy`: Deletes an instance (saving the change into `file.json`).
	- Usage: `destroy <class name> <id>` or `<class name>.destroy(<id>)`
	- Example:
	```
	(hbnb) all
	[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293)    , 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
	(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
	(hbnb) all
	[]
	(hbnb) 
	```

- `update`: Updates an instance by adding or updating an attribute (saving the change into `file.json`)
	- The `update` command can be used in three ways:
		- `update <class name> <id> <attribute name> "<attribute value>"`
		- `<class name>.update(<id>, <attribute name>, <attribute value>)`
		- `<class name>.update(<id>, {<attribute name> <attribute value>[, ...]})`
	- Example:
	```
	(hbnb) create User
	2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4
	(hbnb) show User 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4
	[User] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'first_name': 'Betty', 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 11, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 11, 2, 3, 11, 3, 49401)}
	(hbnb) update User 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4 first_name "John"
	(hbnb) User.update(2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4, last_name, "Smith")
	(hbnb) User.update(2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4, {"age": 89, 'email': "john@mail.com"})
	(hbnb) 
	(hbnb) show User 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4
	[User] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 11, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 11, 2, 3, 11, 3, 49401), 'first_name': 'John', 'last_name': 'Smith', 'age': 89}
	(hbnb) 
	```

- `count`: Displays the number of instances of a class.
	- Usage: `<class name>.count()`
	- Example:
	```
	(hbnb) User.all()
	[User] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 11, 2, 3, 10, 25, 903293)    , 'updated_at': datetime.datetime(2017, 11, 2, 3, 11, 3, 49401), 'first_name': 'John', 'last_name': 'Smith', 'age': 89}
	(hbnb) User.count()
	1
	(hbnb) create User
	(hbhb) User.count()
	2
	(hbnb) 
	```

#### Errors
All commands operate under the following assumptions:
- All arguments are provided for the given command
- Arguments are always in the right order
- Arguments are separated by a space
- String arguments containing a space are between double quotes

As such, you may encounter the following errors:
- `** class name missing **` - You have not provided a `<class name>` argument
- `** class doesn't exist **` - The `<class name>` provided does not exist
- `** instance id missing **` - You have not provided an `<id>` argument
- `** no instance found **` - No instance exists for the `<id>` provided
- `** attribute name missing **` - You have not provide an `<attribute name>` argument
- `** value missing **` - You have not provided an `<attribute value>` argument
- `****` - The console does not recognize the given command

Note: Error management starts from the first argument to the last one
