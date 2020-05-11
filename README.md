# CoversBR
Tools to access and download the CoversBR Dataset.

## Downloading feature files
Use **CoversBR_download.py** to download all feature files from CoversBR database.
Script witten for Python 3.5.x
Uses python modules:
- argparse
- base64
- requests

To run:
python CoversBR_download.py

OR

python CoversBR_download.py -url"<URL of shared OneDrive folder to be downloaded"

## Database Metadata
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

## License
* The code in this repository is licensed under Apache 2.0
* The metadata and the pre-extracted features are licensed under CC BY-NC-SA 4.0

