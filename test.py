from src.Stack import Stack

def decimal2binary(item):
	S=Stack()
	while item>0:
		rem=item%2
		S.push(rem)
		item = item//2
	B=""
	while not S.isEmpty():
		B+=str(S.pop())
	return B

# test
print(decimal2binary(233))
