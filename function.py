import  time
import memory_profiler as mem_profile # pip install memory_profiler

def modulus_of_numbers(nums, mod):
	final_list = []
	for i in nums:
		final_list.append(i % mod)
	return final_list
	
print('Memory Before: ' + str(mem_profile.memory_usage()) + 'MB' )

start_time = time.clock()
mod = modulus_of_numbers ((range(0,1000000)), 3)
end_time = time.clock()

print('Memory: ' + str(mem_profile.memory_usage()) + 'MB' )
print ('Time:{}'.format(end_time - start_time))

