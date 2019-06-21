GraphQL Python Example
=======================

This project demostrates how to implement GraphQL in Python using Graphene.
For simplicity we will be using [nameko](https://github.com/nameko/nameko) as an example, but you can get rid of `service.py` and use a web framework of choice.

The project contains two models, one named `Department` and another
named `Employee`.

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning
this repository:

```bash
# Get the example project code
git clone https://github.com/nairobi-graphql-meetup/graphql-python-example.git
cd graphql-python-example
```

It is good idea (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to keep things simple,
but you may also find something like
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
to be useful:

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install our dependencies:

```bash
pip install -r requirements.txt
```

Now the following command will setup the database, and start the server:

```bash
./run.sh

```

Now head on over to postman and send POST request to:
[http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql)
and run some queries!

Adapted from: https://github.com/graphql-python/graphene-sqlalchemy/tree/master/examples/nameko_sqlalchemy
