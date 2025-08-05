# Right-Justify

def right_justify(msg):
    print( 'Before: ', msg )
    
    str_1 = msg
    
    for i in range(1, 11):
        # str_1 = str_1 + ( ' ' * 7 )
        print( '===' , (7 * i) )
        str_space = ' ' * (7 + i)
        # print( str_space, '-' )
        # str_1 = str.join( str_space )
        # print( i, ': ', 'After : ', ( ' ' * (7 * i) ) + str_1, len(( ' ' * (7 * i) ) + str_1) )
        print( '=asasasasasa=', len((' ' * (7 * i))) )
        str_1 = (' ' * (7 * i)) + str_1
        print( i, ': Spaces Count = ', str_1.count(' ') )
        print( i, ': ', 'After: ', str_1, ' - ', len(str_1) )
        

    print( 'After: ', str_1, ' - ', len(str_1) )
    print( 'Spaces Count = ', str_1.count(' ') )

# right_justify('monty')


def right_justify_2(msg):
    
    print( 'Before: ', msg )
        
    # print( '-----' , len(' ' * (7 * 10)) )

    msg = ' ' * 70 + msg
    
    print( 'After: ' )
    print( msg, ' - Len: ', len(msg) )
    print( 'Spaces Count 1 = ', msg.count(' ') )

    rjust_str = msg.rjust(70)

    print( 'To Check: ' )
    print( rjust_str, ' - Len: ', len(rjust_str) ) 


    msg = '\t' * 10 + msg
    
    print( 'After: ' )
    print( msg, ' - Len: ', len(msg) )
    print( 'Spaces Count 3 = ', msg.count(' ') )


right_justify_2('monty')
