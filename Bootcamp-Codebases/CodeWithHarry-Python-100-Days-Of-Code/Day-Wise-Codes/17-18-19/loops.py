"""
Range() Function - range(start,end,stepSize)
Returns a range object, which starts from the starting point specified & ends at 1 element before the specified ending element on stepSize intervals
Eg. range(1,10,2) will return odd numbers 1,3,5,7,9, thus 1 number '9' before the specified end
Below Options are possible due to Scaling
If start > end then range(start,end,-stepSize) i.e. negative stepSize
If start < end then range(start,end,stepSize) i.e. positive stepSize
Note: We Cannot use float values for start,end,stepSize in range() function only integers allowed

"""