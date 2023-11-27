import numpy as np
house = 1
rock = 1
attr = 0


def act(x):
    return 0 if x < 0.5 else 1


def main(house, rock, attr):
    main_massive = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, 0.5, 1]
    weight1 = np.array([w11, w12])
    weight2 = np.array([-1, 1])

    sum_hidden = np.dot(weight1, main_massive)
    print('значение сумм скрытого слоя:'+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('значения на выходаъ нейронов скрытого слоя :'+str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print('выходное значение HC:'+str(y))
    return y



res = main(house, rock, attr)
if res == 1:
    print('1')
else:
    print('0')




