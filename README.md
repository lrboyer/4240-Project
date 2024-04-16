![](assets/banner.png)

### Introduction
This program does stuff


### Requirements
- python 3.11+


### Installation
```shell
pip install -r requirements.txt
```


### Usage
```shell
python <program_name> [-v] [-q QUARANTINE] [-h] {scan,watch,lock,unlock} <filepath>
```
Example:
```shell
python <program_name> -v scan . 
```

- positional arguments:
  - {`scan`,`watch`,`lock`,`unlock`}
                        (Literal['scan', 'watch', 'lock', 'unlock'], required)
 - `filepath`              (str, required) path to file

- actions explained:
  - `scan`: scans the inputted path and all files within
  - `watch`: actively observes the inputted path for any file changes and will automatically quarantine any malicious files
  - `lock`: locks the inputted file using encryption (making the file inert)
  - `unlock`: unlocks the inputted file
    

- options:
  - `-v`, `--verbose`         (bool, default=False) print more detail
  - `-q QUARANTINE`, `--quarantine QUARANTINE`
                        (str, default=.) directory to move quarantined files
  - `-h`, `--help`            show this help message and exit
