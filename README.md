# Log Generator

a simple yet powerful tool for generating logs with simple rule

```
usage: logGenerator.py [-h] [-a APP_NAME] [-o LOG_PATH] [-c CONF_PATH]
                       [-d DATE] [-e END_DATE] [-i INTERNAL] [-t TOTAL]

Log Generator

optional arguments:
  -h, --help            show this help message and exit
  -a APP_NAME, --app_name APP_NAME
                        app name, default demo
  -o LOG_PATH, --log_file_path LOG_PATH
                        Write to a Log file, default ./data/xiaoshouyi.log
  -c CONF_PATH, --config_file_path CONF_PATH
                        Set conf file path, default ./conf/xiaoshouyi.json
  -d DATE, --start_date_of_log DATE
                        Set date of log, default current local time, for
                        example 2017-11-15 18:04:00
  -e END_DATE, --end_date_of_log END_DATE
                        Set end date of log, for example 2017-11-15 18:04:00
  -i INTERNAL, --internal_seconds INTERNAL
                        Set internal time of records. default internal time =
                        0 second
  -t TOTAL, --logs total number TOTAL
                        total numbers of logs, default 100

```

## 1.requirement:
```
python3.6.5 or later
```

## 2. install
```
pipenv install --python 3.6.5
```

# 3. run
```bash
# pipenv shell
# python logGenerator.py -o ./data/demo.log -c ./conf/demo.json -d "2017-11-15 18:04:00" -i 0.1 -a demo
```

# 4. UserCases
## generate logs between two timestamp (default total: 100)
```
# python logGenerator.py -d "2017-11-15 18:04:00" -e "2017-11-16 18:04:00" -a demo
```

## generate logs at beginning with certain timestamp to now
```
# python logGenerator.py -d "2017-11-15 18:04:00" -e now -a demo
```

## generate logs at beginning with certain timestamp and fixed interval (ie: 100 ms)
```
# python logGenerator.py -d "2017-11-15 18:04:00" -i 0.1 -a demo
```

## generate logs with certain end timestamp and fixed interval (ie: 100 ms)
```
# python logGenerator.py -e "2017-11-15 18:04:00" -i 0.1 -a demo
```

## generate logs with custom total logs (default 100)
```
# python logGenerator.py -d "2017-11-15 18:04:00" -e now -t 100 -a demo
```

## 5. configuration for app
you must create a json configuration for each app, each app configuation are structured as followd:
```
{
  "params": [ // a list for params to be generated
    {
      "name": "ip", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "192.168.1.1": ""
      }
    }
  ]
}
```

### 5.1 basic configuration （without weighted random）
```
{
  "params": [ // a list for params to be generated
    {
      "name": "ip", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "192.168.1.1": ""
      }
    },
    {
      "name": "user_agent", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
": ""，
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
"： ""
      }
    }
  ]
}
```

### 5.2 with weighted random
```
{
  "params": [ // a list for params to be generated
    {
      "name": "ip", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "192.168.1.1": 90, // 90 percentage
        "192.168.1.2": 10 // 10 percentage
      }
    },
    {
      "name": "user_agent", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
": ""，
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
"： ""
      }
    }
  ]
}
```

### 5.3 int param
```
{
  "params": [ // a list for params to be generated
    {
      "name": "package_num", // param name
      "type": "int", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "30": 90, // 90 percentage
        "40": 10 // 10 percentage
      }
    },
    {
      "name": "user_agent", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
": ""，
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
"： ""
      }
    }
  ]
}
```

### 5.4 float param
```
{
  "params": [ // a list for params to be generated
    {
      "name": "time_cost", // param name
      "type": "float", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "0.2": 90, // 90 percentage
        "0.5": 10 // 10 percentage
      }
    },
    {
      "name": "user_agent", // param name
      "type": "str", // param type: 'str' 'int' 'float' currently supported
      "values": { // available values for current param
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0
": ""，
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
"： ""
      }
    }
  ]
}
```