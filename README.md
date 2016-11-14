# gist-dl

gist-dl is a lightweight command line tool for downloading gists from **[gist.github.com](http://gist.github.com)**. gist-dl has been tested on
python 2.7.12 and python 3.5.2.

## Install
Install the project by downloading the project as a zip file or cloning the repository. After downloading the source, run the following command to install in the root directory of the project...

```bash
pip install -e .
```

## Usage
gist-dl's functionality is currently fairly limited, but the following functionality is supported

| command line argument/option | functionality |
| :------------- | :------------- |
| `--help` | list arguments/options for tool |
| `sources` | list of github users accounts to download gists |
| `destination` | directory to download gists to |
| `--username` | github username for credentials  |
| `--password` | github password for credentials |
| `--token` | github token for credentials |
| `--config` | directory to a configuration file |
| `--extension` | file extension to download ex: ipynb |
