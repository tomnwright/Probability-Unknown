import random
import matplotlib.pyplot as plt


class Experiment:
    def __init__(self, prob_a):
        self.prob_a = prob_a

    def trial(self, res=10000):
        result = random.randint(0, res)
        return result <= self.prob_a * res

    def sample_N(self, limit):
        N = 1
        while N <= limit:
            result = self.trial()
            if result:
                break
            N += 1

        return N


def test(resolution, reps_each, limit):
    data = []

    for i in range(resolution + 1):

        prob_a = i / resolution

        print(prob_a)
        exp = Experiment(prob_a)

        for j in range(reps_each):
            sample = exp.sample_N(limit)
            data.append((i, sample,))

    return data


def increment_dict(target_dict, key):
    if key not in target_dict:
        target_dict[key] = 0
    target_dict[key] += 1


def analyse(target_n, data, resolution):
    result = {}
    for i in range(resolution + 1):
        result[i] = 0

    total = 0

    for prob, val in data:
        if val == target_n:
            total += 1
            increment_dict(result, prob)

    x = []
    y = []

    for key in result:
        x.append(key / resolution)
        y.append(result[key] / total)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    test_res = 100

    d = test(test_res, 50000, 100)
    print(d)
    analyse(5, d, test_res)
