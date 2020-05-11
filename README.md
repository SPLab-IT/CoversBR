# CoversBR
CoversBR: a large dataset for cover song identification and understanding. It contains a large set of songs, with **pre-extracted features** and **metadata** for **102,000 songs**. All audio files we use to extract features are encoded in OGG format and their sample rate is 11 kHz. CoversBR does not contain any audio files. For **the results** of **our analyses on modifiable musical characteristics** using the cover analysis subset and **our initial benchmarking of 7 state-of-the-art cover song identification algorithms** on the benchmark subset, you can look at our [publication](http://archives.ismir.net/ismir2020/paper/?????.pdf).

For organizing the data, we use the structure of SecondHandSongs where each song is called a **'performance'**, and each clique (cover group) is called a **'work'**. Based on this, the file names of the songs are their unique performance IDs (PID, e.g. `P_22`), and their labels with respect to their cliques are their work IDs (WID, e.g. `W_14`).

Many songs have their ISRC or ISWC codes.

In addition, we matched the original metadata with MusicBrainz to obtain MusicBrainz ID (MBID). Song length where taken from the song recording and genre/style tags where provided by ECAD. We would like to note that MusicBrainz related information is not available for all the songs in CoversBR, and since we used just our metadata for matching, we include the first precise **'performance'** + **'author'** matching MBIDs for a particular songs.

We also provide tools to access and download the CoversBR Dataset.



## Structure

### Database Metadata
File **CoversBR_metadata.csv** contains a semicolon (;) separated table of the CoversBR database. **CoversBR_metadata.xlsx** is the MS Excell version of this file.
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
* MBID              - Track MusicBrainz ID
* ISWC              - International Standard Musical Work Code
* ISRC              - International Standard Recording Code

### Pre-extracted features

The list of features included in CoversBR can be seen below. All the features are extracted with [acoss](https://github.com/furkanyesiler/acoss/blob/master/acoss/features.py) repository that uses open-source feature extraction libraries such as [Essentia](https://essentia.upf.edu/documentation/), [LibROSA](https://librosa.github.io/librosa/), and [Madmom](https://github.com/CPJKU/madmom).

To facilitate the use of the dataset, we provide two options regarding the file structure.

1- In `da-tacos_benchmark_subset_single_files` and `da-tacos_coveranalysis_subset_single_files` folders, we organize the data based on their respective cliques, and one file contains all the features for that particular song. 

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

2- In `da-tacos_benchmark_subset_FEATURE` and `da-tacos_coveranalysis_subset_FEATURE` folders, the data is organized based on their cliques as well, but each of these folders contain only one feature per song. For instance, if you want to test your system that uses HPCP features, you can download `da-tacos_benchmark_subset_hpcp` to access the pre-computed HPCP features. An example for the contents in those files can be seen below:

```python
{
	"hpcp": numpy.ndarray,
	"label": numpy.str_,
	"track_id": numpy.str_
}

```
## Using the dataset

### Requirements

* Python 3.5+
Python modules:
- argparse
- base64
- requests

### Downloading the data (feature files)
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
* The code in this repository is licensed under Apache 2.0
* The metadata and the pre-extracted features are licensed under CC BY-NC-SA 4.0

