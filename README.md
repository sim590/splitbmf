
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

### Youtube

One can easily use this program in combination with [`youtube-dl`][ytdl]. For e.g.

```sh
$ url='https://www.youtube.com/watch?v=SIKSc397sn4'
$ youtube-dl --extract-audio --audio-format mp3 $url
$ youtube-dl --get-description $url >desc.txt
```

The file `desc.txt`, graciously provided by the Youtube user, has to be
formatted in the manner described in Section *File description format*. Then,
one can extract audio files in the same fashion demonstrated above.

[ytdl]: http://rg3.github.io/youtube-dl/

## File description format

```
time1 Title 1
time2 Title 2
...
```

Time is specified in the well-known format `HH:MM:SS`. Everything that comes
after the time specification is part of the output file title appended before
the file type extension.

## Dependencies

* [FFmpeg](https://ffmpeg.org/)

## Author

Simon Désaulniers <sim.desaulniers@gmail.com>

<!-- vim: set sts=2 ts=2 sw=2 tw=80 et :-->

