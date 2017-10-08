config = {}

def load_config(config_file='config.csv'):
   with open(config_file,'r') as f:
    for line in f:
        if line[0] != '#':
          (key,sep,val) = line.partition('=')
          # if the line does not contain '=', it is invalid and hence ignored
          if len(sep) != 0:
              val = val.strip()
              config[key.strip()] = int(val) if str.isdecimal(val) else val


if __name__ == '__main__':
        load_config()
        print(config)
 
