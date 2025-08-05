try:
    # Code that can raise an Error
    div = 10/0
except:
    print( 'Division by Zero not allowed!' )
finally:
    print( 'Code finished!' )