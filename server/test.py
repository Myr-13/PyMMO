data = b'ghur-9438fh9hrfaf' + bytearray('∈', 'utf-8')
pack_end = bytearray('∈', 'utf-8')

print(
	-len(pack_end),
	data[-len(pack_end):],
	pack_end,
	data[-len(pack_end):] == pack_end
)

input()