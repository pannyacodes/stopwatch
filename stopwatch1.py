def largest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

def smallest(arr,n):
    min=arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min

print("these are the time from stopwatch in seconds")
arr=[10,324,45,90,980,40]
n=len(arr)
answer1=largest(arr,n)
answer2=smallest(arr,n)
print("largest in given array is",answer1)
print("smallest in given array is",answer2)
