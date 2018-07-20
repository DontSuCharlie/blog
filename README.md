# Notes for Myself

## Dependencies
1. [Pelican](http://docs.getpelican.com/en/stable/index.html), a Python-based static blog site generator.
    a. Pelican relies on [Jinja2](http://jinja.pocoo.org/docs/2.10/), a templating language for Python. It allows you to insert code into parts of your HTML page so you can call scripts to piece your page together.
2. [Virtualenv](https://virtualenv.pypa.io/en/stable/) sandboxes Python dependencies (`pip` installs packages globally, meaning you can't have multiple versions of the same library. If you have an old project that uses library v1 and you're starting a project that uses library v8, calling `pip` might break your old project).
2. [ghp-import](https://github.com/davisp/ghp-import). After committing in this repository, it pushes to my Github static site repository.

## Setting up for the first time on a \*NIX machine
Just refer to the [documentation](http://docs.getpelican.com/en/stable/install.html).

## Setting up for the first time on Windows 10
1. Install Python 3.3 or higher.
2. Run `pip install virtualenv` to install `virtualenv` so you can sandbox your libraries.
3. Do **not** immediately run `virtualenv ~/virtualenvs/pelican`. You have to change your directory to where you want the virtual environments to live in.

If I run `virtualenv ~/virtualenvs/pelican` in `C:/Users/Charlie/Documents`, it would **actually create the fucking folder `C:/Users/Charlie/Documents/~/virtualenvs/pelican`** instead of doing `C:/Users/Charlie/virtualenvs/pelican`.

4. Run `virtualenv {your virtualenvs directory}/{name of your sandbox}` to create the new sandbox. For example, my virtualenvs directory on Oreo is `C:/python-virtualenvs` and I wany my sandbox to be called `pelican`, so I would run `virtualenv C:/python-virtualenvs/pelican`.
5. Do **not** run `source /virtualenvs/pelican/bin/activate` to set the current terminal session to the sandbox. First, Windows doesn't recognize the `source` command. **Second, the script is not in /bin. It's in /Scripts. Just run `{your virtualenvs directory}/{name of your sandbox}/Scripts/activate` instead.**
6. `pip install pelican` to install pelican to the current sandbox.
7. `pip install Markdown` to install Markdown support for pelican.
8. `pip install ghp-import` to install `ghp-import`.

## Setting up on Oreo
1. Run `C:/python-virtualenvs/pelican/Scripts/activate` to set the current session to this blog's sandbox.
2. Do your shit.

## Where to edit stuff (the folder structure)
* Go to `themes` to restyle the site, change the scripts, etc.
    * `themes/{theme}/templates` includes all the HTML templates that will be filled.
    * `themes/{theme}/static` includes the CSS/JS.
    * Right now my theme is `notmyidea`.
* Go to `content` to change the actual content. Just create a Markdown file. Look at existing Markdown files to see the required metadata.
* `output` is where `pelican` outputs to.

## Running Pelican to generate the site from Markdown
```
# You *must* give pelican the directory of the CONTENT FOLDER, not the directory of the project, or it will fucking break
# For example, running `pelican` in your root directory fails, but running
pelican content
# works
# (it seems like by default it sets the output dir and the pelicanconf dir)
```

## How to Push to Github Pages
```
# I added a post-commit git hook that runs ghp-import, so after committing...
git commit -am "changes ya"
# it mmediately updates the main repo
```


## Notes on Pelican
1. If you want to delete a blog post, you **have to delete the old HTML in the `output` folder**.
2. You can create arbitrary metadata for files. They *have* to follow the same format as the predefined ones.
3. The variables in Jinja2 are lower cased:

For example, if you have the metadata `CoverImage`, you have to access it as `article.coverimage`. Spaces do not work, so I use `Cover_Image` instead (which I access as `article.cover_image`)

4. By default, the articles are sorted by date (with most recent being first). I rely on that for the main page.