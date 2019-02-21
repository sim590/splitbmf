
# splitbmf

Split a Big MP3 (or any media) File in separate tracks.

## How to use

Let the file `bmf.mp3` and a file description (see next section for
specification) in some file `desc.txt`. One splits the file with:

```sh
$ splitbmf -i bmf.mp3 < desc.txt
```

The resulting files are output in the current directory in the same file type as
the input file (`mp3`). Therefore, `ffmpeg`'s `-codec copy` is used. If one uses
option `-t` like so:

```sh
$ splitbmf -t ogg -i bmf.mp3 < desc.txt
```

then, resulting files will be of file type `ogg` and `-codec copy` can't be
used. Transcoding takes place, therefore taking more time.

## File description format

The file has to

```
time1 Title 1
time2 Title 2
...
```

Time is specified in the well-known format `HH:MM:SS`. Everything that comes
after the time specification is part of the output file title appended before
the file type extension.

## Author

Simon Désaulniers <sim.desaulniers@gmail.com>

<!-- vim: set sts=2 ts=2 sw=2 tw=80 et :-->

