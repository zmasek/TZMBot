BROKEN, DO NOT USE YET

Make sure you have pipenv installed (sudo pip install pipenv), then create the environment:
pipenv --three
It's enough, but here are the rest of the steps.
pipenv install git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
pipenv install black --dev

Because you'll be running a lot of "pipenv run" commands, it's easier to add an alias in the .bashrc
function pr() {
    pipenv run "$@";
}
so you can just say pr whatever command. However, the following commands are full ones

To fix up the code run black
pipenv run black TZMBot/
To run the bot without the docker, cd into TZMBot and execute:
pipenv run python run.py

Dockerfile is added so it's enough to build it with:
docker build -t tzmbot:0.0.1 .
if needed:
docker stop tzmbot && docker rm tzmbot
and then:
docker run --name tzmbot tzmbot:0.0.1

# rewrite on_command_error so it avoids the dict
# add bugsnag
