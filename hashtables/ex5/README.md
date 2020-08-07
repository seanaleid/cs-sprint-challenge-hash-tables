# File Finder

Given a list of full paths to files, and a list of filenames to query,
report all the full paths that match that filename.

Example input:

```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]

queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```

Example return value:

```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
```

because that's where the `foo.txt` and `ls` files are. 

The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.

Return list can be in any order.

Limits:

* Up to approximately 1,000,000 paths.
* Up to approximately 1,000,000 queries.

* U --> Want a list of full file names that match the query file.
* P --> 
    # initialize result list
    # initialize dict
    # 1. Add all filenames as keys and values in a dict
    # 2. Loop through file name values and see if the query is in the dict
        # Yes, append to result list
    # 3. Return result list
* E -->
* R -->