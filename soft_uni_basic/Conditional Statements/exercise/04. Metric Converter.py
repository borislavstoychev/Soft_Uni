num = float(input())
in_metric = input()
out_metric = input()
if in_metric == 'mm' and out_metric == 'cm':
    result = num * 0.1
    print(f'{result: .3f}')
elif in_metric == 'mm' and out_metric == 'm':
    result = num * 0.001
    print(f'{result: .3f}')
elif in_metric == 'cm' and out_metric == 'mm':
    result = num * 10
    print(f'{result: .3f}')
elif in_metric == 'cm' and out_metric == 'm':
    result = num * 0.01
    print(f'{result: .3f}')
elif in_metric == 'm' and out_metric == 'cm':
    result = num * 100
    print(f'{result: .3f}')
elif in_metric == 'm' and out_metric == 'mm':
    result = num * 1000
    print(f'{result: .3f}')
else:
    print('Error')