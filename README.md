# CoversBR
CoversBR is the first large audio database with, predominantly, Brazilian music for 
the cover song identification (CSI) or version identification (VI) and live song identification (LSI) tasks. 
This work was carried out with the participation of [CETUC/PUC-Rio](http://www.cetuc.puc-rio.br/) 
and with the support of [ECAD](https://www3.ecad.org.br/) (Central Bureau for Collection and Distribution), as it is the
holder of the audio base and is responsible for capturing the audio at the shows and
live events in Brazil.

CoversBR contains a large set of songs, with **pre-extracted features** 
and **metadata** for **102,298 songs** distributed in **26,366 groups of covers**. The 
entire collection adds up to a total of approximately 7070 hours, and the average 
song length is 240.11 seconds (4 minutes). All audio files we use to extract features 
are encoded in OGG format and their sample rate is 11 kHz. CoversBR does not contain 
any audio files due copyrights restrictions.  

For organizing the data, we use the structure of [SecondHandSongs](http://millionsongdataset.com/secondhand/) 
where each song is called a **'track'**, and each clique (cover group) is called 
a **'work'**. Based on this, the file names of the songs are their unique 
performance IDs (PID, e.g. `22`), and their labels with respect to their 
cliques are their work IDs (WID, e.g. `14`).

## Structure

### Database Metadata
The file **CoversBR_metadata.csv** contains a semicolon (;) separated table of the 
CoversBR database. **CoversBR_metadata.xlsx** is the MS Excell version of this file.
First line is the header line, with the following meaning:
* work_id           - Music or musical work ID (also called group or clique)
* Music_Name        - Music name
* track_id          - Track ID (also called execution or song)
* Artist_Name       - Artist name of the song player 
* Source            - Source of the recording 
* Genre_ECAD        - Music genre as classified by ECAD
* Recording_Version - Track recording version
* Duration          - Track duration (HH:MM:SS.SS)
* Fs                - Track sampling frquency
* [MBID](https://musicbrainz.org/doc/MusicBrainz_Identifier)             - Track MusicBrainz ID
* [ISWC](http://iswc.org/)               - International Standard Musical Work Code
* [ISRC](http://isrc.ifpi.org/)              - International Standard Recording Code

All songs have their work_id, track_id, name, artist and duration, but 
the other fields may be empty. The purpose of entering the ISRC and ISWC 
is to reliably allow anyone to retrieve complete information about a song 
or even obtain the song from a streaming service. In addition to these codes, 
MBID exists for about 50% of the songs in the database. The table below shows a  
summary of the CoversBR numbers. 

Number of songs with | Quantity
-------------------- | --------
ISRC | 88926
ISWC | 67322
MBID | 50810
Country | 92744
Year | 88926

The nationality and year of the songs were extracted from ISRC and, in cases 
where it is not available, the country was found from the name of the 
performer or the song. The groups of covers were obtained from the ECAD 
database, first using ISWC as the search key 
(since all versions of the same work have the same code), and, in their 
absence, the name of the song.

About 41% of the database is composed of Brazilian music. The table below
shows the distribution of the songs by country. There are 28 other nationalities in the
metadata file. The country codes can be found in **CountryList_ISRC.xlsx**

Country | # Songs | Country | # Songs
-----|---------|------|--------
BR |42277 |IT |431
US |28859 |AU |364
GB |10321 |JP |274
DE |4651 |CA |259
NL |1697 |ES |208
FR |1245 |DK |164
SE |710 |CH |141
AR |505 |Outras |638

CoversBR has music since 1920, as Canal Street Blues, sung by Louis Armstrong and King Oliver
in 1923 (ISRC - USFI82300027). The table below shows the distribution of the songs over the years.

Years |# Songs
-----|---------
1920 - 1929 | 44
1930 - 1939 |72
1940 - 1949 |126
1950 - 1959 |2127
1960 - 1969 |3863
1970 - 1979 |5138
1980 - 1989 |5123
1990 - 1999 |12178
2000 - 2009 |35549
2010 - 2020 |24593

The absolute frequency of the groups of covers (clicks) in
function of the number of versions per group (tracks) can be seen below. 

 Number of songs per Clique | Number of Cliques |Percentage
----------------------|----------|-----------
2 | 14607 |55.40 %
3 |2632 |9.98 %
4 |2909 |11.03 %
5 |1782 |6.76 %
6 - 10 |3132 |11.88 %
11 - 76 |1304 |4.95 %

You can see in the table that the most cover groups contain between 2 and 10 versions. 
Only in some cases there are between 11 and 76 versions per group.

The figure below shows the histogram of absolute frequency by type of musical version.
The data shown in the figure correspond to 99% of the songs in the database.
The main type is Studio, followed by live performances recorded by streaming.

<!--- [](/images/histVersion.png) --->
<p align="center">
<img src="/images/histVersion.png" width="450"/>
</p>

For design reasons, such as storage space, quality of compression /
decompression of audio and royalties, all the songs from the base were recorded in the
ogg-vorbis format with a sampling rate of 11025 Hz (99.95% of cases)
or 16 kHz (0.05% of cases). The next figure presents a pie chart describing
the source of the songs. The percentage of songs without source information is
only 0.8%. There are three sources: RADIO CAPTURE, where the songs were obtained from radio transmission over the streaming channel; IMPORT, where the songs
were provided by music labels; and CD, where the songs were copied
Compact Disks (CDs).

<!---[](/images/pieSource2.png)--->
<p align="center">
<img src="/images/pieSource2.png"  width="450"/>
</p>

Note that many of the songs from the RADIO CAPTURE source were recorded in
live presentations in noisy environments. The next histogram shows the absolute frequency of the duration of the song, whose average is 240 seconds, its
standard deviation is 109 seconds and the minimum and maximum is 18 seconds and 28 minutes,
respectively.

<!---[](/images/histDur.png)--->
<p align="center">
<img src="/images/histDur.png" width="450"/>
</p>

### Pre-extracted features

The list of features included in CoversBR can be seen below. All the features are extracted with [acoss](https://github.com/furkanyesiler/acoss/blob/master/acoss/features.py) repository that uses open-source feature extraction libraries such as [Essentia](https://essentia.upf.edu/documentation/), [LibROSA](https://librosa.github.io/librosa/), and [Madmom](https://github.com/CPJKU/madmom).

To facilitate the use of the dataset, we provide then in the following file structure.

In `CoversBR` folders, we organize the data based on their respective cliques, and one file contains all the features for that particular song. 

```python
{
	"chroma_cens": numpy.ndarray,
	"crema": numpy.ndarray,
	"hpcp": numpy.ndarray,
	"key_extractor": {
		"key": numpy.str_,
		"scale": numpy.str_,_
		"strength": numpy.float64
	},
	"madmom_features": {
		"novfn": numpy.ndarray, 
		"onsets": numpy.ndarray,
		"snovfn": numpy.ndarray,
		"tempos": numpy.ndarray
	}
	"mfcc_htk": numpy.ndarray,
	"tags": list of (numpy.str_, numpy.str_)
	"label": numpy.str_,
	"track_id": numpy.str_
}


```


## Using the dataset

### Requirements

ftp application.

* Python 3.5+
Python modules:
- argparse
- base64
- requests

### Downloading the data (feature files)
Use the ftp application to download the whole structure.

Use **CoversBR_download.py** to download all feature files from CoversBR database.

To run:
python CoversBR_download.py

OR

python CoversBR_download.py -url"<URL of shared OneDrive folder to be downloaded"

## Citing the dataset

Please cite the following [publication](http://archives.ismir.net/ismir2020/paper/???????.pdf) when using the dataset:

> Dirceu Silva, Atila Xavier, Edgard Moraes, Marco Grivet and Fernando Perdigão. CoversBR: A Large Dataset for cover song identification. In Proc. of the 21th Int. Soc. for Music Information Retrieval Conf. (ISMIR), pages ???-???, Montreal, Canada, 2020.

Bibtex version:

```
@inproceedings{silva2020,
    author = "Dirceu Silva, Atila Xavier, Edgard Moraes, Marco Grivet and Fernando Perdig{\~{a}}o",
    title = "{CoversBR}: A Large Dataset for cover song identification",
    booktitle = "Proc. of the 21th Int. Soc. for Music Information Retrieval Conf. (ISMIR)",
    year = "2020",
    pages = "???--???",
    address = "Montreal, Canada"
}
```


## License

* The code in this repository is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) 
* The metadata and the pre-extracted features are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

