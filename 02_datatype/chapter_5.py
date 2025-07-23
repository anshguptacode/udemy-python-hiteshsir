import sys #pre exixting libraries used for different task
current_temp=45.5
ideal_temp=45.4
temp_difference=current_temp-ideal_temp
print(f"Temprature diffence: {temp_difference}")
print(sys.float_info)
'''
Temprature diffence: 9.999965300266922e-10
Temprature diffence: 0.00999999999999801
Temprature diffence: 0.10000000000000142

sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
 min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
'''