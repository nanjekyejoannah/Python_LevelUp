import  time
import memory_profiler as mem_profile

def modulus_of_numbers(nums, mod):
	for i in nums:
		yield (i % mod)

print('Memory Before: ' + str(mem_profile.memory_usage()) + 'MB' )

mod = (modulus_of_numbers([7,6,10,5], 3))

start_time = time.clock()
mod = modulus_of_numbers ((range(0,1000000)), 3)
end_time = time.clock()

print('Memory After: ' + str(mem_profile.memory_usage()) + 'MB' )
print ('Time:{}'.format(end_time - start_time))