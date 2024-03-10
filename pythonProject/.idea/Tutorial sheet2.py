#QUESTION 1
x = 9
y = 5
average = (x+y)/2
print(average)
if x>y:
    print(x, 'is the largest value')
else:
    print(y, 'is the largest value')
#QUESTION 2
x = 17
if 1<=x<=100:
    print('correct')
else:
    print('incorrect')
r = x%5
r==0
if r==0:
    print(x,'is divisible by 5')
else:
    print(x,'is not divisible by 5')


#QUESTION 3 Figure 1
def determining_a_leap_year(y):
    year = y
    Leap_year = y%4
    if Leap_year != 0:
        return y, 'is not a leap year'
    else:
        return y,'is a leap year'
print(determining_a_leap_year(2004))
print(determining_a_leap_year(1997))
print(determining_a_leap_year(2008))


#QUESTION 3 Figure 2
#Age = a
a = 17
if a<16:
    print('you are less than 16 and will be charged £7')
elif 16<=a<65:
    print('you are more than 16yrs but less than 65yrs and will be charged £10')
else:
    print('you are more than 65yrs and will be charged £5')


#QUESTION 4
room_rate = 175
num_nights = 5
cost_of_services = 200
VAT = 20
Hotel_bill = (room_rate*num_nights)+(cost_of_services)
Total_hotel_bill = Hotel_bill*((VAT+100)/100)
print(Total_hotel_bill)


#QUESTION 5
#User = John
total_hrs_worked = 49

hourly_rate = 10
reg_hrs_per_week = 40
overtime_hourly_rate = 10 * 1.5
overtime_hrs = total_hrs_worked - reg_hrs_per_week

regular_pay = hourly_rate * reg_hrs_per_week
overtime_pay = overtime_hrs * overtime_hourly_rate

Total_pay = regular_pay + overtime_pay
print('John earned', int(Total_pay), 'pounds this week')


#QUESTION 6
distance = 200  #miles
speed = 10  #miles/hr

#Cost of Labour per journey
hourly_rate = 10 #£/hr
num_hrs_by_driver1 = distance/speed
cost_of_labour1 = hourly_rate * num_hrs_by_driver1

#Cost of fuel per journey
cost_per_unit = 6 #£/gallon
fuel_consum_rate = 34.6 #miles/gallon
total_gallons1 = distance/fuel_consum_rate #gallons
cost_of_fuel1 = total_gallons1 * cost_per_unit #£

#Total cost per journey
total_cost1 = cost_of_labour1 + cost_of_fuel1

#Checking for business viability
min_passengers = 70
high_tick_price = 20 #£
ticket_sale1 = min_passengers * high_tick_price

print(total_cost1)
print(ticket_sale1)
print(ticket_sale1*1.2)
if ticket_sale1>(total_cost1*1.2):
    print('route is vialable')
else:
    print('route is not viable')


#QUESTION 7 following question 6
distance = 200  #miles
road_type = 'motorway'
if road_type == 'A_road':
    speed = 60 #miles/hr
elif road_type == 'motorway':
    speed = 70 #miles/hr


#Cost of Labour per journey
driver_status = 'junior_driver'
if driver_status == 'senior_driver':
    hourly_rate = 40 #£/hr
elif driver_status == 'junior_driver':
    hourly_rate = 15 #£/hr

num_hrs_by_driver2 = distance/speed
cost_of_labour2 = hourly_rate * num_hrs_by_driver2

#Cost of fuel per journey
fuel_type = 'petrol'

if fuel_type == 'petrol':
    cost_per_unit = 5 #£/gallon
    fuel_consum_rate = 15  # miles/gallon
elif fuel_type == 'diesel':
    cost_per_unit = 6 #£/gallon
    fuel_consum_rate = 25  # miles/gallon

total_gallons2 = distance/fuel_consum_rate #gallons
cost_of_fuel2 = total_gallons2 * cost_per_unit #£

#Total cost per journey
total_cost2 = cost_of_labour2 + cost_of_fuel2

#Checking for business viability
min_passengers = 70
high_tick_price = 15 #£
ticket_sale2 = min_passengers * high_tick_price

print(total_cost2)
print(ticket_sale2)
print(ticket_sale2*1.2)
if ticket_sale2>(total_cost2*1.2):
    print('route is vialable')
else:
    print('route is not viable')

