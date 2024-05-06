from functools import wraps
from collections import Counter
import re
#import tabulate(Модуль tabulate не прауцює, тому не вийшло зробити табличку яяк вказано в завданні)
import sys
import getopt
def parse_log_line(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        result = func(*args, **kwds)
        cleaned_logs = []
        for line in result:
            log_pattern=r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)'
            # cleaned_logs = []
            match = re.match(log_pattern, line)
            if match:
                date = match.group(1)
                time = match.group(2)
                level = match.group(3)
                message=match.group(4)
                cleaned_logs.append({'date': date, 'time': time, 'level':level,'message': message})
        return cleaned_logs                                                                 
    return wrapper

@parse_log_line
def load_logs(file_path: str) ->list: 
    with open('logs.txt', 'r', encoding='utf-8') as file_path:
       lines = [line.strip() for line in file_path.readlines()]
    return lines


#print(load_logs('Exercise_3\\logs.txt'))

def   filter_logs_by_level(file_path: str, level: str) -> list:
    logs = load_logs('logs.txt')
    result=[]
    for log in logs:
      if log['level']==level:
       result.append(log)
    return result



#print(filter_logs_by_level('Exercise_3\\logs.txt','INFO'))


def display_log_counts(counts:dict):
    logs=load_logs('logs.txt')
    log_levels = []
    for log in logs:
      log_levels.append(log['level'])

    log_level_counts = Counter(log_levels)
    return log_level_counts


#print(display_log_counts(load_logs('Exercise_3\\logs.txt')))


def main(argv):
 try:
        opts, _ = getopt.getopt(argv, [], ['log=', 'file='])
 except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
 log_level = None
 file_path = None
 for opt, arg in opts:
  if opt == '--log':
    log_level = arg
  elif opt == '--file':
    file_path = arg

 if not file_path:
        print("Please provide a file path.")
        sys.exit(2)

 logs = load_logs(file_path)
 if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        log_counts = display_log_counts(logs)        
        print("Log Counts:")
        print(log_counts)
        print("Filtered Logs:")
        for log in filtered_logs:
            print(log)
        
 else:
        log_counts = display_log_counts(logs)
        print("Log Counts:")
        print(log_counts)
    
    
     

if __name__ == "__main__":
   main(sys.argv[1:])


#python main.py --file logs.txt --log error
# Calling decorated function
# Calling decorated function
# Calling decorated function
# Log Counts:
# Counter({'INFO': 4, 'DEBUG': 3, 'ERROR': 2, 'WARNING': 1})
# Filtered Logs:
# {'date': '2024-01-22', 'time': '09:00:45', 'level': 'ERROR', 'message': 'Database connection failed.'}
# {'date': '2024-01-22', 'time': '11:30:15', 'level': 'ERROR', 'message': 'Backup process failed.'}

# python main.py --file logs.txt
# Calling decorated function
# Calling decorated function
# Log Counts:
# Counter({'INFO': 4, 'DEBUG': 3, 'ERROR': 2, 'WARNING': 1})
















































# arguments=["date","time","level","message"]
# result={}
#  for line in lines:
#   dictionary = dict(zip(arguments, line))
#  result.append(dictionary)
#  return result

#"[INFO] 2023-05-25 10:15:35: User 'John' logged in."
#log_pattern = r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)'





# print(load_logs('Exercise_3\\logs.txt'))




# def   filter_logs_by_level(load_logs('Exercise_3\\logs.txt'), level: str) -> list:
#    call_3=load_logs('Exercise_3\\logs.txt')
#    result=Counter(call_3)
#    return result

# def   count_logs_by_level(logs: list) -> dict:
   
#    pass

# def   display_log_counts(counts: dict):
   
#    pass



# print(filter_logs_by_level('Exercise_3\\logs.txt','ERROR'))







# ex=parse_log_line(load_logs('Exercise_3\\logs.txt'))




# print(ex)

# ex="2024-01-22 12:00:00 INFO User logged out."

# print(parse_log_line(ex))