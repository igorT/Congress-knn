from __future__ import division
from heapq import *
def distance( a, b ):
    dist = 0
    for i in range( 1, len( a ) ):
        if( a[ i ] != b[ i ] ):
            dist+=1
    return dist

def decide( a, k ):
    global neig
    prio = []
    for n in neig:
        heappush( prio, ( distance( a, n ), n ) )

    nns = nsmallest( k, prio )
    count = 0
    for n in nns:

        if ( n[1][ 0 ] == "democrat" ):
            count+=1
        else:
            count-=1
    if ( count > 0 ):
        return "democrat"
    else:
        return "republican"

f = open('house-votes-84.data')
lines = f.readlines()
f.close()
values = []

for l in lines:
    line = l.rstrip('\n').split( ',' )
    values.append( line )

def classify( k, toInit ):
    global neig
    neig = values[:toInit]
    correct = 0

    for v in values[ toInit: ]:
        res = decide( v, k )
        if ( res == v[ 0 ] ):
            correct+=1
        toApp = [ res ] + v[1:]
        neig.append( toApp )

    return correct

for x in range( 1, 33, 2 ):
    for i in range( 1, 33, 2 ):
        if ( x >= i ):
            r = classify( i, x )
            print str( x ) + "-" + str(i) + ":" + str( r ) + " " + str( r/(435 - x) * 100 )[:2] + "%"
