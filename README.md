# DELTARUNE Chapter 1 Japanese -> English Anki deck

this is the source code for an anki deck i made, including the code i used to generate all the notes from the dialogue files. you can download the deck [link go here!!].

## limitations

- the lines of dialogue aren't exactly in the order they appear in-game. it might be a good idea just to randomize the card order anyways
- this is only chapter 1 dialogue--see the "things to do" section at the end of the page for an explanation of why this is the case
- there's no data on which character each line is from, although this is not stored in the data files so i can't really have this happen

## credits

font (en): [Determination Mono](https://www.behance.net/gallery/31268855/Determination-Better-Undertale-Font)
font (jp): JF Dot Shinonome Gothic 14

## technical details

### building from scratch

if you want to make changes to this deck, you can make the deck from scratch as follows. however, i would recommend importing the shared deck and then doing the final 2 steps instead, to save effort.

1. create a note type "deltarune" as specified [here](deck/notetype.txt).
2. the note type should have one card, with [this front template](deck/templates/1-front.html) and [this back template](deck/templates/1-back.html). the styling should be from [here](deck/templates/styling.css).
3. add all the files in the `deck/media` folder into your anki media folder.
4. create a deck.
5. use the `build` script to first build `src/lines.json` (a dump of every line in the game) and then `deck/data.txt` (the notes for the deck).
6. import `deck/data.txt` into the deck you created with these settings:
    - Field separator: Tab
    - Allow HTML in fields: on
    - Import options:
        - Notetype: deltarune
        - Deck: [whatever the deck you made is]
        - Existing notes: Update
        - you can leave the other options alone here
    - Field mapping:
        - id: `1: DEVICE_CONTACT_slash_Step_0_gml_6_0` or similar
        - jp: `2: 聞コエマスカ？` or similar
        - en: `3: ARE YOU THERE?` or similar
        - sort_id: `4: 0` or similar
        - Tags: (Nothing)

if you are updating the data, go through steps 5 and 6 only. in step 6, set the "Tag all notes" option to a new tag. after you import the file, do the following:

7. search for notes in the deck without the tag you created--you can click on the deck in browse and then ctrl-alt-click (or something--i use macos where it's cmd-opt-click) on the tag, or you can search `deck:[deckname] -tag:[tagname]`.
8. select all of these and delete them. make sure you selected everything right beforehand, of course.
9. delete the tag.

### changing patterns and such

the `src/ankify.py` script takes the `src/lines.json` file with every line in the game in both languages and converts it into an anki deck. during this, each line is processed in two main ways:

- we remove all of the special characters used in the dialogue for e.g. pausing, and replace special characters such as newlines and color setting with HTML equivalents.
- we filter empty lines, lines which are not translated from english, and repeats.
- we remove lines whose keys match specific patterns.

the first one of these is done via the `src/special.txt` file, which consists of lines in the form `regex` or `regex|repl`. in the first case, every match of `regex` is removed, and in the second, every match of `regex` is replaced with `repl`.

the third one would be done via the `src/exclude.txt` file, but there isn't anything there at the moment. the file would consist of regexes, each on a separate line; any line of dialogue whose key (`DEVICE_CONTACT_slash_Step_0_gml_6_0` etc.) matches one of the regexes will be filtered out and not added into the deck. this is so we can filter out lines that aren't very important but don't fit any of the criteria listed in the second bullet point above. i'm too lazy to manually go through all 5000+ lines and figure out which ones are garbage but if you run into any useless lines while using the deck please leave a bug report.

### things to do

- putting dialogue from chapter 2 into `src/lines.json`. this wouldn't be too hard for japanese--there's a file `lang_ja.json` that has all the chapter 2 dialogue--but in english all of the dialogue is embedded into the code because toby fox is lazy. someone has already extracted the dialogue in the form of the [deltarune dialogue dump website](https://hushbugger.github.io/drdia/#) and [github repo](https://github.com/HushBugger/hushbugger.github.io) and i could steal the data from there, but it doesn't seem to include the keys. i could also try and get a dump of the game and do some Magical Text Processing but that sounds pretty difficult. but also i'm guessing chapter 2 has some interesting dialogue that might be useful.
- filtering out useless lines. this seems trivial but it's also probably a real pain. i'll probably do this while using the deck, or something.