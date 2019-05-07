.. image:: https://coveralls.io/repos/github/zmasek/TZMBot/badge.svg?branch=master
   :target: https://coveralls.io/github/zmasek/TZMBot?branch=master
   :alt: Coverage Status

The easiest way to use this is running with Docker::

    docker build -t tzmbot:0.0.1 .

if needed::

    docker stop tzmbot && docker rm tzmbot

and then::

    docker run --name tzmbot tzmbot:0.0.1

For skipping Docker, make sure you have pipenv installed (sudo pip install pipenv), then make do with the provided Pipfile::

    pipenv install --dev

It's enough, but here are the rest of the steps.

Because you'll be running a lot of "pipenv run" commands, it's easier to add an alias in the .bashrc in your home folder::

    function pr() {
        pipenv run "$@";
    }

With that alias you can just say pr whatever command. However, the commands in this file will be the full ones.

To fix up the code run black::

    pipenv run black TZMBot/

But it's better if you just install pre-commit hooks::

    pipenv run pre-commit install

The provided profile file has the environment variables that the bot will use so it's best if you modify it, **never commit it**,  cd into the repo folder and source the file::

    . profile

To run the bot without Docker, execute::

    pipenv run python TZMBot/app.py

To execute tests::

    pipenv run python -m tests

