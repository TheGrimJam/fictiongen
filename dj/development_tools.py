
import time
import linecache
import sys
import os
# Tools for development and logging purposes.
# I.e custom built profilers and loggers (although third party loggers are probably idea.)

MARKOV_LOGGING = False # Hook this up to logging function 

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)



def g_log_exception(err, filename="general_log.txt", exception=False):
  if MARKOV_LOGGING:
    errorFile = open(os.path.join(os.path.dirname(__file__), 'errors', filename), "a")
    startTime = time.time()
    startTime = datetime.datetime.fromtimestamp(startTime) # check 
    errorFile.write("Time: " + str(startTime) + "  ")
    errorFile.write(str(err))
    if exception:
      errorFile.write("\n" + PrintException())
    errorFile.write("\n")
    errorFile.close()