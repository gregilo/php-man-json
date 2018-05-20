# php-man-json

The goal of this repo is to provide the necessary tools and scripts for downloading the PHP manual from [php.net](https://secure.php.net/download-docs.php) and converting the method documentation to JSON.

This was specifically made for an [Atom](https://atom.io) plugin.

---

## How to use

### Fetch

The fetch script aims to download the PHP manual from php.net and extract it. This is a prerequisite for converting.

Run with:
```bash
python ./fetch_manual.py
```

The documentation files will be extracted to a directory called `php-chunked-xhtml-old`.

### Convert

Assuming that you ran the fetch script above, run:

```bash
python ./convert.py
```

This will take the `name`, `synopsis`, and `usage` for every method in the docs, combine them into an object, and push them into a JSON array.

The JSON array will be written to a file called `man.json`
