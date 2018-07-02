# Notes for Myself

## Dependencies
* For building the site, I'm using [pelican](http://docs.getpelican.com/en/stable/index.html), a Python-based static blog site generator.
    * Pelican relies on [Jinja2](http://jinja.pocoo.org/docs/2.10/), a templating language for Python. It allows you to insert code into parts of your HTML page so you can use scripts to piece your page together.
* For making it more convenient (i.e. after committing, it pushes it to my website's repo), I use [ghp-import](https://github.com/davisp/ghp-import).

## How to Build

```
# you *have* to give pelican the directory of the content, or it'll break
# (it seems like by default it sets the output dir and the pelicanconf dir)
pelican content
```

NOTE: You have to delete the old HTML of your deleted blog posts manually.

## How to Push to Github Pages
```
# I added a post-commit git hook that runs ghp-import, so after committing...
git commit -am "changes ya"
# it mmediately updates the main repo
```

## Organization
* Go to `themes` to restyle the site, change the scripts, etc.
    * `themes/templates` includes all the HTML templates that will be filled.
    * `themes/static` includes the CSS/JS.
* Go to `content` to change the actual content.
* `output` is where `pelican` outputs to.

## Notes on Pelican
1. You can create arbitrary metadata for files. They *have* to follow the same format as the predefined ones.
2. The variables in Jinja2 is lower cased:

For example, if you have the metadata `CoverImage`, you have to access it as `article.coverimage`. Spaces do not work, so I use `Cover_Image` instead (which I access as `article.cover_image`)

3. By default, the articles are sorted by date (with most recent being first). I rely on that for the main page.