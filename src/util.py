
DEBUG_PRINT = True

def debug_print( *args ):
  if DEBUG_PRINT:
    print( " ".join( map( str, args ) ) )
