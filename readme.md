# Folder Portals

## What is this thing?

`folder-portals` is a tiny utility that gives you four simple commands:

- `save someKey` creates a "portal" to the current working directory saved under `someKey`
- `goto someKey` retrieves the portal `someKey` and navigates there
- `portals` prints a list of your portals and their associated directories
- `rmportal someKey` deletes the portal associated with `someKey`

## Ok, I want it. How do I install it?

1. If you don't have python3, install python3. (Not sure? `python3 --version`.)

2. **Check out folder-portals where you want it installed.** I like ~/.portals, but it's up to you.
	
	```bash
	git clone https://github.com/benjisidi/folder-portals $HOME/.portals
	```
	
3. **Define the environment variable PORTALS_ROOT** to wherever you cloned the repo to, and source the `commands.sh` file.

	- For **bash:**
        ```bash
        echo 'export PORTALS_ROOT="$HOME/.portals"' >> ~/.bash_profile
        echo '. $PORTALS_ROOT/commands.sh' >> ~/.bash_profile
        ```
   - For **Ubuntu:**
        ```bash
        echo 'export PORTALS_ROOT="$HOME/.portals"' >> ~/.bashrc
        echo '. $PORTALS_ROOT/commands.sh' >> ~/.bashrc
        ```
    - For **Zsh:**
        ```bash
        echo 'export PORTALS_ROOT="$HOME/.portals"' >> ~/.zshrc
        echo '. $PORTALS_ROOT/commands.sh' >> ~/.zshrc
        ```
All going well, you should now be able to restart your shell with `$SHELL`, and running `portals` should print an empty map `{}`

## Why's it a weird mishmash of python and shell script?

- I hacked it together one afternoon because I use WSL2 on windows and having to navigate between Windows and Linux directories all the time was a pain. 

- I then equally hackily modified it for general use.

- Don't judge.



- ...stay tuned for a more sensible version.

