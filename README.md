lilian
======

Lilian is my web framework, wanna fight about it?

How To Use It
======

You really can't, yet, unless you want to do some muching around.  This is my personal framework that I use for my own projects.

If for some reason you do:

import lilian.py

include lilian.js

Here are some useful functions for you (within lilian.js):

login()
logout()
whoami()

There are some others in there as well, but those are mostly for dealing with a specific use case of this.

lilian.py is where the work happens.

About the token system
=====

You don't have to use it.  If you pass token "banana", it will always return True.  This is for debugging, and you should turn it off.  To turn it off, comment out the lines that say: 
if token == "banana": 
	valid = True

After that, you will have to create a token for each user action.  This is to prevent Cross Site Request Forgery.  You should care about this, it's important.

To generate a token, call:

generate_token(user,action)

Where user is the username of the person for whom the token shoul validate.  Action is the action that they are allowed to perform with the token.  This "action" must match what is then used during validate_token(token,user,action).

About the authentication system
=====

It uses bcrypt.  You should use bcrypt because bcrypt is good.

You can read about it here: http://en.wikipedia.org/wiki/Bcrypt

If you choose not to read about it, you should know the following: bcrypt is an intentionally-slow cryptographic function.  It uses salts automatically, which is to prevent rainbow tabling, and uses its speed (or lack thereof) to prevent brute-force attacks.

I might be wrong about that, though!  I am not a cryptographer, but this is what I have read seems to explain.  If I'm wrong, bull request me, dawg.

