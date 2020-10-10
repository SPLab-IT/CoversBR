# CoversBR - A large dataset for Cover Song Identification
CoversBR is the first large audio database with, predominantly, Brazilian music for 
the Cover Song Identification (CSI) or Version Identification (VI) and Live Song Identification (LSI) tasks. 
This work was carried out with the participation of [CETUC/PUC-Rio](http://www.cetuc.puc-rio.br/) 
and with the support of [ECAD](https://www3.ecad.org.br/) (Central Bureau for Collection and Distribution) as 
holder of the audio database and responsible for capturing the audio at the shows and live events in Brazil.

CoversBR contains a large set of **pre-extracted features** and **metadata** from **102,298 songs**, 
distributed in **26,366 groups of covers**. The entire collection adds up to a total of approximately 7070 hours. 
The average song length is 240 seconds (4 minutes). CoversBR does not contain 
any audio files due copyright restrictions.  

For organizing the data, we use the structure of [SecondHandSongs](http://millionsongdataset.com/secondhand/), 
where each song is called a **'track'** and each clique (cover group) is called 
a **'work'**. Based on this, each entry song in the database has a unique 
performance ID (PID, e.g. `22`), and a clique or work ID (WID, e.g. `14`).

## Dataset Description

### Database Metadata
The file **CoversBR_metadata.csv** is a semicolon (;) separated value table of the 
CoversBR database coded in UTF-8. **CoversBR_metadata.xlsx** is the MS Excell version of this file.
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
* Country           - Country of the version
* Year              - Year of version

### Dataset Statistics

All songs have their work_id, track_id, name, artist and duration, but 
the other fields may be empty. The purpose of entering the ISRC and ISWC 
is to reliably allow anyone to retrieve complete information about a song 
or even obtain the song from a streaming service. In addition to these codes, 
MBID exists for about 50% of the songs in the database. The table below shows a  
summary of the CoversBR numbers. 


|Number of songs with | Quantity|
|:--------------------|--------:|
|ISRC | 88926|
|ISWC | 67322|
|MBID | 50810|
|Country | 92744|
|Year | 88926|


The country and year of the songs were extracted from ISRC. In cases 
where country is not available, it was attributed from the name of the 
performer of the song. The groups of covers were obtained from the ECAD 
database, first using ISWC as the search key 
(since all versions of the same work have the same code), and, in their 
absence, from the name of the song.

About 41% of the database is composed of Brazilian music. The table below
shows the distribution of the songs by country. There are 28 other nationalities in the
metadata file. The country codes can be found in **CountryList_ISRC.xlsx**


Country | # Songs | Country | # Songs
-----|---------:|------|--------:
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


Years |Number of Songs
-----|---------:
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
:----------------------:|----------:|-----------:
2 | 14607 |55.40 %
3 |2632 |9.98 %
4 |2909 |11.03 %
5 |1782 |6.76 %
6 - 10 |3132 |11.88 %
11 - 76 |1304 |4.95 %


You can see in the table that most cover groups contain between 2 and 10 versions. 
Only in some cases there are between 11 and 76 versions per group.

The figure below shows the histogram of absolute frequency by type of musical version.
The data shown in the figure correspond to 99% of the songs in the database.
The main type is Studio, followed by live performances recorded by streaming.

<!--- [](/images/histVersion.png) --->
<p align="center">
<img src="/images/histVersion.png" width="450"/>
</p>

For design reasons, such as storage space, quality of compression /
decompression of audio and royalties, all the songs of the database were recorded in the
ogg-vorbis format with a sampling rate of 11025 Hz. The next figure presents a pie chart describing
the source of the recordings. The percentage of songs without source information is
only 0.8%. There are three sources: RADIO CAPTURE, where the songs were obtained from radio transmission over the streaming channel; IMPORT, where the songs
were provided by music labels; and CD, where the songs were copied from 
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

## Dataset Structure
### Pre-extracted features

The list of features included in CoversBR can be seen below. All the features are extracted with [acoss](https://github.com/furkanyesiler/acoss/blob/master/acoss/features.py) repository that uses open-source feature extraction libraries such as [Essentia](https://essentia.upf.edu/documentation/), [LibROSA](https://librosa.github.io/librosa/), and [Madmom](https://github.com/CPJKU/madmom).

To facilitate the use of the dataset, we provide them in the following file structure.

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

### Dataset directory structure 

#### Feature file

CoversBR uses the same structure of [acoss](https://github.com/furkanyesiler/acoss/blob/master/acoss/):

```
features-h5
    /work_id
        /track_id.h5 
```   

```python
import deepdish as dd

feature = dd.load("feature_file.h5")
```

An example feature file will be in the following structure.

 ```
{
    'feature_1': [],
    'feature_2': [],
    'feature_3': {'type_1': [], 'type_2': [], ...},
    ......  
}
```

#### CSV annotation file for a dataset

The csv annotation file is differente from acoss pattern. Here there are more fields in csv with the folowing structure:

| work_id | Music_Name | track_id | Artist_Name | Source | Genre_ECAD | Recording_Version | Duration| Fs | MBID| ISWC| ISRC| Country| Year| 
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----| ---- | ----| ----| ----| ----| ----|
|1|ADMIRAVEL GADO NOVO|19629|CASSIA ELLER|CD|ND|STUDIO|00:04:35.07|11025|8311499a-4e40-4afc-a826-6725d8454851|T0391535844|BRPGD9600090|BR|96| 
|1|ADMIRAVEL GADO NOVO|23880|ZE RAMALHO|CD|ND|STUDIO|00:05:06.69|11025|1ec54f25-7525-480a-b7fa-4c79fc2ee05f|T0391535844|BRBMG9700282|BR|97|
|1|ADMIRAVEL GADO NOVO|579191|BIQUINI CAVADAO|IMPORTACAO|ND|STUDIO|00:04:21.77|11025|880622cf-96fd-4211-850f-9f914a5244c6|T0391535844|BRSME9400075|BR|94|
|  ...|...|...|...|..|..|...|...|...|...|...|...|...|...| 

```
features-h5
    /1
        /19629.h5 
        /23880.h5
        /579191.h5
        /...
```   

`acoss` methods benchmark can use the annotation csv file in the above given format.

## Using the dataset - Tutorial

### Downloading the data (feature files)

CoversBR is publicly available on AWS. Check out the AWS Registry of Open Data for details. 

The easiest way to access the data is through the [AWS Command Line Interface (CLI)](https://aws.amazon.com/pt/cli/). Follow that 
link to setup and configure the AWS CLI. The CoversBR data is stored on the coversBR S3 bucket.
Use the ftp application to download the whole structure.

To list the content of the s3 bucket associated with CoversBR, run

> aws s3 ls s3://covers-song-br --no-sign-request

There will be one folder and 1 file of metadata:

```
features-h5
CoversBR_metadata.csv
```

The features-h5 folder contains all work_id with their track_id in h5 format. 

Download data using aws s3 sync <source> <target> [--options] or 
aws s3 cp <source> <target> [--option]. For example, to download all 
data to current directory run the following:

> aws s3 sync s3://covers-song-br  .  --no-sign-request

This operation will get a long time. The dataset has about 500 GB.

if you want download only a specific work_id, run:

> aws s3 cp s3://covers-song-br/features-h5/<work_id>  .  --no-sign-request

The metadata can be downloaded using:

> aws s3 cp s3://covers-song-br/CoversBR_metadata.csv  .  --no-sign-request


### Using the feature files

The features files of CoversBR ware generated by [acoss extractor](https://github.com/furkanyesiler/acoss/blob/master/acoss/extractors.py),
so the usage is the same of it.

CoversBR has used a different PROFILE to configure the parameters of extraction, then we did a fork of the original code 
to allow some changes - [acoss-1](https://github.com/silvadirceu/acoss-1.git). 

```
git clone https://github.com/silvadirceu/acoss-1.git
git checkout develop
```

This version of acoss uses [Ray](https://docs.ray.io/en/latest/using-ray.html) for multiprocessing, because 
it allow to use the [SLURM](https://slurm.schedmd.com/overview.html) to run the code in a cluster.


## Citing the dataset

Please cite the following when using the dataset:

> Dirceu Silva, Atila Xavier, Edgard Moraes, Marco Grivet and Fernando Perdigão. 
> CoversBR: A Large Dataset for Cover Song Identification. 
> https://github.com/SPLab-IT/CoversBR

## License

* The code in this repository is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) 
* The metadata and the pre-extracted features are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

