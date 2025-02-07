x = torch.arange(12, dtype=torch.float32).reshape((3,4))
y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
x,y,x == y,x < y,x > y
(tensor([[ 0., 1., 2., 3.],
[ 4., 5., 6., 7.],
[ 8., 9., 10., 11.]]),
tensor([[2., 1., 4., 3.],
[1., 2., 3., 4.],
[4., 3., 2., 1.]]),
tensor([[False, True, False, True],
[False, False, False, False],
[False, False, False, False]]),
tensor([[ True, False, True, False],
[False, False, False, False],
[False, False, False, False]]),
tensor([[False, False, False, False],
[ True, True, True, True],
[ True, True, True, True]]))