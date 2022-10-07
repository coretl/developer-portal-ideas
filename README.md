# developer-portal-ideas
Ideas on how the software developer guidelines and catalogue of repos might look.

Visit https://coretl.github.io/developer-portal-ideas to see built docs.

## Building locally

First you need python3.9. If at Diamond you can do this to get it:

```shell
$ module load python/3.9
```

To build the docs locally run:

```shell
$ ./autobuild.sh
```

This will make a venv and locally host the docs, auto-rebuilding and refreshing
when you make changes to the source. Point your browser at
<http://localhost:8000> to see the docs.

