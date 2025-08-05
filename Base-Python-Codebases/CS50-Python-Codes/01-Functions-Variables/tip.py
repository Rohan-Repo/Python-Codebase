"""
In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
typically an amount equal to 15% or more of your meal’s cost. 

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), 
remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
"""

def dollars_to_float(amt):
    amt = amt.replace('$', '')
    return float( amt )

def percent_to_float(perc):
    perc = perc.replace('%','')
    return float(perc)/100

def main():
    dollar_amt = dollars_to_float( input('Enter Bill Amount:') )
    tip_perc = percent_to_float( input('Enter Tip Percentage:') )

    tip = dollar_amt * tip_perc

    print( 'Bill Amount = $', dollar_amt )
    print( F'Leave ${tip:.2f}' )


if __name__ == "__main__":
    main()