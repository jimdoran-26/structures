#e-commerce site with 5 products, has delivery orders
#[delivery_details=[1,4,6,10,12]
#if max number of trips is 10, what is min number of items he should carry evry single time to finish delivery in 10 trips
#if max num products is 12, he will finish in 5
#if min is 1 he will finish in more than10

delivery_details=[1,4,6,10,12]
allowed_trips=10



def Solution(delivery):
    min_d=min(delivery)
    max_d=max(delivery)

    for number in range(min_d,max_d+1):
        trips =0
        for item in delivery:
            if item % number ==0:
                trips += item // number
            else:
                trips += (item//number)+1
        #print('number of trips for %d items is %d'%(number,trips))
        if trips<= allowed_trips:
            print('min number of items required for delivery is %d' %(number))
            break

(Solution(delivery_details))
"""
1-1
4-2
6-3
6-4
10-5
10-6
10-7
12-8
12-9
12-10
"""