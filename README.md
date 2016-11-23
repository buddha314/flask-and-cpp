# flask-and-cpp
Learning how to build a Flask app with tests and C++ extensions.  Pain expected.

Using the `src` directory to hold the C++ files and tests.

## Use VirtualEnv

First time, don't forget to to

```
python virtualenv.py env
```

and use `pip install -r requirements.txt` before you run anything.

## Running the extension (basic)

Go into `app/src/build` (create it if you don't have it) and run
```
cmake ..
make
```

Now, in the same build directory you should be able to do 
```
python
import clegs_ext
>>> clegs_ext.get_captain_name()
'Jack Sparrow'
```

Or from the app dir, you should be able to do 

```
python
>>> from src.build import clegs_ext
>>> clegs_ext.get_captain_name()
'Jack Sparrow'
```

Now, see if we can do this from the Flask app.

